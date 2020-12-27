#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Created on 18 Dec 2020
    @Author: Geoff Willis
    @Email: gwillis18@yahoo.com
    @Updated On:
    @Updated On:
    @template: Wrapper class for Intercpt attributes/fields
"""

import json
import parameter_generator as pgen
import matplotlib.pyplot as plt

#config = None

def read_config_file()-> list:
    with open('intercept.json', 'r') as fh:
        data = json.load(fh)     
    return data

def write_intercept(output_file_name, intercept):
    with open (output_file_name, 'w') as fh:
         json.dump(intercept, fh, indent=4)    

def build_intercept():
    global config
    gen = config.get("EMITTER").get("GENERAL")
    params = config.get("EMITTER").get("PARAMETERS")
    elnot = gen.get("ELNOT")
    domain = gen.get("domain")
    mod_type = params.get("PRI").get("modulation_type")

    intercept = {"ELNOT": elnot, "mod_type": mod_type, "domain": domain}
    intercept["rfs"]  = pgen.process_parameters(params.get("RF"))
    intercept["pris"] = pgen.process_parameters(params.get("PRI"))
    intercept["pds"]  = pgen.process_parameters(params.get("PD"))
    intercept["scan"] = pgen.process_parameters(params.get("SCAN"))

    return intercept

def run_tests(): 
    rfs = pgen.get_random_float_values_normal_dist(8500, 2, 10)
    print(rfs)

    pris = pgen.get_random_float_values_normal_dist(533, 2, 20)
    print(pris)

    pds = pgen.get_random_float_values_normal_dist(.3, .1, 5)
    print(pds)

    scans = pgen.get_random_float_values_normal_dist(10.0, .1, 1)
    print(scans)



#Here is where the work gets done
config = read_config_file()
out_file_name = config.get("EMITTER").get("GENERAL").get("output_file_name")
num_intercepts = int (config.get("EMITTER").get("GENERAL").get("number_intercepts"))

out_file = open(out_file_name, "a")
out_file.write("{INTERCEPTS: [ {")

for i in range(num_intercepts):
    intercept = build_intercept()
    intercept["id"] = i
    out_file.write(json.dumps(intercept, indent=4))
    out_file.write(",")

out_file.write("]}")
out_file.close()


data = pgen.get_random_float_values_normal_dist()
plt.hist(data, bins=30)
plt.show()

import pandas as pd 
df = pd.read_json("LND01_intercepts", orient='split')











