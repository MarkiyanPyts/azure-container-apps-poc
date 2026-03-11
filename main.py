import json
import os
import time
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobBlock, BlobClient, StandardBlobTier


def read_job_config_from_blob(storage_config_file_path):
    print('AZURE_CLIENT_ID', os.environ['AZURE_CLIENT_ID'])
    account_url = f"https://{os.environ['STORAGE_ACCOUNT_NAME']}.blob.core.windows.net"
    credential = DefaultAzureCredential()

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=credential)

    container_client = blob_service_client.get_container_client(os.environ["STORAGE_CONTAINER_NAME"])
    # read json file from blob storage, use the same path as upload_to_blob.py
    # https://sacontainerappjobpoc.blob.core.windows.net/test/2026-03-10T00:00:00Z/f3ddeb69-9e58-429b-ae52-b1b6e0fc8c51.json
    file_path = storage_config_file_path
    blob_client = container_client.get_blob_client(file_path)
    downloaded_blob = blob_client.download_blob().readall()

    return json.loads(downloaded_blob)


def main():
    duration = 120  # seconds
    interval = 10
    elapsed = 0
    storage_config_file_path = os.environ.get("STORAGE_CONFIG_FILE_PATH", "{}")
    print(f"Raw STORAGE_CONFIG_FILE_PATH: {storage_config_file_path}")
    try:
        config = read_job_config_from_blob(storage_config_file_path)
        print(f"Successfully read job config from blob: {json.dumps(config, indent=2)}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse STORAGE_CONFIG_FILE_PATH as JSON: {e}")
        config = {}
    start_date = config.get("startDate", "N/A")

    print(f"Job started. Running for {duration // 60} minutes... [startDate={start_date}]")

    while elapsed < duration:
        time.sleep(interval)
        elapsed += interval
        print(f"Progress: {elapsed}/{duration}s ({int(elapsed / duration * 100)}%) [startDate={start_date}]")

    print(f"Job completed successfully. [startDate={start_date}]")


if __name__ == "__main__":
    main()
