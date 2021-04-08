#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Created on 21 Dec 2020
    @Author: Geoff Willis
    @Email: gwillis18@yahoo.com
    @Updated On:
    @Updated On:
    @template: Randomize provided seeds using various statistical models
"""

import numpy as np

#First two generate test data, second two are called by system
def get_random_float_values_uniform_dist_test(low = 9500.0, high = 0.1, size = 500 ):
    return np.random.uniform(low, high, size)

def get_random_float_values_normal_dist(median = 9500., sigma = 1, size = 1000000):
    return np.random.normal(median, sigma, size)

#These are actually called by API, above can be used to gen data for plots to demonstrate the ranges
def generate_random_float_uniform(value, tolerance):
    half_tol = float(tolerance)/2
    val = float(value)
    return np.random.uniform(val-half_tol, val+half_tol)

def generat_random_float_uniform_less_than_seed(value, tolerance):
    return np.random.uniform(value-tolerance, value)

def generate_random_float_normal(nom_val, sigma = 0.1):
    return np.random.normal(float(nom_val), float (sigma))

#Insert here if desire a different statistical model to generate random value from seed
def process_parameters(config):
    if(config):
        prob_distribution = config.get("distribution")
        prob_tolerance = config.get("tolerance")
        if(prob_distribution == "NORMAL"):
            return [generate_random_float_normal(element, prob_tolerance) for element in config.get("data")]
        elif(prob_distribution == "UNIFORM"):
            return [generate_random_float_uniform(element, prob_tolerance) for element in config.get("data")]

def generate_random_geo_from_seed(config):
    seed_point = config.get("center_point")
    major_axis = config.get("ellipse_major_axis_length")
    orientation = config.get("ellipse_major_axis_angle")

    center = seed_point[np.random.randint(len(seed_point))]
    major = np.random.choice(major_axis)
    orient = np.random.choice(orientation)

    random_lat = generate_random_float_normal(center[0], 0.13)
    random_lon = generate_random_float_normal(center[1], 0.13)
    random_major = generate_random_float_normal(major, 2)
    random_minor = np.abs(generat_random_float_uniform_less_than_seed(random_major, 2.0))
    random_angle = generate_random_float_normal(orient, 0.3)

    return dict(lat=random_lat, lon=random_lon, major_axis=random_major, minor_axis=random_minor, orientation=random_angle)

