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
    sample1 = {"startDate":"12.01.2025","endDate":"","runConfig":[{"hierarchyEventConfigurationId":"","funcLoc":"","timeseriesId":"","facility":"","rule":{"ruleSet":"","processingInterval":"","side":"","rpmThreshold":"","recommendedKVal":"","aggMetric":["stddev","avg","min"]}}]}
    # Upload sample1 to blob storage under today's date folder with a uuid as the file name
    container_client = blob_service_client.get_container_client(os.environ["TEST_CONTAINER_NAME"])
    # todays date UTC in YYYY-MM-DDThh:mm:ssZ format
    today_date = date.today().strftime("%Y-%m-%dT%H:%M:%SZ")
    upload_path = f"{today_date}/{str(uuid.uuid4())}.json"
    print(f"Uploading blob to account url {account_url}, to container {os.environ['TEST_CONTAINER_NAME']} to path {upload_path}")
    blob_client = container_client.get_blob_client(upload_path)
    upload_status = blob_client.upload_blob(json.dumps(sample1), blob_type="BlockBlob", standard_blob_tier=StandardBlobTier.Hot)
    print(f"you can download the blob from: {upload_path}")



# x-ms-original-file: specification/app/resource-manager/Microsoft.App/ContainerApps/stable/2025-07-01/examples/Job_Start.json
if __name__ == "__main__":
    main()