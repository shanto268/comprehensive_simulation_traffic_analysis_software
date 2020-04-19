# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:13:32 2019

@author: Owner
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
    plt.savefig("final/"+"/tricomp.png")
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
    plt.savefig("final/"+"/tricomprv.png")
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
    plt.savefig("final/"+"/tricompav.png")    
    plt.show()
    
    plt.plot(range(len(l1)), l1  ,label = "aware") 
    plt.plot(range(len(l2)), l2  ,label = "unaware")
    plt.plot(range(len(l3)), l3 ,label = "control")
    plt.xlabel('time steps')
    plt.legend()
    plt.ylabel('Number of lane changes to test lane')
    plt.savefig("final/"+"/lanecomprv.png")    
    plt.show()
    
        
    
plot2(r1m1, r1m2, r2m1)    
