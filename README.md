# Run Locally
uv sync
podman compose up --build

## Run demo code


# ACR Login With Podman
1. az acr login -n testacrmarkiyan --expose-token
2. fetch values from loginServer and accessToken and username
3. podman login <your-registry-name>.azurecr.io -u 00000000-0000-0000-0000-000000000000 -p $TOKEN
    e.g podman login testacrmarkiyan.azurecr.io -u 00000000-0000-0000-0000-000000000000 -p $TOKEN

## Push Build And Push Image To Registry
# Note: use --platform linux/amd64 to ensure compatibility with Azure Container Apps (required when building on Apple Silicon)
podman build --platform linux/amd64 -t testacrmarkiyan.azurecr.io/azure-container-apps-poc:v1 .
podman push testacrmarkiyan.azurecr.io/azure-container-apps-poc:v1

## Check Container In Registry And Tags
az acr repository list -n testacrmarkiyan -o table
az acr repository show-tags -n testacrmarkiyan --repository azure-container-apps-poc -o table

## Container JOB API Docs
https://learn.microsoft.com/en-us/rest/api/resource-manager/containerapps/jobs-executions/list?view=rest-resource-manager-containerapps-2025-07-01&tabs=Python

## Useful Links
https://stackoverflow.com/questions/79458024/azure-container-apps-run-multiple-job-with-different-env-variable