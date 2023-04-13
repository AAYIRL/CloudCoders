from flask import *
from create_database import *
from create_VirtualM import *
from Storage_Account import *
import logging
from datetime import datetime
import os

app = Flask(__name__)

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
os.chdir('./')
path = os.getcwd()
print(path)
LOGFILE = path + '\log.log'
logging.basicConfig(filename=LOGFILE, level=logging.INFO)

def log_and_print(message):
    logging.info(message)
    print(message)

def start_script(fun_name):
    log_and_print("\n############## Script - {} Creation STARTED ".format(fun_name))
    log_and_print(" Date: "+ dt_string +"")
    log_and_print("---------------------------------------------------------------------------")

def end_script(fun_name):
    log_and_print("\n############## Script - {} Creation ENDED ".format(fun_name))
    log_and_print("\n############## LOGS at - " + LOGFILE)
    log_and_print("---------------------------------------------------------------------------")


@app.route('/create_storage', methods=['GET', 'POST'])
def Create_Storage():
    rg_name=request.form['rg_name']
    stacc_name=request.form['stacc_name']
    cont_name=request.form['cont_name']
    sub_id=request.form['sub_id']
    cont_name = cont_name.lower()
    stacc_name = stacc_name.lower()
    try:
        start_script('Storage')
        create_rg(rg_name, sub_id)
        provision_storage(rg_name, stacc_name, sub_id)
        provision_container(rg_name, stacc_name, cont_name, sub_id)
        end_script('Storage')
        return redirect("http://localhost:3000/storage-account?success=true")
    except:
        return redirect("http://localhost:3000/storage-account?success=false")




@app.route('/create_VirtualM', methods=['GET', 'POST'])
def create_VM():
    sub_id = request.form.get('sub_id')
    rg_name = request.form.get('rg_name')
    vm_name = request.form.get('vm_name')
    vm_type = request.form.get('vm_type')
    username = request.form.get('username')
    password = request.form.get('password')
    try:
        start_script('Virtual Machine')
        create_rg(rg_name, sub_id)
        provision_network(rg_name, sub_id)
        subnet_result = provision_subnet(rg_name, sub_id)
        ip_address_result = provison_ip(rg_name, sub_id)
        nic_result = provision_NIC(rg_name, sub_id, subnet_result, ip_address_result)
        provision_VM(rg_name, sub_id, vm_name, vm_type, username, password, nic_result)
        end_script('Virtual Machine')
        return redirect("http://localhost:3000/virtual-machine?success=true")
    except:
        return redirect("http://localhost:3000/virtual-machine?success=false")

@app.route('/create_database', methods=['GET', 'POST'])
def Create_database():
    rg_name=request.form['rg_name']
    sub_id=request.form['sub_id']
    db_name = request.form['db_name']
    db_server_name=request.form['db_server_name']
    db_admin_name=request.form['db_admin_name']
    db_admin_password=request.form['db_admin_password']
    try:
        start_script('Database')
        create_rg(rg_name, sub_id)
        create_myql_server(db_server_name, db_admin_name, db_admin_password, rg_name, sub_id)
        provision_database(db_name, rg_name, db_server_name, sub_id)
        end_script('Database')
        return redirect("http://localhost:3000/mysql-database?success=true")
    except:
        return redirect("http://localhost:3000/mysql-database?success=false")

if __name__=='__main__':
    app.run()