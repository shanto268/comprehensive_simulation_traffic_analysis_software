from simulation.speedLimits import *
from simulation.trafficGenerators import * 
import random
import sys

data = ["test_trial.txt", 24, 5, 5, 4, 2, 1, 0.6, 0, 0.4, 7, 50]# low density aware and oppo
maxFps= 40
size = width, heigth = 1280, 720
# in miliseconds
updateFrame = 500

seed = None

lanes = 3
length = 300
maxSpeed = int(data[2])
numCar = int(data[1])
trafficGenerator = TrafficGenerator(numCar)

speedLimits = [ SpeedLimit(((150,0),(300,0)), limit=0, ticks=0), SpeedLimit(((220, 2), (300,2)), limit=0, ticks=0) ]
#trafficGenerator = SimpleTrafficGenerator(2)

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
