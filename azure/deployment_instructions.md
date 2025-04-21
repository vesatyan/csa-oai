
## Azure Deployment Setup

### 1. Create Azure Container Registry
```bash
az acr create --resource-group <YourResourceGroup> --name <YourRegistryName> --sku Basic
```

### 2. Build and Push Docker Image (Manual)
```bash
az acr login --name <YourRegistryName>
docker build -t <YourRegistryName>.azurecr.io/cloud-suitability-app:latest .
docker push <YourRegistryName>.azurecr.io/cloud-suitability-app:latest
```

### 3. Create Azure Web App for Containers
```bash
az webapp create --resource-group <YourResourceGroup> --plan <YourAppServicePlan>   --name <YourAppName> --deployment-container-image-name <YourRegistryName>.azurecr.io/cloud-suitability-app:latest
```

### 4. Configure GitHub Secrets
Add the following to your GitHub repo secrets:
- `AZURE_CREDENTIALS`: Azure service principal JSON
- `REGISTRY_LOGIN_SERVER`: <YourRegistryName>.azurecr.io
- `REGISTRY_USERNAME`: ACR username
- `REGISTRY_PASSWORD`: ACR password
- `AZURE_WEBAPP_NAME`: Your web app name

