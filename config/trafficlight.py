import random
from simulation.speedLimits import *
from simulation.trafficGenerators import * 
import pygame
import sys

data = ["test_trial.txt", 24, 5, 5, 4, 2, 1, 0.6, 0, 0.4, 7, 50]# low density aware and oppo

maxFps= 40
size = width, heigth = 500 , 800
# in miliseconds
updateFrame = 500

seed = None

lanes = 3
length = 100
maxSpeed = int(data[2])
numCar = int(data[1])
maxLength = 1000


speedLimits = [SpeedLimit(range=((6, 0), (6,2)), limit=0, ticks=30)]
trafficGenerator = TrafficGenerator(numCar)


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

'''
#while #get loop with updates such that it changes value every update
for i in range(0,1000):
    w = random.randint(1,10)
    print (w)
    if w > 5: #determines degree of mixed flow
        slowDownProbability, laneChangeProbability = 0.3, 0.4
        print(slowDownProbability)
        print(laneChangeProbability)#case: RV
    else:
        slowDownProbability, laneChangeProbability = 0, 0 #case: AV
        print(slowDownProbability)
        print(laneChangeProbability)



slowDownProbability, laneChangeProbability = None, None
w = random.randint(1,10)
print (w)
if w > 5: #determines degree of mixed flow
    slowDownProbability, laneChangeProbability = 0.3, 0.4#case: RV
else:
     slowDownProbability, laneChangeProbability = 0, 0 #case: AV
'''
