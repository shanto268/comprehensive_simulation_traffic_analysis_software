import sys, pygame, simulation.road, simulation.speedLimits, random, importlib, config
from representation import Representation
from simulationManager import SimulationManager
from simulation.trafficGenerators import *

class caEnv_v0():
    def __init__(self,config):
        self.config = config
        self.data = config.data
        print(self.data)

    #def reset(self):
    #def step(self,action):
        
    def displayInitialize(self, isBatch):
        if isBatch:
            print("Initializing batch simulation....")
            print("Starting simulation...\n")
        else:
            pygame.init()
            pygame.display.set_caption('Traffic Analysis Software')

    def render_interactive(self):
        random.seed(config.seed) 
        screen = pygame.display.set_mode(config.size)
        clock = pygame.time.Clock()
        speedLimits = simulation.speedLimits.SpeedLimits(config.speedLimits, config.maxSpeed)
        road = simulation.road.Road(config.lanes, config.length, speedLimits) 
        simulation_ = SimulationManager(road, config.trafficGenerator, config.updateFrame) 
        representation = Representation(screen, road, simulation_, config.data)
        while simulation_.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    simulation_.processKey(event.key)
            clock.tick_busy_loop(config.maxFps)#.tick_busy_loop = updates the clock
            dt = clock.get_time()# —	time used in the previous tick
            simulation_.update(dt) #updates logistics
            representation.draw(dt * simulation_.timeFactor) #updates graphics
            pygame.display.flip()

    def render_batch(self):
        random.seed(config.seed)
        clock = pygame.time.Clock()
        speedLimits = simulation.speedLimits.SpeedLimits(config.speedLimits, config.maxSpeed)
        road = simulation.road.Road(config.lanes, config.length, speedLimits) 
        simulation_ = SimulationManager(road, config.trafficGenerator, config.updateFrame) 
        while simulation_.running:
            clock.tick_busy_loop(config.maxFps)#
            dt = clock.get_time()# —	time used in the previous tick
            simulation_.update(dt) #updates logistics

    def runInteractive(self):
        self.displayInitialize(False) #interactive
        self.render_interactive()

    def runBatch(self): 
        self.displayInitialize(True) #batch
        self.render_batch()

#    def getStateSpace(self):
#    def getActionSpace(self):
#    def getStateSpaceSize(self, state_space):
#    def getActionSpaceSize(self, action_space):



# main
config = importlib.import_module('config.case')
mode = sys.argv[1]
env = caEnv_v0(config)
if mode=="batch":
    env.runBatch()
elif mode=="gui": 
    env.runInteractive()
else:
    env.runBatch()
