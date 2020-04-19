#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 00:10:06 2020

@author: sshanto
"""

import numpy as np
import matplotlib.pyplot as plt

def ana():
    f = open("draft_2/experiment_1/data_files/average_parameters_for_all_cases_combined.txt","r") 
    titles = []
    vals = []
    cases = []
    time = []
    time_t = []
    clsize = []
    clnum = []
    clsize_t = []
    clnum_t = []
    
    for x in f:
        x = x.split(" ")
        y = x[2:5]
        title = "_".join(y)
        val = float(x[-3])
        case = x[-1]
        case = [i for i in case if i != "\n"]
        case = "".join(case)
        if title == "Time_period_of":
            if val != 1199.0 :
                time.append(val)
                time_t.append(case)
        
        if title == "Mean_cluster_size":
                clsize.append(val)
                clsize_t.append(case)
                
        if title == "Number_of_clusters":
                clnum.append(val)
                clnum_t.append(case)
        
        titles.append(title)
        vals.append(val)
        cases.append(case)

    return titles, vals, cases, time, time_t, clsize, clnum, clsize_t, clnum_t
    
sim_type = ana()[2]
param = ana()[0]
param_val = ana()[1]
time = ana()[3]
group = ana()[4]

grp = ana()[7]
clsize = ana()[5]
clnum =ana()[6]

def shrt(q):
    x = []
    for i in q:
        x.append(i[0])
    res = "".join(x)
    return res

def plotter(fig, t, group,key):    
    """
    types = []
    for i in group:
        types.append(shrt(i.split("_")))
    x_coords = [i for i in range(len(t))]
    y_coords = t
   # print(types)
    j = 0
    for i,type in enumerate(types):
        x = x_coords[i]
        y = y_coords[i]
        barlist = plt.bar(x, y, label = type)
       # plt.legend()
        plt.text(x-0.5, y+0.006, type, fontsize=9)
        barlist[0].set_color('r')
        if j%5 == 0:
            barlist[0].set_color('g')
        if j%5 == 1:
            barlist[0].set_color('b')
        if j%5 == 2:
            barlist[0].set_color('k')
        if j%5 == 3:
            barlist[0].set_color('y')
        j+=1
    
    plt.show()
    """
    
    # set width of bar
    barWidth = 0.15

    # set height of bar
    bars1 = [t[0],t[5],t[10]]
    bars2 = [t[1],t[6],t[11]]
    bars3 = [t[2],t[7],t[12]]
    bars4 = [t[3],t[8],t[13]]
    bars5 = [t[4],t[9],t[14]]
    
    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]  
    r5 = [x + barWidth for x in r4]
    
    print(group)
    # Make the plot
    plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='opportunistic')
    plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='neighbor aware')
    plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='oppo and neighbor aware')
    plt.bar(r4, bars4, color='#1B4D03', width=barWidth, edgecolor='white', label='baseline')
    plt.bar(r5, bars5, color='#349B05', width=barWidth, edgecolor='white', label='baseline headway')
    
    # Add xticks on the middle of the group bars
    plt.xlabel('Regime')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['Low Density', 'Critical Density', 'High Density'])
    plt.title("Average Survival "+key+ " for different Models and Regimes")
    plt.ylabel("Average Survival " +key)
    # Create legend & Show graphic
    plt.legend()
    plt.savefig("draft_2/experiment_1/figures/" + fig)
    plt.show()
    
def plotter1(fig, t, group,key):        
    # set width of bar
    barWidth = 0.15

    # set height of bar
    bars1 = [t[0],t[5]]
    bars2 = [t[1],t[6]]
    bars3 = [t[2],t[7]]
    bars4 = [t[3],t[8]]
    bars5 = [t[4],t[9]]
    
    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]  
    r5 = [x + barWidth for x in r4]
    
    print(group)
    # Make the plot
    plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='opportunistic')
    plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='neighbor aware')
    plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='oppo and neighbor aware')
    plt.bar(r4, bars4, color='#1B4D03', width=barWidth, edgecolor='white', label='baseline')
    plt.bar(r5, bars5, color='#349B05', width=barWidth, edgecolor='white', label='baseline headway')
    
    # Add xticks on the middle of the group bars
    plt.xlabel('Regime')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['Low Density', 'Critical Density', 'High Density'])
    plt.title("Average Survival "+key+ " for different Models and Regimes")
    plt.ylabel("Average Survival " +key)
    
    # Create legend & Show graphic
    plt.legend()
    plt.savefig("draft_2/experiment_1/figures/" + fig)
    plt.show()

def ana_clusterability():
    f = open("draft_2/experiment_1/data_files/clusterability.txt","r") 
    titles = []
    clval = []
    for x in f:
        x = x.split(",")
        titles.append(x[0])
        y = float((x[1].split("\n")[0]))
        clval.append(y)
    return titles, clval

tit = ana_clusterability()[0]
c1 = ana_clusterability()[1]

#print(tit)
plotter1("time_report_exp1.png", time, group, "Time")
plotter("cluster_size_report_exp1.png", clsize, grp, "Cluster Size")
plotter("cluster_num_report_exp1.png", clnum, grp, "Cluster Number")
plotter("clusterability_report.png", c1, tit, "Clusterability")



# plot and think about comparing other values for analysis


    