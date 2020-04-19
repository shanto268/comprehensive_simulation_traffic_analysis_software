import sys, pygame, simulation.road, simulation.speedLimits, random, importlib, config
from representation import Representation
from simulationManager import SimulationManager
from simulation.trafficGenerators import *

pygame.init()
pygame.display.set_caption('Traffic Analysis Software')

# cd Documents\Research_work\Traffic_flow\Python

#if len(sys.argv) != 2: #number of arguments
#    print("Usage: python pyTraffic.py module_with_config")
#    exit()

#config = importlib.import_module(sys.argv[1]) #sys.argv[1] = e.g. .case or .trafficlight
config = importlib.import_module('config.case') #sys.argv[1] = e.g. .case or .trafficlight


random.seed(config.seed) #this too
pygame.init()
screen = pygame.display.set_mode(config.size)

clock = pygame.time.Clock() #object created to keep track of time

speedLimits = simulation.speedLimits.SpeedLimits(config.speedLimits, config.maxSpeed) #takes speedLimits and maxSpeed input from source file
road = simulation.road.Road(config.lanes, config.length, speedLimits) #road takes lane and length input from source file and speed limit from ^
simulation = SimulationManager(road, config.trafficGenerator, config.updateFrame) #simulation takes input from road, trafficgen from source file, and update frame from source file
representation = Representation(screen, road, simulation)#from above functions


while simulation.running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            simulation.processKey(event.key)
    clock.tick_busy_loop(config.maxFps)#.tick_busy_loop = updates the clock
    dt = clock.get_time()# —	time used in the previous tick
    simulation.update(dt) #updates logistics
    representation.draw(dt * simulation.timeFactor) #updates graphics
  #  representation.batch(dt * simulation.timeFactor) #batch mode
    pygame.display.flip()


