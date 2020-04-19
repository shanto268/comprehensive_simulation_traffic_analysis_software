# comment/uncomment for different experiment

import pygame

time_period = 100 
simTime = 1200

class SimulationManager: 
    def __init__(self, road, trafficGenerator, updateFrame):
        self.road = road
        self.trafficGenerator = trafficGenerator
        self.updateFrame = updateFrame
        self.acc = 0
        self.timeFactor = 20.0
        self.prevTimeFactor = 1.0
        self.running = True
        self.stepsMade = 0

    def update(self, dt): #updates the traffic input and the car-road interplay
        self.acc += dt * self.timeFactor
        limit = 0
        if self.acc >= self.updateFrame:
            self.acc = self.acc % (self.updateFrame + 0)
           # self.makeStep_constant_density()  #comment this for increasing density
            self.makeStep_increasing_density()  #uncomment this for increasing density
       # self.endSimulation()  #uncomment for steady state
            self.endSim_fd() #comment for increasing density
            
    def makeSteps(self, steps): #makes multiple steps
      #  for x in range(steps): self.makeStep_constant_density()  #comment this for increasing density
        for x in range(steps): self.makeStep_increasing_density()  #uncomment this for increasing density
        
    def makeStep_constant_density(self):  #for constant density
        if self.stepsMade == 0:
            self.trafficGenerator.generate(self.road) #generates traffic
        self.road.update(); 
        self.stepsMade += 1
         
    def makeStep_increasing_density(self): #for increasing density
        if self.stepsMade == 0:
            self.trafficGenerator.generate(self.road) #generates traffic
        if self.stepsMade >= time_period and (self.stepsMade % time_period) == 1 : #increases density every 100 updates
            self.trafficGenerator.generate(self.road)
        self.road.update(); 
        self.stepsMade += 1    
    
    def processKey(self, key):
        {
            pygame.K_ESCAPE: self.__exit,
            pygame.K_SPACE:  self.__pauseSwitch,
            pygame.K_m: self.__speedUp,
            pygame.K_n: self.__speedDown,
            pygame.K_s: self.__oneStepForward,
            pygame.K_d: self.__manyStepsForward(100)
        }.get(key, lambda: print("Unknown key"))()

    def isStopped(self):
        return self.timeFactor == 0

    def __exit(self): 
        self.running = False
        
    def __pauseSwitch(self):
        self.timeFactor, self.prevTimeFactor = self.prevTimeFactor, self.timeFactor
    def __speedUp(self): 
        self.timeFactor = min(8.0, self.timeFactor*2)

    def __speedDown(self): 
        self.timeFactor = max(1/8, self.timeFactor/2)

    def __oneStepForward(self):
        if self.isStopped(): 
         #   self.makeStep_constant_density()  #comment this for increasing density
           self.makeStep_increasing_density()  #uncomment this for increasing density
        else: print("Can't make step: simulation is running")
    def __manyStepsForward(self, steps):
        def manySteps():
            self.makeSteps(steps)
        return manySteps
    
    def endSimulation(self):
        if (self.road.updates == simTime):
            self.running = False
            
    def endSim_fd(self):
        if self.road.carCount() == 300:
            self.running = False
