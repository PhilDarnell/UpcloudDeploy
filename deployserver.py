import requests
import upcloud_api
from upcloud_api import Server, Storage, ZONE, login_user_block

manager = upcloud_api.CloudManager('darnellapi', 'Master1960#')
manager.authenticate()

noofservers = 3

login_user = login_user_block(
    username='theuser',
    ssh_keys=['ssh-rsa AAAAB3NzaC1yc2EAA[...]ptshi44x user@some.host'],
    create_password=False
)

for inc in range(0, noofservers):
    server_config = Server(
                title='Server'+str(inc),
                plan='1xCPU-1GB',
                hostname='server'+str(inc)+'.darnell.com',
                zone=ZONE.Chicago,
                storage_devices=[
                    Storage(os='CentOS 6.5', size=25),
                ],
                login_user=login_user,
                user_data='/createproxy.sh'
            )

    manager.create_server(server_config)
print("end of loop")
