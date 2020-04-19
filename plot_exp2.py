# -*- coding: utf-8 -*-
"""
Experiment 2 plot

Note: remove -1 from clusterability
"""

from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import csv
#from scipy.optimize import curve_fit
#from scipy.optimize import differential_evolution
#import warnings

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])
        
def x_intercept(slope, yi, xi):
    return (slope*xi - yi)/ slope

def histo(a,q3,nn):  # a is array, q3 is a string label for parameter name and nn is nn[0]
    a = list(filter(lambda x: x != 0.0, a)) #array with zero remobed
    b = [[x,a.count(x)] for x in set(a)]
    num = []
    freq = []
    
    for i in b:
        num.append(i[0])
        freq.append(i[1])
    
    alphab = num # x axis 
    alphab = np.round(alphab,2)
    alphab.sort()
    
    sum_freq = 0
    sum_numer = 0
    
    for i in range(len(alphab)):
        sum_freq += freq[i]
        sum_numer += (alphab[i]*freq[i])
    
    if sum_freq == 0:
        w_mean = 0
    else:
        w_mean = ( sum_numer / sum_freq )
        
    print("Average of " + str(q3) + " is "  + str(w_mean) + " for " + str(nn) + "\n")
    

def plot1(fname):
        fn = fname
        new_nn = fname.split('/')
        fn = new_nn[3]
        nn = fn.split('.')

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
        totlane = []
        avlane = []
        rvlane = []
        carclus = []
        
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
                totlane.append(float(row[10]))
                avlane.append(float(row[11]))
                rvlane.append(float(row[12]))
                carclus.append(float(row[13]))
                
        FD_arr = []
        params = []  #fd, fdrv, fdav
        FD_RV_arr = []
        FD_AV_arr = []
        
        dens = density[::99]
        totlane_dens = totlane[::99]
        avlane_dens = avlane[::99]
        rvlane_dens = rvlane[::99]
        totlane_dens = [totlane_dens[0]] + [totlane_dens[i+1] - totlane_dens[i] for i in range(len(totlane_dens)-1)]
        avlane_dens = [avlane_dens[0]] + [avlane_dens[i+1] - avlane_dens[i] for i in range(len(avlane_dens)-1)]
        rvlane_dens = [rvlane_dens[0]] + [rvlane_dens[i+1] - rvlane_dens[i] for i in range(len(rvlane_dens)-1)]
        PAV = prob[::99]
        delPAV = [0] + [prob[i+1]-prob[i] for i in range(len(PAV)-1)]
        
        plt.scatter(dens, delPAV)
        plt.plot(dens, delPAV)
        plt.title("Change in P(AV-AV)")
        plt.ylabel("Del P(AV-AV)")
        plt.xlabel("System Density")
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/del_p(av)_all_"+str(nn[0])+".png")
        plt.show()
        
    #    print("av: " + str(avlane_dens))
    #    print("rv: " + str(rvlane_dens))
   #     print("\n\n")
        densityrv_ = densityrv[::99]
        densityav_ = densityav[::99]
        numrv = [round(300*i) for i in densityrv_]
        numav = [round(300*i) for i in densityav_] 
        
   #     print("numav: " + str(numav))
   #     print("numrv: " + str(numrv))
   #     print("\n\n")
        
        for i in range(len(avlane_dens)):
            avlane_dens[i] = avlane_dens[i] / numav[i] 
            rvlane_dens[i] = rvlane_dens[i] / numrv[i] 
            totlane_dens[i] = totlane_dens[i] / (numrv[i] + numav[i] )
      #  print("total: " + str(totlane_dens))
    #    print("av: " + str(avlane_dens))
   #     print("rv: " + str(rvlane_dens))
            
        cum_clnum = []
        cum_i = 0
        for i in clnum:
            cum_i += i
            cum_clnum.append(cum_i)
            
        carclus = list(filter(lambda a: a != -1, carclus))
        
        a = avgclsize
        tcls = []
        index = []
        t = 0
        for i in range(len(a)):
            if a[i] != 0:
                index.append(i)
        t = 0
        for i in range(len(index)-1):
            j = i + 1
            if j <= len(index):
                if (index[j] - index[i]) == 1:
                    t += 1
                    if j == len(index) - 1:
                        tcls.append(t)
                else:
                    tcls.append(t)
                    t = 0
        histo(tcls, "Time period of clusters", nn[0])
        
        
        plt.plot(updates, totlane, 'black', label='Total')
        plt.plot(updates, avlane, 'red', label='AV')
        plt.plot(updates, rvlane, 'blue', label='RV')
        plt.xlabel("Timesteps")
        plt.ylabel("Total Number of Lane Changes")
        plt.title("Number of Lane Changes over time")
        plt.ylim(0,10000)
        plt.legend()
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/total_number_of_lane_changes_all_"+str(nn[0])+".png")
        plt.show()
        
        plt.plot(updates, avlane)
        plt.xlabel("Timesteps")
        plt.ylabel("Total Number of Lane Changes by AV")
        plt.title("Number of Lane Changes (AV) over time")
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/total_number_lane_changes_av_"+str(nn[0])+".png")
        plt.show()
        
        plt.plot(updates, rvlane)
        plt.xlabel("Timesteps")
        plt.ylabel("Total Number of Lane Changes by HV")
        plt.title("Number of Lane Changes (HV) over time")
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/total_number_lane_changes_hv_"+str(nn[0])+".png")
        plt.show()
        
        plt.bar([i for i in range(len(carclus))], carclus)
     #   plt.plot([i for i in range(len(carclus))], smooth(carclus,500), 'r-', lw=1)
        plt.xlabel("Timesteps")
        plt.ylabel("Ratio")
        plt.title("Clusterability")
      #  plt.ylim(0,0.4)
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/clusterability_"+str(nn[0])+".png")
        plt.show()
        
        
        ####
        plt.scatter(dens, totlane_dens, label='Total')
        plt.scatter(dens, avlane_dens, label='AV')
        plt.scatter(dens, rvlane_dens, label='RV')
        plt.plot(dens, totlane_dens)
        plt.plot(dens, avlane_dens)
        plt.plot(dens, rvlane_dens)
        plt.xlabel("System Density")
        plt.ylabel("Lane Change Rate")
        plt.ylim(0,30)
        plt.title("Lane Change Rate")
        plt.legend()
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/lane_change_rate_all_"+str(nn[0])+".png")
        plt.show()
        
        plt.scatter(dens, avlane_dens, color='orange')
        plt.plot(dens, avlane_dens, 'orange')
        plt.xlabel("System Density")
        plt.ylabel("Lane Change Rate of AVs")
        plt.title("Lane Change Rate (AV)")
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/lane_change_rate_av_"+str(nn[0])+".png")
        plt.show()
        
        plt.scatter(dens, rvlane_dens, color='green')
        plt.plot(dens, rvlane_dens, 'green')
        plt.xlabel("System Density")
        plt.ylabel("Lane Change Rate of HVs")
        plt.title("Lane Change Rate (HV)")
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/lane_change_rate_hv_"+str(nn[0])+".png")
        plt.show()
        
        ###
        
        plt.bar(updates, cum_clnum )
        plt.xlabel("Timesteps")
        plt.ylabel("Total Number of Clusters")
        plt.title("Number of Clusters over time")
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/total_cluster_num_"+str(nn[0])+".png")
        plt.show()
        
        plt.plot(updates, prob)
        plt.xlabel("Timesteps")
        plt.ylabel("Proportion of AV-AV headways")
        plt.title("Probability of AV-AV headways")
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/p_av_av_"+str(nn[0])+".png")
        plt.show()
        
        plt.bar(updates, clnum)
        plt.xlabel("Timesteps")
        plt.ylabel("Number of Clusters")
        plt.title("Number of Clusters over time")
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/cluster_num_per_time_step_"+str(nn[0])+".png")
        plt.show()
        
        plt.bar(updates, avgclsize)
        plt.xlabel("Timesteps")
        plt.ylabel("Average Size of Clusters")
        plt.title("Average Size of Clusters over time")
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/cluster_size_per_time_step_"+str(nn[0])+".png")
        plt.show()
        
        plt.scatter(densityrv, flowrv, s= 1)
        plt.xlabel("HV density")
        plt.ylabel("HV flow")
        plt.xlim(0,0.75)
        plt.ylim(0,0.45)
        plt.title("Fundamental Diagram: HV")  
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/fd_hv_data_"+str(nn[0])+".png")
        plt.show()
        
        plt.scatter(densityav, flowav, s= 1)
        plt.xlabel("AV density")
        plt.ylabel("AV flow")
        plt.xlim(0,0.35)
        plt.ylim(0, 0.25)
        plt.title("Fundamental Diagram: AV") 
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/fd_av_data_"+str(nn[0])+".png")
        plt.show()
        
        
        plt.scatter(density, flow, s= 1)
        plt.xlabel("density")
        plt.ylabel("flow")
        plt.title("Fundamental Diagram") 
        plt.xlim(0,1)
        plt.ylim(0, 0.6)
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/fd_all_data"+str(nn[0])+".png")
        plt.show()
        
        flow_max_index = flow.index(max(flow))
        flowrv_max_index = flowrv.index(max(flowrv))
        flowav_max_index = flowav.index(max(flowav))
        
        x = density
        y =flow
        N= 3000
        
        p0 = [np.mean(x), np.mean(y), 1, 1]
                    #weighing functions:            
                    
        y_weight = np.empty(len(y))
        y_weight.fill(10)
        y_weight[0] = y_weight[-5:-1] = 0.1
        y_weight[flow_max_index] = 0.2
        
        
        p , e = optimize.curve_fit(piecewise_linear, x, y, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
        perr = np.sqrt(np.diag(e))
        xd = np.linspace(0, 1, N)
        
        x0, y0, k1, k2 = p
                                                                                #function and coefficients
        y_crit = y0 #max flow
        x_crit = x0 #critical density
        x_jam = max(xd) #jam density
        x_jam = min(x_intercept(k2, y0, x0),1)                                  #NEED TO RETURN THIS
        free_y = k1   #slope 1
        wave_v = k2    #slope 2
        

        plt.plot(xd, piecewise_linear(xd, *p), 'orange', label = 'fit')             #NEED TO RETURN THIS
        plt.scatter(x,y,color = 'mediumblue', s=3, marker = ".", label = 'data')
        plt.legend()
        plt.xlabel('density')
        plt.ylabel('flow')
        plt.title('Fundamental diagram: ')
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/fd_fit_and_data_"+str(nn[0])+".png")
        plt.show()
        
        #print("[x_critical  y_max  free_flow_v  wave_speed]")
        #print(p)                                                                                    #NEED TO RETURN THIS
        #print("jam density: " + str(x_jam))        
        
        plt.plot(xd, piecewise_linear(xd, *p), 'orange')   
        plt.xlabel('density')
        plt.ylabel('flow')
        plt.title('Fundamental diagram: ')
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/fd_fit_only_"+str(nn[0])+".png")
        plt.show()
        FD_arr.append(xd)
        FD_arr.append( piecewise_linear(xd, *p)) 
        
        """
      #  plt.plot(lan, updates)
      #  plt.xlabel('time steps')
      #  plt.ylabel('Number of lane changes to test lane')
      #  plt.savefig("/lane"+str(nn[0])+".png")
      #  plt.show()
        """
        
        xrv = densityrv
        yrv= flowrv        
        
        y_weight = np.empty(len(yrv))
        y_weight.fill(10)
        y_weight[0] = y_weight[-5:-1] = 0.1
      #  y_weight[flowrv_max_index] = 0.2
        
        p0 = [np.mean(xrv), np.mean(yrv), 1, 1]
        prv , e = optimize.curve_fit(piecewise_linear, xrv, yrv, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
        perr = np.sqrt(np.diag(e))
        #xdrv = np.linspace(0, max(xrv), 3000)
        xdrv = np.linspace(0, 1, 3000)
        
        plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'orange')     #need to return this
        plt.xlabel('HV density')
        plt.ylabel('HV flow')
        plt.gca().set_xlim([0,max(densityrv)+0.05])
        plt.gca().set_ylim([0, max(flowrv) + 0.05])
        plt.title('HV Fundamental diagram: ')
       # plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/fd_hv_fit_"+str(nn[0])+".png")
        plt.show()
        
        FD_RV_arr.append(xdrv)
        FD_RV_arr.append( piecewise_linear(xdrv, *prv))

        xav = densityav
        yav= flowav        
        
        y_weight = np.empty(len(yav))
        y_weight.fill(10)
       # y_weight[0] = y_weight[-5:-1] = 0.1 #works for model 1
        y_weight[0] =  0.1
      #  y_weight[int(len(yav) - 1)] = 0.1  #worked for r1m1
        y_weight[0] = y_weight[-5:-1] = 0.01
        y_weight[flowav_max_index] = 0.01
        
        p0 = [np.mean(xav), np.mean(yav), 1, 1] 
        pav , e = optimize.curve_fit(piecewise_linear, xav, yav, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
        perr = np.sqrt(np.diag(e))
        #xdav = np.linspace(0, max(xav), 3000)
        xdav = np.linspace(0, 1, 3000)
        
        plt.plot(xdav, piecewise_linear(xdav, *pav), 'orange')     #need to return this
        plt.xlabel('AV density')
        plt.ylabel('AV flow')
        plt.gca().set_xlim([0,max(densityav)+0.05])
        plt.gca().set_ylim([0, max(flowav) + 0.05])
        plt.title('AV Fundamental diagram: ')
      #  plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/fd_av_fit_"+str(nn[0])+".png")
        plt.show()
    
        FD_AV_arr.append(xdav)
        FD_AV_arr.append( piecewise_linear(xdav, *pav))
        
        params.append(p)
        params.append(prv)
        params.append(pav)
        
        plt.plot(xdav, piecewise_linear(xdav, *pav), 'orange', label='AV')  
        plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'green', label='RV')  
        plt.plot(xd, piecewise_linear(xd, *p), 'blue', label='Overall')  
        plt.ylim(0, 0.65)
        plt.xlim(0,1)
        plt.legend()
        plt.title('Fundamental diagram: ')
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/fd_av_hv_fit_"+str(nn[0])+".png")
        plt.show()
        
        plt.scatter(density, flow, c='r', s=1, marker = "x", label='Overall')  
        plt.scatter(densityrv, flowrv, c='b', s=1, marker = "o", label='HV')  
        plt.scatter(densityav, flowav, c='g', s=1, marker = ".", label='AV')  
        plt.ylim(0, 0.65)
        plt.xlim(0,1)
        plt.legend(loc='upper right')
        plt.title('Fundamental diagram: ')
        plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/fd_av_hv_data"+str(nn[0])+".png")
        plt.show()
        
        return FD_arr, FD_RV_arr, FD_AV_arr, params
        
        
namea = "draft_2/experiment_2/data_files/fd_oppo.txt"
nameb = "draft_2/experiment_2/data_files/fd_aware.txt"
nameba = "draft_2/experiment_2/data_files/fd_aware_oppo.txt"
namec = "draft_2/experiment_2/data_files/fd_base_hvlike.txt"
nameca = "draft_2/experiment_2/data_files/fd_base_hway.txt"


plot1(namea)

#plot_all = [namea, nameb, nameba, namec, nameca]
#for i in plot_all:
#    plot1(i)


"""

def plot2(arr1, arr2, arr3):
    d1 = arr1[0][0]
    d2 = arr2[0][0]
    d3 = arr3[0][0]
    
    q1 = arr1[0][1] 
    q2 = arr2[0][1] 
    q3 = arr3[0][1] 
    
    drv1 = arr1[1][0]
    drv2 = arr2[1][0] 
    drv3 = arr3[1][0]
    
    qrv1 = arr1[1][1]
    qrv2 = arr2[1][1] 
    qrv3 = arr3[1][1]
    
    
    dav1 = arr1[2][0] 
    dav2 = arr2[2][0]  
    dav3 = arr3[2][0]  
    
    qav1 = arr1[2][1]
    qav2 = arr2[2][1]
    qav3 = arr3[2][1]
    
    
    
    l1 = np.diff(arr1[4])
    l2 = np.diff(arr2[4])
    l3 = np.diff(arr3[4])
    
    plt.plot(d1, q1, 'r:' ,label = "aware")
    plt.plot( d2, q2, 'y' ,label = "unaware")
    plt.plot(d3, q3, 'b:' ,label = "control")
    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Fundamental diagram: ')
    plt.savefig("draft_2/experiment_2/figures/tricomp.png")
    plt.show()
    
    #plt.plot(drv1, qrv1, label = "aware", drv2, qrv2, label = "aware",drv3, qrv3, label = "control",drv4, qrv4, label = "R2M2")
    plt.plot(drv1, qrv1, 'r:' ,label = "aware")
    plt.plot( drv2, qrv2, 'y' ,label = "unaware")
    plt.plot(drv3, qrv3, 'b:' ,label = "control")
    plt.ylim(0, 0.7)
    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Fundamental diagram: RV')
    plt.savefig("draft_2/experiment_2/figures/tricomprv.png")
    plt.show()
    
  #  plt.plot(dav1, qav1, label = "aware", dav2, qav2, label = "unaware",dav3, qav3, label = "control",dav4, qav4, label = "R2M2")
    plt.plot(dav1, qav1, 'r:' ,label = "aware")
    plt.plot( dav2, qav2, 'y' ,label = "unaware")
    plt.plot(dav3, qav3, 'b:' ,label = "control")
    plt.ylim(0, 0.7)
    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Fundamental diagram: AV')
    plt.savefig("draft_2/experiment_2/figures/tricompav.png")
    plt.show()
            
    
plot2(m1, m2, m3)    
plot2(m4, m5, m6)    
plot2(m7, m8, m9)    



"""
