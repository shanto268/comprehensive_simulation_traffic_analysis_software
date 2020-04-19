#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 13:07:14 2020
Need to make directory universal
@author: sshanto
#input file strucuture:
    lane, length, total cars, maxSpeed, p_l(HV), p_l(AV), p_s(HV), p_s(AV), v_aa, v_ah, v_h
"""
# change densities 
# change maxspeed
import csv
from simulation.speedLimits import *
from simulation.trafficGenerators import *
import pandas as pd

df = pd.read_csv('/Users/sshanto/techmrt/Python_new/config/input.csv', names=['lane', 'length', 'totcar', 'maxSpeed', 'p_l(HV)', 'p_l(AV)', 'p_s(HV)','p_s(AV)', 'v_aa', 'v_ah', 'v_h'], header=None)

maxFps= 500 #default = 40 , fast = 10, nice = 500
size = width, heigth = 1250, 500
updateFrame = 500 #default = 500, fast = 10 , nice 500
seed = None

lanes = df['lane'][0]
length = df['length'][0]


trafficGenerator = TrafficGenerator(df['totcar'][0]) #density 0.08= 24, 0.2 = 60, 0.6 = 180 , 0.4 = 120    #if 15 then that means increase system density linearly
speedLimits = []

maxSpeed = df['maxSpeed'][0]
maxLength = 1000

print("lane, length, total cars, maxSpeed, p_l(HV), p_l(AV), p_s(HV), p_s(AV), v_aa, v_ah, v_h: ")

print(df['lane'][0], df['length'][0], df['totcar'][0], df['maxSpeed'][0], df['p_l(HV)'][0], df['p_l(AV)'][0], df['p_s(HV)'][0], df['p_s(AV)'][0], df['v_aa'][0], df['v_ah'][0], df['v_h'][0])