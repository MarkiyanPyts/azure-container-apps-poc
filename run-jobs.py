from azure.identity import DefaultAzureCredential

from azure.mgmt.appcontainers import ContainerAppsAPIClient
import json
import os
import dotenv

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


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"],
    )

    CONTAINER_APPS_JOB_NAME = os.environ["CONTAINER_APPS_JOB_NAME"]
    IMAGE_NAME = os.environ["IMAGE_NAME"]
    RESOURCE_GROUP_NAME = os.environ["RESOURCE_GROUP_NAME"]

    sample1 = {"startDate":"12.01.2025","endDate":"","runConfig":[{"hierarchyEventConfigurationId":"","funcLoc":"","timeseriesId":"","facility":"","rule":{"ruleSet":"","processingInterval":"","side":"","rpmThreshold":"","recommendedKVal":"","aggMetric":["stddev","avg","min"]}}]}
    sample2 = {"startDate":"12.01.2026","endDate":"","runConfig":[{"hierarchyEventConfigurationId":"","funcLoc":"","timeseriesId":"","facility":"","rule":{"ruleSet":"","processingInterval":"","side":"","rpmThreshold":"","recommendedKVal":"","aggMetric":["stddev","avg","min"]}}]}

    template1 = {
        "containers": [
            {
                "name": CONTAINER_APPS_JOB_NAME,
                "image": IMAGE_NAME,
                "env": [
                    {"name": "TEST_ENV_VAR", "value": json.dumps(sample1)}
                ]
            }
        ]
    }

    template2 = {
        "containers": [
            {
                "name": CONTAINER_APPS_JOB_NAME,
                "image": IMAGE_NAME,
                "env": [
                    {"name": "TEST_ENV_VAR", "value": json.dumps(sample2)}
                ]
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