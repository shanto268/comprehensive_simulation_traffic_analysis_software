import pygame, random
from infoDisplayer import *
from simulation.trafficGenerators import *
import math as mp

class Representation():
    def __init__(self, screen, road, simulationManager, data):
        self.screen = screen
        self.width, self.heigth = screen.get_width(), screen.get_height()
        self.road = road
        self.updateFrame = simulationManager.updateFrame
        self.margins = (10, 10)
        self.cellSize = 12 #the height of road
        self.acc = 0
        self.theta = 0
        self.data = data
        self.infoDisplayer = InfoDisplayer(screen, road, simulationManager, data)
        self.colors = [ (255, 0, 0), (180, 20, 0), (80, 60, 0), (100, 80, 0), (0, 180, 0), (0, 255, 0), (80, 120, 0), (60, 140, 0), (40, 160, 0) ]
        self.colors1 = [(39,64,139), (205,0,0)] #hv blue

    def draw(self, dt):#updates simulation
        self.__updateAcc(dt) #updates infodisplayer
        self.screen.fill( (0,100,0) ) #background
        self.drawRoad(dt)
        self.infoDisplayer.draw() #draws the comments and updates

    def batch(self, dt):#updates simulation
        self.__updateAcc(dt) #updates infodisplayer
     #   self.screen.fill( (0,100,0) ) #background
     #   self.drawRoad(dt)
     #   self.infoDisplayer.draw() #draws the comments and updates

    def drawRoad(self, dt): #determines widht and number of lane geometry
        y = 0
        for lane in self.road.lanes:
            self.__drawLane(lane, y, dt)
            y += self.cellSize  #number of values depend on the number of lanes
         #   print("y: " + str(y))
            
    def __drawLane(self, lane, y, dt):  #draws the cars and empty road
        x = 0
        for cell in lane: #cell stores the value (i.e. None if empty or car object if car object!) it is the element
            idx = x / self.cellSize, y / self.cellSize #each grid id in coordinates (x,y)
            speedLimit = self.road.getSpeedLimitAt(idx)
            self.__drawCell(x, y, speedLimit) 
            if cell != None:             
                self.__drawCar(cell, x, y)
            x += self.cellSize #the width of the road
            
    def __drawCell_dedicated(self, x, y, speedLimit): #draws the road cells
        if self.road.updates > 10: #include color condition for dedicated lane --> change the current condition and dedicated lane colored only
            realPos = self.__getPosOnScreen((x,y)) #needs change
            pygame.draw.rect(self.screen, ( 180, 180, 180), (realPos[0], realPos[1], self.cellSize, self.cellSize), 0) 
        else: 
            realPos = self.__getPosOnScreen((x,y)) 
            pygame.draw.rect(self.screen, ( 180, 180, 180), (realPos[0], realPos[1], self.cellSize, self.cellSize), 0) 
    
    def __drawCell(self, x, y, speedLimit): #draws the road cells
            realPos = self.__getPosOnScreen((x,y)) #needs change
            pygame.draw.rect(self.screen, ( 180, 180, 180), (realPos[0], realPos[1], self.cellSize, self.cellSize), 0) 
    
    def drawCellSpeedLimits(self, x, y, speedLimit):
            realPos = self.__getPosOnScreen((x,y)) #needs change
            pygame.draw.rect(self.screen, ( 180, 180, 180), (realPos[0], realPos[1], self.cellSize, self.cellSize), 0) 
           #include new colors 
           #import config
           #include speed and ticks from config file

    def __drawCar(self,car, x, y): #include param for type
        invProgress = (1 - self.acc / self.updateFrame)*self.cellSize
        offset = (car.prevPos[0] - car.pos[0])*invProgress, (car.prevPos[1] - car.pos[1])*invProgress
        realPos = self.__getPosOnScreen((x+offset[0], y+offset[1]))
        if car.vtype == 1:
            pygame.draw.rect(self.screen, self.colors1[0], (realPos[0],realPos[1],self.cellSize,self.cellSize), 0)
        else:
            pygame.draw.rect(self.screen, self.colors1[1], (realPos[0],realPos[1],self.cellSize,self.cellSize), 0)


    def __updateAcc(self, dt):#updates infodisplayer
        self.acc += dt
        if self.acc >= self.updateFrame:
            self.infoDisplayer.update()
        self.acc = self.acc % (self.updateFrame + 0)
     
        # draws the car blocs
    def __getPosOnScreen(self, pos):
        x, y = pos
        while x + self.margins[0] >= self.width - self.margins[0]:
            x -= (self.width - 2*self.margins[0])
            y += (self.road.getLanesCount() + 1) * self.cellSize + self.cellSize
        return (x + self.margins[0], y + self.margins[1])
