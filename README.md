# Run Locally
podman compose up --build

# ACR Login With Podman
1. az acr login -n testacrmarkiyan --expose-token
2. fetch values from loginServer and accessToken and username
3. podman login <your-registry-name>.azurecr.io -u 00000000-0000-0000-0000-000000000000 -p $TOKEN
    e.g podman login testacrmarkiyan.azurecr.io -u 00000000-0000-0000-0000-000000000000 -p $TOKEN

## Push Build And Push Image To Registry
podman build -t testacrmarkiyan.azurecr.io/azure-container-apps-poc:v1 .
podman push testacrmarkiyan.azurecr.io/azure-container-apps-poc:v1

## Check Container In Registry And Tags
az acr repository list -n testacrmarkiyan -o table
az acr repository show-tags -n testacrmarkiyan --repository azure-container-apps-poc -o table