import csv
import json
from pprint import *

class Router :
    '''New class for Router objects '''
    def __init__(self , Model , SWversion , Router_ID):
        self.model = Model
        self.software_version = SWversion
        self.Router_ID = Router_ID

    def get_desc(self):
        print('Router model = {}'.format(self.model))
        print('Software Version = {} '.format(self.software_version))
        print('Router ID = {}'.format(self.Router_ID))

    def device_data_csv(self):
        file = open('devices_data.csv', 'a')
        file_writing = csv.writer(file)
        file_writing.writerow([self.model , self.software_version , self.Router_ID])
        file.close()


    class Interface :
        '''Router Interfaces is part of the Router object'''
        def __init__(self , Type ,Number , IP_Address , State ):
            '''
            :param Type: 'G' for gigabit ethernet , 'FA' for fast ethernet
            :param Number: Number of port
            :param IP_Address: really ??
            :param State: 'UP' or 'DOWN'
            '''
            self.Interface_number =  Number
            self.Type =Type
            self.IP_Address = IP_Address
            self.State = State

        def get_desc(self):
            print('Interface {} {} with IP Address of : {} is {}'.format(self.Type , self.Interface_number , self.IP_Address , self.State))

class L3_Switch (Router) :
    def get_desc(self):
        print('Switch model = {}'.format(self.model))
        print('Software Version = {} '.format(self.software_version))
        print('Switch ID = {}'.format(self.Router_ID))

    def device_data_csv(self):
        file = open('devices_data.csv', 'a')
        file_writing = csv.writer(file)
        file_writing.writerow([self.model , self.software_version , self.Router_ID])
        file.close()

def read_devices_data_from_code(device) :
    Device_type = None
    if type(device) == Router :
        Device_type = 'Router'
        print("The {} with model {} & Software of {} with ID {} ".format( Device_type  ,device.model , device.software_version , device.Router_ID  ))

def read_devices_from_csv(file) :
    file = open(file , 'r')
    devices_list = csv.reader(file)
    for device in devices_list :
        if len(device) == 0 :
            continue
        else:
            print("The device with model {} & Software of {} with ID {} ".format( device[0] , device[1] , device[2]  ))

def print_json_file_content(file):
    with open(file) as data :
        json_data = data.read()
        dictionary  = json.loads(json_data)
        return dictionary













