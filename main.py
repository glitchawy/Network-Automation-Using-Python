from classess import *

R1 = Router('Catalyst 8200 Series Edge' , 'Cisco IOS' , '192.168.1.1')
R1.get_desc()
router_int1 = Router.Interface('G' , '0/0' , '192.168.1.1' , 'UP')
router_int2 =  Router.Interface('G' , '0/1' , '192.168.1.2' , 'DOWN')
print("--------------------------------------------------------------------------")
router_int1.get_desc()
router_int2.get_desc()
print("--------------------------------------------------------------------------")
Sw1 = L3_Switch("Catalyst 9300", "Cisco IOS" , "10.10.1.1")
Sw1.get_desc()
print("--------------------------------------------------------------------------")

switch_int1 =  L3_Switch.Interface("FA","0/0","10.10.1.1","UP")
switch_int2 =  L3_Switch.Interface("FA","0/1","10.10.1.2","DOWN")

switch_int1.get_desc()
switch_int2.get_desc()

R1.device_data_csv()
Sw1.device_data_csv()

read_devices_from_csv('devices_data.csv')

json_file = print_json_file_content('interfaces.json')

pprint(json_file['G0/1'])



