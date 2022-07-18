import numpy as np
import math
import random
import time

def rasterize_0d(data, rast_multiplier):
    return data * rast_multiplier;

def rasterize_1d(data, rast_multiplier):
    new_data = [];
    if data:
        for i in data:
            new_data.append(i * rast_multiplier);
    return new_data;

def filt_limit(x, xmin, xmax):
    if x < xmin:
        x = xmin;
    elif x > xmax:
        x = xmax;
    return x;

def create_normal_dist(mean, sd):
    normal_dist = [];
    if mean and sd:
        dist_range = [mean - (sd * 2), mean + (sd * 2)]; #arbitrary range 
        dist_space = np.arange(dist_range[0], dist_range[1], .1); #decimal point .0
        normal_dist = (np.pi*sd) * np.exp(-0.5*((dist_space-mean)/sd)**2);
    return normal_dist;

def create_gaussian(mean, sd, drange):
    normal_dist = [];
    if mean and sd:
        dist_space = np.arange(0, drange[1]-drange[0], 1.0); #decimal point .0
        normal_dist = (np.pi*sd) * np.exp(-0.5*((dist_space-mean)/sd)**2);
    return normal_dist;

def sample_from_normal_dist(normal_dist, n):
    samples = [];
    for s in range(n):
        samples.append(normal_dist[random.randint(0, len(normal_dist)-1)]);
    return samples;

def add_map_to_master(map_to_add, master_map):
    for row_s_i in range(len(map_to_add)):
        row_s = map_to_add[row_s_i];
        for col_s_i in range(len(row_s)):
            master_map[row_s_i][col_s_i] += map_to_add[row_s_i][col_s_i];
    return master_map;

def create_world_map(resolution):
    world_map = [];

    for x in range(resolution[0]):
        world_map.append([]);
        for y in range(resolution[1]):
            world_map[x].append(0);

    return world_map;