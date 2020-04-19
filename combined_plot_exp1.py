0# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:13:31 2019

@author: Owner
"""

from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import csv
import scipy, matplotlib
import pandas as pd

def data(fname):
    density = []
    flow = []
    updates = []
    densityrv = []
    flowrv = []
    densityav = []
    flowav = []
    clnum = []
    avgclsize = []
    prob = []

    with open(fname,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            density.append(float(row[0]))
            flow.append(float(row[1]))
            updates.append(float(row[2]))
            densityrv.append(float(row[3]))
            flowrv.append(float(row[4]))
            densityav.append(float(row[5]))
            flowav.append(float(row[6]))
            clnum.append(float(row[7]))
            avgclsize.append(float(row[8]))
            prob.append(float(row[9]))

    d =density[0]

    cum_clnum = []
    cum_i = 0
    for i in clnum:
            cum_i += i
            cum_clnum.append(cum_i)


    max_flow = max(flow)
    max_flowav = max(flowav)
    max_flowrv = max(flowrv)

    min_flow = min(flow)
    min_flowav = min(flowav)
    min_flowrv = min(flowrv)

    ave_flow = sum(flow) / len(flow)
    ave_flowav = sum(flowav) / len(flowav)
    ave_flowrv = sum(flowrv) / len(flowrv)

    return (d, max_flow, max_flowav, max_flowrv, min_flow, min_flowav, min_flowrv, ave_flow, ave_flowav, ave_flowrv, density, flow, updates, cum_clnum)

def plotter(f1,f2,f3,f4,f5,f6,f7,f8,f9): #f4 represents density string
    d1 = data(f1)
    d2 = data(f2)
    d3 = data(f3)
    d4 = data(f4)
    d5 = data(f5)
    d6 = data(f6)
    d7 = data(f7)
    d8 = data(f8)
    d9 = data(f9)


    dd1 = d1[0]

    max_flow1 = d1[1]
    max_flowav1 = d1[2]
    max_flowrv1 = d1[3]
    min_flow1 = d1[4]
    min_flowav1 = d1[5]
    min_flowrv1 = d1[6]
    ave_flow1 = d1[7]
    ave_flowav1 = d1[8]
    ave_flowrv1 = d1[9]
    updates1 = d1[10]
    cclnum1 = d1[11]

    max_flow2 = d2[1]
    max_flowav2 = d2[2]
    max_flowrv2 = d2[3]
    min_flow2 = d2[4]
    min_flowav2 = d2[5]
    min_flowrv2 = d2[6]
    ave_flow2 = d2[7]
    ave_flowav2 = d2[8]
    ave_flowrv2 = d2[9]
    updates2 = d2[10]
    cclnum2 = d1[11]


    max_flow3 = d3[1]
    max_flowav3 = d3[2]
    max_flowrv3 = d3[3]
    min_flow3 = d3[4]
    min_flowav3 = d3[5]
    min_flowrv3 = d3[6]
    ave_flow3 = d3[7]
    ave_flowav3 = d3[8]
    ave_flowrv3 = d3[9]
    updates3 = d3[10]
    cclnum3 = d1[11]


    dd2 = d4[0]

    max_flow4 = d4[1]
    max_flowav4 = d4[2]
    max_flowrv4 = d4[3]
    min_flow4 = d4[4]
    min_flowav4 = d4[5]
    min_flowrv4 = d4[6]
    ave_flow4 = d4[7]
    ave_flowav4 = d4[8]
    ave_flowrv4 = d4[9]
    updates4 = d4[10]
    cclnum4 = d1[11]

    max_flow5 = d5[1]
    max_flowav5 = d5[2]
    max_flowrv5 = d5[3]
    min_flow5 = d5[4]
    min_flowav5 = d5[5]
    min_flowrv5 = d5[6]
    ave_flow5 = d5[7]
    ave_flowav5 = d5[8]
    ave_flowrv5 = d5[9]
    updates5 = d5[10]
    cclnum5 = d1[11]



    max_flow6 = d6[1]
    max_flowav6 = d6[2]
    max_flowrv6 = d6[3]
    min_flow6 = d6[4]
    min_flowav6 = d6[5]
    min_flowrv6 = d6[6]
    ave_flow6 = d6[7]
    ave_flowav6 = d6[8]
    ave_flowrv6 = d6[9]
    updates6 = d6[10]
    cclnum6 = d1[11]

    dd3 = d7[0]

    max_flow7 = d7[1]
    max_flowav7 = d7[2]
    max_flowrv7 = d7[3]
    min_flow7 = d7[4]
    min_flowav7 = d7[5]
    min_flowrv7 = d7[6]
    ave_flow7 = d7[7]
    ave_flowav7 = d7[8]
    ave_flowrv7 = d7[9]
    updates7 = d7[10]
    cclnum7 = d1[11]


    max_flow8 = d8[1]
    max_flowav8 = d8[2]
    max_flowrv8 = d8[3]
    min_flow8 = d8[4]
    min_flowav8 = d8[5]
    min_flowrv8 = d8[6]
    ave_flow8 = d8[7]
    ave_flowav8 = d8[8]
    ave_flowrv8 = d8[9]
    updates8 = d8[10]
    cclnum8 = d1[11]

    max_flow9 = d9[1]
    max_flowav9 = d9[2]
    max_flowrv9 = d9[3]
    min_flow9 = d9[4]
    min_flowav9 = d9[5]
    min_flowrv9 = d9[6]
    ave_flow9 = d9[7]
    ave_flowav9 = d9[8]
    ave_flowrv9 = d9[9]
    updates9 = d9[10]
    cclnum9 = d1[11]

#***************************************************    FD  OVERALL *****************************************************************
    plt.scatter(dd1, ave_flow1 ,label = "low opportunistic")
    plt.scatter(dd1, ave_flow2 ,label = "low aware")
    plt.scatter(dd1, ave_flow3 ,label = "low base case")

    plt.scatter(dd2, ave_flow4 ,label = "crit opportunistic")
    plt.scatter(dd2, ave_flow5 ,label = "crit aware")
    plt.scatter(dd2, ave_flow6 ,label = "crit base case")

    plt.scatter(dd3, ave_flow7 ,label = "high opportunistic")
    plt.scatter(dd3, ave_flow8 ,label = "high aware")
    plt.scatter(dd3, ave_flow9 ,label = "high base case")

    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Average Fundamental diagram: ')
    plt.savefig("draft_2/experiment_1/figures/combined_aveflow.png")
    plt.show()


    plt.scatter(dd1, max_flow1 ,label = "low opportunistic")
    plt.scatter(dd1, max_flow2 ,label = "low aware")
    plt.scatter(dd1, max_flow3 ,label = "low base case")

    plt.scatter(dd2, max_flow4 ,label = "crit opportunistic")
    plt.scatter(dd2, max_flow5 ,label = "crit aware")
    plt.scatter(dd2, max_flow6 ,label = "crit base case")

    plt.scatter(dd3, max_flow7 ,label = "high opportunistic")
    plt.scatter(dd3, max_flow8 ,label = "high aware")
    plt.scatter(dd3, max_flow9 ,label = "high base case")

    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Maximum Fundamental diagram: ')
    plt.savefig("draft_2/experiment_1/figures/combined_maxflow.png")
    plt.show()

    plt.scatter(dd1, min_flow1 ,label = "low opportunistic")
    plt.scatter(dd1, min_flow2 ,label = "low aware")
    plt.scatter(dd1, min_flow3 ,label = "low base case")

    plt.scatter(dd2, min_flow4 ,label = "crit opportunistic")
    plt.scatter(dd2, min_flow5 ,label = "crit aware")
    plt.scatter(dd2, min_flow6 ,label = "crit base case")

    plt.scatter(dd3, min_flow7 ,label = "high opportunistic")
    plt.scatter(dd3, min_flow8 ,label = "high aware")
    plt.scatter(dd3, min_flow9 ,label = "high base case")

    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Minimum Fundamental diagram: ')
    plt.savefig("draft_2/experiment_1/figures/combined_minflow.png")
    plt.show()

#***************************************************   AV FD  COMBINED *****************************************************************
    plt.scatter(dd1, ave_flowav1 ,label = "low opportunistic")
    plt.scatter(dd1, ave_flowav2 ,label = "low aware")
    plt.scatter(dd1, ave_flowav3 ,label = "low base case")

    plt.scatter(dd2, ave_flowav4 ,label = "crit opportunistic")
    plt.scatter(dd2, ave_flowav5 ,label = "crit aware")
    plt.scatter(dd2, ave_flowav6 ,label = "crit base case")

    plt.scatter(dd3, ave_flowav7 ,label = "high opportunistic")
    plt.scatter(dd3, ave_flowav8 ,label = "high aware")
    plt.scatter(dd3, ave_flowav9 ,label = "high base case")

    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Average AV Fundamental diagram: ')
    plt.savefig("draft_2/experiment_1/figures/combined_av_aveflow.png")
    plt.show()


    plt.scatter(dd1, max_flowav1 ,label = "low opportunistic")
    plt.scatter(dd1, max_flowav2 ,label = "low aware")
    plt.scatter(dd1, max_flowav3 ,label = "low base case")

    plt.scatter(dd2, max_flowav4 ,label = "crit opportunistic")
    plt.scatter(dd2, max_flowav5 ,label = "crit aware")
    plt.scatter(dd2, max_flowav6 ,label = "crit base case")

    plt.scatter(dd3, max_flowav7 ,label = "high opportunistic")
    plt.scatter(dd3, max_flowav8 ,label = "high aware")
    plt.scatter(dd3, max_flowav9 ,label = "high base case")

    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Maximum AV Fundamental diagram: ')
    plt.savefig("draft_2/experiment_1/figures/combined_av_maxflowav.png")
    plt.show()

    plt.scatter(dd1, min_flowav1 ,label = "low opportunistic")
    plt.scatter(dd1, min_flowav2 ,label = "low aware")
    plt.scatter(dd1, min_flowav3 ,label = "low base case")

    plt.scatter(dd2, min_flowav4 ,label = "crit opportunistic")
    plt.scatter(dd2, min_flowav5 ,label = "crit aware")
    plt.scatter(dd2, min_flowav6 ,label = "crit base case")

    plt.scatter(dd3, min_flowav7 ,label = "high opportunistic")
    plt.scatter(dd3, min_flowav8 ,label = "high aware")
    plt.scatter(dd3, min_flowav9 ,label = "high base case")

    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Minimum AV Fundamental diagram: ')
    plt.savefig("draft_2/experiment_1/figures/combined_av_minflow.png")
    plt.show()



#********************************************************* RV FD COMBINED *****************************************************************

    plt.scatter(dd1, ave_flowrv1 ,label = "low opportunistic")
    plt.scatter(dd1, ave_flowrv2 ,label = "low aware")
    plt.scatter(dd1, ave_flowrv3 ,label = "low base case")

    plt.scatter(dd2, ave_flowrv4 ,label = "crit opportunistic")
    plt.scatter(dd2, ave_flowrv5 ,label = "crit aware")
    plt.scatter(dd2, ave_flowrv6 ,label = "crit base case")

    plt.scatter(dd3, ave_flowrv7 ,label = "high opportunistic")
    plt.scatter(dd3, ave_flowrv8 ,label = "high aware")
    plt.scatter(dd3, ave_flowrv9 ,label = "high base case")

    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Average RV Fundamental diagram: ')
    plt.savefig("draft_2/experiment_1/figures/combined_rv_aveflow.png")
    plt.show()


    plt.scatter(dd1, max_flowrv1 ,label = "low opportunistic")
    plt.scatter(dd1, max_flowrv2 ,label = "low aware")
    plt.scatter(dd1, max_flowrv3 ,label = "low base case")

    plt.scatter(dd2, max_flowrv4 ,label = "crit opportunistic")
    plt.scatter(dd2, max_flowrv5 ,label = "crit aware")
    plt.scatter(dd2, max_flowrv6 ,label = "crit base case")

    plt.scatter(dd3, max_flowrv7 ,label = "high opportunistic")
    plt.scatter(dd3, max_flowrv8 ,label = "high aware")
    plt.scatter(dd3, max_flowrv9 ,label = "high base case")

    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Maximum RV Fundamental diagram: ')
    plt.savefig("draft_2/experiment_1/figures/combined_rv_maxflowrv.png")
    plt.show()

    plt.scatter(dd1, min_flowrv1 ,label = "low opportunistic")
    plt.scatter(dd1, min_flowrv2 ,label = "low aware")
    plt.scatter(dd1, min_flowrv3 ,label = "low base case")

    plt.scatter(dd2, min_flowrv4 ,label = "crit opportunistic")
    plt.scatter(dd2, min_flowrv5 ,label = "crit aware")
    plt.scatter(dd2, min_flowrv6 ,label = "crit base case")

    plt.scatter(dd3, min_flowrv7 ,label = "high opportunistic")
    plt.scatter(dd3, min_flowrv8 ,label = "high aware")
    plt.scatter(dd3, min_flowrv9 ,label = "high base case")

    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Minimum RV Fundamental diagram: ')
    plt.savefig("draft_2/experiment_1/figures/combined_rv_minflow.png")
    plt.show()

#********************************************* CLUSTER NUMBER ANALYSIS ********************************************************8

#    update = [updates1, updates2, updates3, updates4, updates5, updates6, updates7, updates8, updates9 ]
"""    updates = np.linspace(0,1200,1209)

    plt.plot(updates, cclnum1, label = "low opportunistic")
    plt.plot(updates, cclnum2, label = "low aware")
    plt.plot(updates, cclnum3, label = "low base case")


    plt.plot(updates, cclnum4, label = "low opportunistic")
    plt.plot(updates, cclnum5, label = "high aware")
    plt.plot(updates, cclnum6, label = "low base case")


    plt.plot(updates, cclnum7, label = "high opportunistic")
    plt.plot(updates, cclnum8, label = "high aware")
    plt.plot(updates, cclnum9, label = "low base case")

    plt.legend()
    plt.xlabel('Total number of clusters')
    plt.ylabel('Timesteps')
    plt.title('Number of Clusters')
  #  plt.savefig("draft_2/experiment_1/figures/combined_rv_minflow.png")
    plt.show()
