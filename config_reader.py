"""
    @Created on 18 Dec 2020
    @Author: Geoff Willis
    @Email: gwillis18@yahoo.com
    @Updated On:
    @Updated On:
    @template: Read the JSON config file that defines intercept

"""


import json

def read_config_file()-> list:
    with open('intercept.json', 'r') as fh:
        data = json.load(fh)
        print(data )       
    return data