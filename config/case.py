# change densities 
# change maxspeed
import simulation.road, simulation.speedLimits
import random
import sys
from simulation.speedLimits import *
from simulation.trafficGenerators import *

#sim data
#data = ["trial.txt",50,5,3,3,3,0.8,0.8,0.4,0.4,1,10]    
data = ["test_trial.txt", 24, 5, 5, 4, 2, 1, 0.6, 0, 0.4, 7, 50]# low density aware and oppo


#constants
maxFps= 2000 #default = 40 , fast = 10, nice = 500
size = width, heigth = 1250, 500
updateFrame = 2000 #default = 500, fast = 10 , nice 500
seed = None
lanes = 3
length = 100
maxSpeed = int(data[2])
numCar = int(data[1])
trafficGenerator = TrafficGenerator(numCar) #density 0.08= 24, 0.2 = 60, 0.6 = 180 , 0.4 = 120    #if 15 then that means increase system density linearly

speedLimits = []
#speedbreaker
#speedLimits = [ SpeedLimit( ((0,2), (99,2)), limit=2, ticks=60) ]

#printing onto console
def printData():
    print("\n")
    print("The input parameters are: \n")
    names = ["Output file name: ","Total Number of cars: ", "Maximum speed on road: ", "Maximum AV-AV speed: ", "Maximum AV-HV speed: ", "Maximum HV speed: ", "Probability of lane change of AV: ", "Probability of lane change of HV: ", "Probability of braking of AV: ", "Probability of braking of HV: ", "Number of AVs: ","Simulation Terminates at (cycles): "]
    for i in range(len(data)):
        print(str(names[i]) + str(data[i]))
    if seed == None:
        print("No random seed")
    else:
        print("Random seed is fixed at ", seed)
    print("\n\n")

printData()
