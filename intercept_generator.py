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
rf_accumulator = []
pri_accumulator = []

def read_config_file():
    with open('intercept.json', 'r') as fh:
        data = json.load(fh)     
    return data

def write_intercept(output_file_name, intercept):
    with open (output_file_name, 'w') as fh:
         json.dump(intercept, fh, indent=4)    

def populate_param_accumulator(params, param_type):
    accum = []
    if param_type=="PRI":
        accum=pri_accumulator
    if param_type=="RF":
        accum=rf_accumulator
    #for param in params:
    #    accum.append(param)
    accum.append([param for param in params])

def build_intercept(config):
    gen = config.get("GENERAL")
    params = config.get("PARAMETERS")
    elnot = gen.get("ELNOT")
    domain = gen.get("domain")
    mod_type = params.get("PRI").get("modulation_type")
    geos = params.get("GEO")

    intercept = {"ELNOT": elnot, "mod_type": mod_type, "domain": domain}
    intercept["rfs"]  = pgen.process_parameters(params.get("RF"))
    populate_param_accumulator(intercept["rfs"], "RF")
    intercept["pris"] = pgen.process_parameters(params.get("PRI"))
    populate_param_accumulator(intercept["pris"], "PRI")
    intercept["pds"]  = pgen.process_parameters(params.get("PD"))
    intercept["scan"] = pgen.process_parameters(params.get("SCAN"))
    if geos:
       location = pgen.generate_random_geo_from_seed(geos)
       #print(location)
       intercept['location'] = location

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
out_file_name = config.get("EMITTER")[0].get("GENERAL").get("output_file_name")

out_file = open(out_file_name, "a")
out_file.write("{INTERCEPTS: [ {")
guid = 0

emitter_configs = config.get("EMITTER")
for emitter_config in emitter_configs:
    num_intercepts = int (emitter_config.get("GENERAL").get("number_intercepts"))
    for i in range(num_intercepts):
        intercept = build_intercept(emitter_config)
        intercept["id"] = guid
        out_file.write(json.dumps(intercept, indent=4))
        out_file.write(",")
        guid+=1

out_file.write("]}")
out_file.close()


data = pgen.get_random_float_values_normal_dist()
plt.hist(rf_accumulator, bins=20)
plt.show()
plt.hist(pri_accumulator, bins=20)
plt.show()

#import pandas as pd 
#df = pd.read_json("LND01_intercepts.json", lines=True)











