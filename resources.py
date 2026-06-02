import os  
from azure.identity import DefaultAzureCredential  
from azure.mgmt.resource import ResourceManagementClient  
  
# Authentication  
credential = DefaultAzureCredential()  
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]  
  
# Initialize Resource Management client  
resource_management_client = ResourceManagementClient(credential, subscription_id)  
  
# List available resource providers and select ProviderNamespace and RegistrationState  
providers = resource_management_client.providers.list()  
  
for provider in providers:  
    print(f"ProviderNamespace: {provider.namespace}, RegistrationState: {provider.registration_state}")