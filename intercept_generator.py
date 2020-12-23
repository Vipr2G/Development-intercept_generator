"""
    @Created on 18 Dec 2020
    @Author: Geoff Willis
    @Email: gwillis18@yahoo.com
    @Updated On:
    @Updated On:
    @template: Wrapper class for Intercpt attributes/fields

"""
from Intercept import Intercept
import config_reader
import parameter_generator



def initialize_config():
    global config
    config = config_reader.read_config_file()
    #unpack_config(config)



def build_intercept():
    gen = config.get("EMITTER").get("GENERAL")
    params = config.get("EMITTER").get("PARAMETERS")
    elnot = gen.get("ELNOT")
    num_intercepts = gen.get("number_intercepts")
    out_file_name = gen.get("output_file_name")

    #for param in params.values():
    rfs  = parameter_generator.process_parameters(params.get("RF"))
    pris = parameter_generator.process_parameters(params.get("PRI"))
    pds  = parameter_generator.process_parameters(params.get("PD"))
    scan = parameter_generator.process_parameters(params.get("SCAN"))
    intercept = Intercept(pris, rfs, pds, scan, "", "90.0", "0.0", "", elnot)
    print("*" * 80)
    print(intercept.intercept_map)



def run_tests(): 
    rfs = pgen.get_random_float_values_normal_dist(8500, 2, 10)
    #print(rfs)

    pris = pgen.get_random_float_values_normal_dist(533, 2, 20)
    print(pris)

    pds = pgen.get_random_float_values_normal_dist(.3, .1, 5)
    print(pds)

    scans = pgen.get_random_float_values_normal_dist(10.0, .1, 1)


#intercept = Intercept(pris, rfs, pds, scans, "D", "123.456", "222.1212", "A", "AIR01")
#print(intercept.pris)



initialize_config()
build_intercept()









