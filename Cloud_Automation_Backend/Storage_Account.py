#import libraries
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from flask import *

#Credentials
credential = AzureCliCredential()


#This function creates resource group
def create_rg(rg_name, sub_id):
    subscription_id = sub_id
    resource_client = ResourceManagementClient(credential, subscription_id)
    RESOURCE_GROUP_NAME = rg_name
    LOCATION = "eastus"
    rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME, { "location": LOCATION })
    return print(f"Provisioned resource group {rg_result.name}")

#This function creates Storage Account
def provision_storage(rg_name, stacc_name, sub_id):
    subscription_id = sub_id
    RESOURCE_GROUP_NAME = rg_name
    LOCATION = "eastus"
    storage_client = StorageManagementClient(credential, subscription_id)    
    STORAGE_ACCOUNT_NAME = stacc_name
    poller = storage_client.storage_accounts.begin_create(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME,
        {
            "location" : LOCATION,
            "kind": "StorageV2",
            "sku": {"name": "Standard_LRS"}
        }
    )
    account_result = poller.result()
    return print(f"Provisioned storage account {account_result.name}")

#This function creates Container/Blob
def provision_container(rg_name, stacc_name, cont_name, sub_id):
    subscription_id = sub_id
    RESOURCE_GROUP_NAME = rg_name
    STORAGE_ACCOUNT_NAME = stacc_name    
    CONTAINER_NAME = cont_name
    storage_client = StorageManagementClient(credential, subscription_id)
    container = storage_client.blob_containers.create(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME, CONTAINER_NAME, {})
    return print(f"Provisioned blob container {container.name}")    