"""
def plot_all():
        name1 = "draft_2/experiment_1/data_files/low_density_oppo.txt"
        name2 = "draft_2/experiment_1/data_files/low_density_aware.txt"
        name2a = "draft_2/experiment_1/data_files/low_density_aware_oppo.txt"
        name3 = "draft_2/experiment_1/data_files/low_density_base_hv_like.txt"
        name3a = "draft_2/experiment_1/data_files/low_density_base_hv_hway.txt"
             
        name4 = "draft_2/experiment_1/data_files/crit_density_oppo.txt"
        name5 = "draft_2/experiment_1/data_files/crit_density_aware.txt"
        name5a = "draft_2/experiment_1/data_files/crit_density_aware_oppo.txt"
        name6 = "draft_2/experiment_1/data_files/crit_density_base_hv_like.txt"
        name6a = "draft_2/experiment_1/data_files/crit_density_base_hv_hway.txt"
             
        name7 = "draft_2/experiment_1/data_files/high_density_oppo.txt"
        name8 = "draft_2/experiment_1/data_files/high_density_aware.txt"
        name8a = "draft_2/experiment_1/data_files/high_density_aware_oppo.txt"
        name9 = "draft_2/experiment_1/data_files/high_density_base_hv_like.txt"
        name9a = "draft_2/experiment_1/data_files/high_density_base_hv_hway.txt"
             
        namei = "draft_2/experiment_1/data_files/mid_density_oppo.txt"
        nameii = "draft_2/experiment_1/data_files/mid_density_aware.txt"
        nameii = "draft_2/experiment_1/data_files/mid_density_aware_oppo.txt"
        nameiii = "draft_2/experiment_1/data_files/mid_density_base_hv_like.txt"
        nameiiia = "draft_2/experiment_1/data_files/mid_density_base_hv_hway.txt"

        plotter(name1,name2,name3,name4,name5,name6,name7,name8,name9)

plot_all()
