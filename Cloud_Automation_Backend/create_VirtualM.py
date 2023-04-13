# Import the needed credential and management objects from the libraries.
import os
from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from flask import *

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

# Step 2: provision a virtual network
def provision_network(rg_name, sub_id):
    VNET_NAME = "vm-service-vnet"
    SUBNET_NAME = "vm-service-subnet"
    IP_NAME = "vm-service-ip"
    NIC_NAME = "vm-service-nic"
    subscription_id = sub_id
    RESOURCE_GROUP_NAME = rg_name
    LOCATION = 'eastus'
    # Obtain the management object for networks
    network_client = NetworkManagementClient(credential, subscription_id)
    # Provision the virtual network and wait for completion
    poller = network_client.virtual_networks.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        VNET_NAME,
        {
            "location": LOCATION,
            "address_space": {"address_prefixes": ["10.0.0.0/16"]},
        },
    )
    vnet_result = poller.result()
    print(f"Provisioned virtual network {vnet_result.name} with address prefixes {vnet_result.address_space.address_prefixes}")

# Step 3: Provision the subnet and wait for completion
def provision_subnet(rg_name, sub_id):
    subscription_id = sub_id
    RESOURCE_GROUP_NAME = rg_name
    VNET_NAME = "vm-service-vnet"
    SUBNET_NAME = "vm-service-subnet"

    network_client = NetworkManagementClient(credential, subscription_id)
    poller = network_client.subnets.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        VNET_NAME,
        SUBNET_NAME,
        {"address_prefix": "10.0.0.0/24"},
    )
    subnet_result = poller.result()

    print(f"Provisioned virtual subnet {subnet_result.name} with address prefix {subnet_result.address_prefix}")
    return subnet_result

# Step 4: Provision an IP address and wait for completion
def provison_ip(rg_name, sub_id):
    subscription_id = sub_id
    RESOURCE_GROUP_NAME = rg_name
    IP_NAME = "vm-service-ip"
    LOCATION = 'eastus'
    network_client = NetworkManagementClient(credential, subscription_id)
    poller = network_client.public_ip_addresses.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        IP_NAME,
        {
            "location": LOCATION,
            "sku": {"name": "Standard"},
            "public_ip_allocation_method": "Static",
            "public_ip_address_version": "IPV4",
        },
    )

    ip_address_result = poller.result()

    print(f"Provisioned public IP address {ip_address_result.name} with address {ip_address_result.ip_address}"
    )
    return ip_address_result

# Step 5: Provision the network interface client
def provision_NIC(rg_name, sub_id, subnet_result, ip_address_result):
    RESOURCE_GROUP_NAME = rg_name
    NIC_NAME = "vm-service-nic"
    LOCATION = 'eastus'
    IP_CONFIG_NAME = "vm-service-ip-config"
    subscription_id = sub_id
    network_client = NetworkManagementClient(credential, subscription_id)
    poller = network_client.network_interfaces.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        NIC_NAME,
        {
            "location": LOCATION,
            "ip_configurations": [
                {
                    "name": IP_CONFIG_NAME,
                    "subnet": {"id": subnet_result.id},
                    "public_ip_address": {"id": ip_address_result.id},
                }
            ],
        },
    )

    global nic_result
    nic_result = poller.result()

    print(f"Provisioned network interface client {nic_result.name}")
    return nic_result


# Step 6: Provision the virtual machine

def provision_VM(rg_name, sub_id, vm_name, vm_type, username, password, nic_result):

    subscription_id = sub_id
    RESOURCE_GROUP_NAME = rg_name
    # Obtain the management object for virtual machines
    compute_client = ComputeManagementClient(credential, subscription_id)

    VM_NAME = vm_name
    VM_TYPE = vm_type
    USERNAME = username
    PASSWORD = password
    nic_result = nic_result
    LOCATION = 'eastus'

    print(f"Provisioning virtual machine {VM_NAME}; this operation might take a few minutes.")

    poller = compute_client.virtual_machines.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        VM_NAME,
        {
            "location": LOCATION,
            "storage_profile": {
                "image_reference": {
                    "publisher": "Canonical",
                    "offer": "UbuntuServer",
                    "sku": "16.04.0-LTS",
                    "version": "latest",
                }
            },
            "hardware_profile": {"vm_size": VM_TYPE},
            "os_profile": {
                "computer_name": VM_NAME,
                "admin_username": USERNAME,
                "admin_password": PASSWORD,
            },
            "network_profile": {
                "network_interfaces": [
                    {
                        "id": nic_result.id,
                    }
                ]
            },
        },
    )

    vm_result = poller.result()
    print(f"Provisioned virtual machine {vm_result.name}")

