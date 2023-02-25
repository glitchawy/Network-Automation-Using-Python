from netmiko import ConnectHandler
connection = {
    'device_type' : 'cisco_ios' ,
    'ip' : 'sbx-nxos-mgmt.cisco.com' ,
    'username' : 'admin' ,
    'password' : 'Admin_1234!',
    'port' : 22
}

connection2 = ConnectHandler(**connection)
output = connection2.send_command('show ip int brief | json-pretty')
print(output)
