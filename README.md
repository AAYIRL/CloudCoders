# Azure Resouce Automation

Many organizations utilize cloud services from various cloud vendors like Microsoft Azure. However, the manual process of creating any cloud based resource is a time-consuming and error-prone process. A POC is required that will automate this manual process. There is a frontend to the application which will act as an easy-to-use interface for the users.

Automate the process of creating the following resources from Microsoft Azure:
(1) Virtual Machine
(2) Azure Storage
(3) Database


**Overview of code base**

Here we are automating the process of Azure resource creation using Python and Azure libraries. There is a frontend which will take the input from the users. There is a listener (flask or Django) which will be 'listening' for any request from the frontend. The backend application will utilize the Azure Python SDK to programmatically create and manage VMs, storage resources and databases from Azure.

This solution will automate the Azure resource creation which will save time & will be less prone to error as there will be less human intervention. The same automation can be used to create multiple azure resources at a given time which is not possible using manual process.

```
├──|Cloud_Automation_Frontend/
     |__<react based files>
├──|Cloud_Automation_Backend/
    |__<VM Creation.py>
	|__<Storage.py>
	|__<Database.py>
├──|Start React/
├──|Start Flask/
├──|Changelog/
├──|README.md/
    
```

**Usecases covered:**
1. VM Provisioning
2. Storage Creation
3. Database Creation


**How to run the Code?**

- Run the **"Start React.bat"**
- The below screen will appear infront of you:

- Run the **"Start Flask.bat"**
- Script starts the backend flask server


Dependencies
------------
Package Version  
-- 
azure-common 1.1.28  
azure-core 1.26.2  
azure-identity 1.12.0  
azure-mgmt-compute 29.1.0  
azure-mgmt-core 1.3.2  
azure-mgmt-network 22.2.0  
azure-mgmt-rdbms 10.1.0  
azure-mgmt-resource 22.0.0  
azure-mgmt-storage 21.0.0


Authors
-------
* [Aman Surkar](mailto:<aman_surkar@persistent.com>)
* [Aayush Kumar](mailto:<aayush_kumar1@persistent.com>)
* [Abhijit Katore](mailto:<abhijit_katore@persistent.com>)
* [Aditi Gupta](mailto:<aditi_gupta1@persistent.com>)

Maintainers
-----------
## PSL Cloud Coders
