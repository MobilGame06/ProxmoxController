import config
from proxmoxer import ProxmoxAPI
import time
import os

#Login
proxmox = ProxmoxAPI(config.hostname, user=config.user, password=config.password,verify_ssl=config.verify_ssl)

#Variables
node = proxmox.nodes.server()

#startvm
def startVm(startVmId):
    node.qemu(startVmId).status.start.post()
    MainMenu()

#startlxc
def startLxc(startLxcId):
    node.lxc(startLxcId).status.start.post()
    MainMenu()

#stopvm
def stopVm(stopVmId):
    node.qemu(stopVmId).status.stop.post()
    MainMenu()

def stopLxc(stopLxcId):
    node.lxc(stopLxcId).status.stop.post()
    MainMenu()


#Menu logo
def MenuLogo(text):
    print(r"""  ____                                                  
/\  _`\                                                
\ \ \L\ \_ __   ___   __  _   ___ ___     ___   __  _  
 \ \ ,__/\`'__\/ __`\/\ \/'\/' __` __`\  / __`\/\ \/'\ 
  \ \ \/\ \ \//\ \L\ \/>  <//\ \/\ \/\ \/\ \L\ \/>  </ 
   \ \_\ \ \_\\ \____//\_/\_\ \_\ \_\ \_\ \____//\_/\_\
    \/_/  \/_/ \/___/ \//\/_/\/_/\/_/\/_/\/___/ \//\/_/
                                                       
                                                """)
    print("By MobilGame06")
    getVersion = node.version.get()
    print("Proxmox Version: " + getVersion["version"])
    print("")
    print(text)
    print("-------------------------------------------")

#Start Menu
def StartMenu():
    MenuLogo("Start Menu")
    print("[1] vm")
    print("[2] lxc")
    startInput = int(input("[?]"))
    os.system('cls||clear')
    if startInput == 1:
        vmidMenu("start")
    elif startInput == 2:
        lxcIdMenu("start")

#Stop Menu
def StopMenu():
    MenuLogo("Stop Menu")
    print("[1] vm")
    print("[2] lxc")
    stopInput = int(input("[?]"))
    os.system('cls||clear')
    if stopInput == 1:
        vmidMenu("stop")
    elif stopInput == 2:
        lxcIdMenu("stop")

#vmid Menu
def vmidMenu(status):
    MenuLogo("lxcid Menu")
    print("Type your vm id")
    vmid = int(input("[ID]"))
    os.system('cls||clear')
    if status == "start":
        startVm(vmid)
    elif status == "stop":
        stopVm(vmid)

#lxcid Menu
def lxcIdMenu(status):
    MenuLogo("lxcid Menu")
    print("Type your lxc id")
    lxcid = int(input("[ID]"))
    os.system('cls||clear')
    if status == "start":
        startLxc(lxcid)
    elif status == "stop":
        stopLxc(lxcid)

#Main Menu
def MainMenu():
    MenuLogo("Main Menu")
    #Menu start
    print("[1] Start")
    print("[2] Stop")
    print("[3] Exit")
    mainInput = int(input("[?]"))
    os.system('cls||clear')
    if mainInput == 1:
        StartMenu()
    elif mainInput == 2:
        StopMenu()
    elif mainInput == 3:
        print("bye")
        os.system('cls||clear')





MainMenu()
