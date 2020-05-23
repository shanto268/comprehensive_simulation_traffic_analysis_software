import random
from simulation.speedLimits import *
from simulation.trafficGenerators import * 
import pygame

maxFps= 40
size = width, heigth = 500 , 800
# in miliseconds
updateFrame = 500

seed = None

lanes = 2
length = 100

maxSpeed = 5
maxLength = 1000


#speedLimits = [SpeedLimit(range=((82, 0), (82,2)), limit=0, ticks=30)]
speedLimits = []
trafficGenerator = SimpleTrafficGenerator(2)


slowDownProbability, laneChangeProbability = 0, 0



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