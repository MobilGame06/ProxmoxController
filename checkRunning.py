import config
from proxmoxer import ProxmoxAPI

proxmox = ProxmoxAPI(config.hostname, user=config.user, password=config.password,verify_ssl=config.verify_ssl)


node = proxmox.nodes.server()
vmid = 152

getVm = node.qemu(vmid).status.current.get()
print(getVm['status'])