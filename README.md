# ACR Login With Podman
1. az acr login -n testAcrMarkiyan
2. fetch values from loginServer and accessToken and username
3. podman login <your-registry-name>.azurecr.io -u 00000000-0000-0000-0000-000000000000 -p $TOKEN
    e.g podman login testAcrMarkiyan.azurecr.io -u 00000000-0000-0000-0000-000000000000 -p $TOKEN
