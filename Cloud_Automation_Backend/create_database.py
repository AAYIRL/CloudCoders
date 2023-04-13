import random, os
#import urllib.request as urll
from flask import *
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.rdbms.mysql import MySQLManagementClient
from azure.mgmt.rdbms.mysql.models import ServerForCreate, ServerPropertiesForDefaultCreate, ServerVersion

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

#This function creates resource group
def create_rg(rg_name, sub_id):
    subscription_id = sub_id
    resource_client = ResourceManagementClient(credential, subscription_id)
    RESOURCE_GROUP_NAME = rg_name
    LOCATION = "eastus"
    rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME, { "location": LOCATION })
    return print(f"Provisioned resource group {rg_result.name}")

def create_myql_server(db_server_name, db_admin_name, db_admin_password, rg_name, sub_id):
    mysql_client = MySQLManagementClient(credential, sub_id)
    # Provision the server and wait for the result
    poller = mysql_client.servers.begin_create(rg_name,
    db_server_name, 
        ServerForCreate(
            location='eastus',
            properties=ServerPropertiesForDefaultCreate(
                administrator_login=db_admin_name,
                administrator_login_password=db_admin_password,
                version=ServerVersion.FIVE7
            )
        )
    )
    server = poller.result()
    return print(f"Provisioned MySQL server {server.name}")


def provision_database(db_name, rg_name, db_server_name, sub_id):
    mysql_client = MySQLManagementClient(credential, sub_id)
    poller = mysql_client.databases.begin_create_or_update(rg_name,db_server_name, db_name, {})
    db_result = poller.result()
    return print(f"Provisioned MySQL database {db_result.name} with ID {db_result.id}")    


