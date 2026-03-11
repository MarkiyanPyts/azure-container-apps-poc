from azure.identity import DefaultAzureCredential

from azure.mgmt.appcontainers import ContainerAppsAPIClient
import json
import os
import dotenv
import uuid
from datetime import date
from azure.storage.blob import BlobServiceClient, StandardBlobTier

dotenv.load_dotenv()

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-appcontainers
# USAGE
    python job_start.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""

def uploadToBlob(credential, jsonData) -> str:
    account_url = f"https://{os.environ['STORAGE_ACCOUNT_NAME']}.blob.core.windows.net"

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=credential)

    container_client = blob_service_client.get_container_client(os.environ["STORAGE_CONTAINER_NAME"])
    # todays date UTC in YYYY-MM-DDThh:mm:ssZ format
    today_date = date.today().strftime("%Y-%m-%dT%H:%M:%SZ")
    upload_path = f"{today_date}/{str(uuid.uuid4())}.json"
    blob_client = container_client.get_blob_client(upload_path)
    blob_client.upload_blob(json.dumps(jsonData), blob_type="BlockBlob", standard_blob_tier=StandardBlobTier.Hot)

    return upload_path


def main():
    credential = DefaultAzureCredential()
    client = ContainerAppsAPIClient(
        credential=credential,
        subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"],
    )

    CONTAINER_APPS_JOB_NAME = os.environ["CONTAINER_APPS_JOB_NAME"]
    RESOURCE_GROUP_NAME = os.environ["RESOURCE_GROUP_NAME"]

    job = client.jobs.get(
        resource_group_name=RESOURCE_GROUP_NAME,
        job_name=CONTAINER_APPS_JOB_NAME
    )

    base_container = job.template.containers[0]

    base_container_env_objects = base_container.env if base_container.env is not None else []

    sample1 = {"startDate":"12.01.2027","endDate":"","runConfig":[{"hierarchyEventConfigurationId":"","funcLoc":"","timeseriesId":"","facility":"","rule":{"ruleSet":"","processingInterval":"","side":"","rpmThreshold":"","recommendedKVal":"","aggMetric":["stddev","avg","min"]}}]}
    sample_1_upload_path = uploadToBlob(credential, sample1)
    sample2 = {"startDate":"12.01.2028","endDate":"","runConfig":[{"hierarchyEventConfigurationId":"","funcLoc":"","timeseriesId":"","facility":"","rule":{"ruleSet":"","processingInterval":"","side":"","rpmThreshold":"","recommendedKVal":"","aggMetric":["stddev","avg","min"]}}]}
    sample_2_upload_path = uploadToBlob(credential, sample2)
    template1 = {
        "containers": [
            {
                "name": base_container.name,
                "image": base_container.image,
                "env": base_container_env_objects + [{"name": "STORAGE_CONFIG_FILE_PATH", "value": sample_1_upload_path}]
            }
        ]
    }

    template2 = {
        "containers": [
            {
                "name": base_container.name,
                "image": base_container.image,
                "env": base_container_env_objects + [{"name": "STORAGE_CONFIG_FILE_PATH", "value": sample_2_upload_path}]
            }
        ]
    }

    jobResponse1 = client.jobs.begin_start(
        resource_group_name=RESOURCE_GROUP_NAME,
        job_name=CONTAINER_APPS_JOB_NAME,
        template=template1
    ).result()
    print(jobResponse1)

    jobResponse2 = client.jobs.begin_start(
        resource_group_name=RESOURCE_GROUP_NAME,
        job_name=CONTAINER_APPS_JOB_NAME,
        template=template2 
    ).result()
    print(jobResponse2)


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/ContainerApps/stable/2025-07-01/examples/Job_Start.json
if __name__ == "__main__":
    main()