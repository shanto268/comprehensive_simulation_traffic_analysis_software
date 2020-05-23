import simulation.road, simulation.speedLimits
import random
import sys
from simulation.speedLimits import *
from simulation.trafficGenerators import *

#sim data
#data = ["trial.txt",50,5,3,3,3,0.8,0.8,0.4,0.4,1,10]
data = ["test_trial.txt", 24, 5, 5, 4, 3, 1, 0.6, 0, 0.4, 7, 20]# low density aware and oppo

maxFps= 40
size = width, heigth = 1250, 500
# in miliseconds
updateFrame = 500

seed = None
lanes = 3
length = 100

numCar = int(data[1])
trafficGenerator = TrafficGenerator(numCar) #density 0.08= 24, 0.2 = 60, 0.6 = 180 , 0.4 = 120    #if 15 then that means increase system density linearly
#trafficGenerator = SimpleTrafficGenerator(2)
maxSpeed = int(data[2])

#maxLength = 1000
"""
speedLimits = [
        SpeedLimit(((70, 0), (130, lanes-1)), limit=3, ticks=0),
        SpeedLimit(((200, 0), (260, 0)), limit=0, ticks=0),
        SpeedLimit(((200, 2), (260, 2)), limit=0, ticks=0)
        ]
"""

speedLimits = [ SpeedLimit(((0,0),(100,0)), limit=0, ticks=20)]

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

