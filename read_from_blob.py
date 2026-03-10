import io
import os
import uuid
import json
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobBlock, BlobClient, StandardBlobTier

from datetime import date
import dotenv

dotenv.load_dotenv()


def main():
    print('AZURE_CLIENT_ID', os.environ['AZURE_CLIENT_ID'])
    account_url = f"https://{os.environ['STORAGE_ACCOUNT_NAME']}.blob.core.windows.net"
    credential = DefaultAzureCredential()

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=credential)

    container_client = blob_service_client.get_container_client(os.environ["TEST_CONTAINER_NAME"])
    # read json file from blob storage, use the same path as upload_to_blob.py
    # https://sacontainerappjobpoc.blob.core.windows.net/test/2026-03-10T00:00:00Z/f3ddeb69-9e58-429b-ae52-b1b6e0fc8c51.json
    file_path = "2026-03-10T00:00:00Z/caed3097-0b18-4880-9455-af129d6acabe.json"
    blob_client = container_client.get_blob_client(file_path)
    downloaded_blob = blob_client.download_blob().readall()
    json_content = json.loads(downloaded_blob)
    start_date = json_content['startDate']
    print(f"Start date from blob: {start_date}")
    print(f"Downloaded blob content: {json.dumps(json_content, indent=2)}")
    
if __name__ == "__main__":
    main()