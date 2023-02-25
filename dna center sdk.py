import json
import dnacentersdk.api
import urllib3
from pprint import *
#urllib3.disable_warnings()
connectionnn = dnacentersdk.api.DNACenterAPI(username='devnetuser', password='Cisco123!', base_url="https://sandboxdnac2.cisco.com:443" , verify=False)
devices = connectionnn.devices.get_device_list()
for device in devices.response:
    pprint(device)