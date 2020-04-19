#change made in maxSpeed
import simulation.speedLimits, random
from functools import reduce
from simulation.car import Car
import math as mp
import numpy as np
import sys

#changes made in inbounds and simulationmanager --> problem in update x and pos[0] function conditions.. dead when coincide and glides

c1 = 12
maxSpeed = int(sys.argv[3])    #change maxSpeed for exp1 (3 for base, 5 for aware, 4 for oppo)
time_period = 100

class Road:
    
    def __init__(self, lanesCount, length, speedLimits):
        self.lanes = Road.generateEmptyLanes(lanesCount, length) #functional call to create empty lanes using user input -> returns desired number of lanes with desired number of length with None values as elements
        self.updatedLanes = Road.generateEmptyLanes(lanesCount, length) #same as above but used to update the elements of the created structure
        self.speedLimits = speedLimits if speedLimits != None else simulation.speedLimits.SpeedLimits([], 5) #refers to speedlimits.py to set speedlimits
        self.deadAV = 0 # cars that are gone
        self.updates = 0 #number of updates?
        self.deadCars = 0
        self.rv = 0
        self.vcount = 0
        self.avgclus = 0
        self.av = 0
        self.count = 1
        self.clunum = 0
        self.lanechange = 0
        self.rvlane = 0
        self.avlane = 0
        self.contspeed = 3.5
        self.contprop = 30
        self.tick = 0
        self.amount = 0
        self.temp = []
        self.even = 0
        self.odd = 0
        self.result = 0
        self.lanesCount = lanesCount
        self.L0c = 0
        self.length = length
        self.avprop = 0
        self.start = 0
        self.startt = 0
        self.trigger= 0
        self.triggert= 0
        self.addedtime = []
        self.avproptime = []
        self.avgveloc= []
        self.dlane = 0
        self.avg = 0
        self.avarr = []
        self.trigga = 0
        self.avee = 0
        self.c = 0
        self.d = 0
        self.clarr = []
        self.clnum = 0
        self.freqAV = 0
        self.numer = 0
        self.denom = 0
        self.clsize = 0
        self.laneform_count = 0 #counts the number of lane formations
        self.laneform_size = [] #keeps the size of lane formations
        self.cluster_count = 0 #counts the number of lane formations
        self.clusterform_size = [] #keeps the size of clusters
        self.triggerbin = 0
        self.cluster_num_car = 0 #number of cars in cluster
        self.avpercent = 18    #case: AV   12 -  20%    9 - 15% ; 18 - 30%  ; 30 - 50%;  45 - 75%  
        
        
    def __updateCars(self, action):
        for lane in self.lanes:
            for entity in lane:
                if entity != None:       
                    if entity.vtype == 2:
                        self.avee += 1
                    newPos = action(entity) #tuple --> (x + v, lane) 
                    if self.inBounds(newPos): #returns  true #newpos[0] = position on x: x_i + v  #newpos[1]: lane number
                        self.updatedLanes[newPos[1]][newPos[0]] = entity
                        self.lanechange = self.lanechangenum(entity.feedlaneroadpy())
                      #  self.L0c = self.lanechangenum(entity.feedlaneroadLO())
                        self.numer += entity.freq
                        self.denom += entity.freqtot
                        if self.denom == 0:
                            self.freqAV = 0
                        else:            
                            self.freqAV = self.numer / self.denom
                        
                      #  print("moving at: "+str(newpos))
                    else:
                        print("dead at: "+str(newPos))
         
    #    print(newPos)                     
        self.flipLanes() #makes the road empty for new cars to enter and propagates existing cars in the lanes
        
    def _updateCars(self, action):
        for lane in self.lanes:
            for entity in lane:
                if entity != None:       
                    newPos = list(action(entity)) #tuple --> (x + v, lane)     
            #        print("moving at at: "+str(newPos))
                    if self.inBounds(newPos):
                        self.updatedLanes[newPos[1]][newPos[0]-self.getLength()] = entity 
                     #   print(entity)
                        self.lanechange = self.lanechangenum(entity.feedlaneroadpy()) #total number of lane changes
                        self.avlane = self.lanechangenum(entity.feedav()) #total number of av lane change
                        self.rvlane = self.lanechange - self.avlane #total number of av lane change
                   #     self.L0c = self.lanechangenum(entity.feedlaneroadLO())
                        self.numer += entity.freq
                        self.denom += entity.freqtot
                        if self.denom == 0:
                            self.freqAV = 0
                        else:            
                            self.freqAV = self.numer / self.denom
                    #    print("freq: " + str(self.numer))
                    #    print("freqtot: " + str(self.denom))
                      #  print("moving at: "+str(newPos))

        self.flipLanes()            
    
    def update(self): #updates speedlimits and car movements
        self.speedLimits.update()   
        self.lane_form()
        self.cluster()
        r1 = lambda x: x.updateLane()  #for hetero only
        speedupdate = lambda x: x.updateX()
        vupdate = lambda x: x._updateX()
        r2 = lambda x: x.dynamicupdateLane()
        self._updateCars(r1) #pass lanechange for just regular heteregenous flow 
        self._updateCars(speedupdate)
       # print(self.av) 
     #   print("Update: " + str(self.updates))
        if (self.updates % 100) == 1:
            self.avee = self.av     
        elif self.updates <= 100: self.avee = self.av 
        self.avgspeed = self.getAvgCarSpeed()[1]
        self.avgveloc.append(self.avgspeed)
        if self.updates > 0 and (self.updates % 100) == 0:
            self.vcount = 0
            self.avg = (sum(self.avgveloc[self.start:self.updates - 1]) / 100)
            self.start = self.updates
        self.updates += 1    
       # if self.updates > 100: self.av = 0 
      #  print(self.avee)
   #     print(self.avg)    
   #     print("update: " + str(self.updates))
  #      print("")
    def lanechangenum(self, num): 
        return num
    
    '''
    def triggerdyn(self):
        if self.avg < 2 and ((self.avee / self.amount) * 100) > 30 and (self.updates % 100) == 1: #dyn lane trigger conditions
            self.trigga += 1
        return self.trigga
    '''
    def flipLanes(self):#makes the road empty for new cars to enter and propagates existing cars in the lanes
        self.lanes = self.updatedLanes
        self.updatedLanes = Road.generateEmptyLanes(self.getLanesCount(), self.getLength())
        
    def triggerplot1(self):
        self.triggerbin = 1
    def triggerplot2(self):
        self.triggerbin = 0
        
    def addCar(self): #doesn't seemed to have been used. Boolean Results!
        if self.lanes[0][0] == None: #true initially
            self.lanes[0][0] = Car(self, (0,0)) #initiates the identity car at with road being self, and position being (0,0)
            return True 
        else:
            return False

    def pushCars(self, amount): #amount comes from TG
        return self.__dpushCars(amount)
    
    def __dpushCars(self, amount): #if car pushed then return 1, if not then 0 -->HETERO
        if not amount: return 0
        else:
            for index in range(amount):
                lane = random.randint(0,2)
                car = Car(self, (random.randint(0,self.getLength()-1), lane), self.speedLimits.maxSpeed, self.assigntype())
                if(self.placeObject(car)): #if true --> object in desired position is not blocked
                    return 1 + self.__dpushCars(amount - 1)
                else: 
                    return 0 +  self.__dpushCars( amount )

    def pushCarsRandomly(self, amount): #does what the name suggests
        lanes = [x for x in range(self.getLanesCount())] 
        random.shuffle(lanes) #changes lane order
       # print("lane order " +str(lanes))
        return self.__pushCars(amount, lanes)
   
    def gtpushcars(self, inflow):
        lanes = [x for x in range(self.getLanesCount())] 
        random.shuffle(lanes)
        return self.gt__pushCars(inflow, lanes)    
          
    def gt__pushCars(self, inflow, lanes): #if car pushed then return 1, if not then 0
        #totalCars, avgSpeed = self.getAvgCarSpeed()
        lane = lanes.pop() 
        avnum = self.gaussianprob(inflow)
        rvnum = inflow - avnum
       # print("RV: "+ str(rvnum))
        for cars in range(1,avnum+1):  
            car = Car(self, (0, lane), self.speedLimits.maxSpeed, 2)
           # print("AV num " + str(cars)) #First AV car 1
        for carse in range(avnum+1,inflow+1):
            car = Car(self, (0, lane), self.speedLimits.maxSpeed, 1)
          #  print("Regular V num " + str(carse)) #First RV car 1 + avnum
       
    def gaussianprob(self, inflow):  
        mu, sigma = 3, .5 # mean and standard deviation
        s = np.random.normal(mu, sigma, 100)        
        x =random.randint(0,99)
      #  print("x " + str(x))
        print(s[x])
        print(mp.floor(s[x]))
        avnumber =mp.ceil(( s[x] / 100 ) * inflow )
      #  print("AV number: " + str(avnumber))         
        return avnumber 
    
    def _pushCarsRandomly(self, amount): #does what the name suggests
        lanes = [x for x in range(self.getLanesCount())] 
        random.shuffle(lanes) #changes lane order
        return self.t__pushCars(amount, lanes)
    
    def assigntype(self):   
        '''
        mu, sigma = .15, .05                        # mean and standard deviation 
        avprob = np.random.normal(mu, sigma, 100) 
        x =random.randint(0,99)
        prob_av = avprob[x]
     #   print("Prob(AV): " + str(prob_av))
        prob_rv = 1 - prob_av
   #     print("Prob(RV): " + str(prob_rv))
        y = random.uniform(0, 1)
        z = random.uniform(0.38,0.4)
        d_av = abs(y - prob_av + z)
        d_rv = abs(y - prob_rv)
        print("d(AV): " + str(d_av))
        print("d(RV): " + str(d_rv))
        w = min(d_rv,d_av)  
      #  print("Choice: " + str(w))
       # print("")
       '''
     #  d_rv = 
     #  d_av = 
        w = random.randint(1,60)
        if w > int(self.avpercent):                       #   case: RV   9 - 15% ; 18 - 30% ; 30 - 50%;  45 - 75%
          vtype = 1
          return vtype
        elif w <= int(self.avpercent) :                             
         vtype = 2
         return vtype 
         
        
    def t__pushCars(self, amount, lanes): #if car pushed then return 1, if not then 0
        if not amount or not lanes: return 0
        else:
            lane = lanes.pop() #decides which lane to select
     #      print("lane popped " +str(lane))
            car = Car(self, (0, lane), self.speedLimits.maxSpeed, self.assigntype()) #point of generation of object Car at a random lane
            if(self.placeObject(car)): #if true --> object is at starting position
                if car.vtype == 2:
                    self.avcount += 1
                return 1 + self.t__pushCars(amount - 1, lanes) #recursive condition that counts number of cars enterring
            else:
                return self.t__pushCars(amount, lanes)     
    def carcount(self):        
        for lane in self.lanes:
            none = lane[0:119].count(None)
            numcar = self.getCellCount() - none 
            return numcar
            
    def carCount(self):
        return sum( reduce(lambda x, y: x+(0 if y == None else 1), lane, 0) for lane in self.lanes)          
    
    def AVprop(self):
        if self.carCount() > 0:
            avprop = ((self.av - self.deadAV) / self.carCount()) * 100
        elif self.carCount() == 0:
            avprop = ((self.av - self.deadAV) / (self.carCount() + 1) ) * 100
        return avprop
    
    def __pushCars(self, amount, lanes): #if car pushed then return 1, if not then 0 -->HETERO
        if not amount or not lanes: return 0
        else:
            lane = random.randint(0,2)
            #lane = lanes.pop()
            car = Car(self, (random.randint(0,self.getLength()-1), lane), self.speedLimits.maxSpeed, self.assigntype())
            if(self.placeObject(car)): #if true --> object in desired position is not blocked
                return 1 + self.__pushCars(amount - 1, lanes) #recursive condition that counts number of cars enterring
            else:
                return self.__pushCars(amount, lanes)
            
    
    def avinflow(self, amount):
        self.temp.append(amount)
   #     print(self.temp)
   #     print(self.temp[len(self.temp) - 1])   
        if (self.updates % 2) == 0: #even 
            self.even = self.temp[len(self.temp) - 1]
        else: 
            self.odd = self.temp[len(self.temp) - 1]
        self.result = abs(- self.even + self.odd)
   #     print("result: " + str(self.result))
            
  
        
    #sum(iterable, start) --> for each lane from start from zero and add all cars as they come in
    def getSpeedLimitAt(self, pos):
        return self.speedLimits.getLimit(pos)         
        
    
    def distanceToNextThing(self, pos): #gives distance to next thing
        #Counts distance between given pos and next object (car or obstacle), takes into considerations stops (speedLimit set to 0)
    #    print(self.__distanceToNextThing((pos[0]+1, pos[1])))         
     #   print("")
        return self.__distanceToNextThing((pos[0]+1, pos[1]))
 
    def __distanceToNextThing(self, pos):
        if pos[0] >= self.getLength():
          #  pos = pos[0] % self.getLength(), pos[1]
            return self.getLength() # leaves the screen
        else:
            #print(self.lanes[pos[1]][pos[0]])
            if self.lanes[pos[1]][pos[0]] == None and not self.speedLimits.shouldStop(pos):
                return 1 + self.__distanceToNextThing((pos[0]+1, pos[1]))
            else:
                return 0
    
    def ncvtype1(self, pos): #looping case boundary
        return self.nxtcartype1((pos[0]+1, pos[1]))
        
    def nxtcartype1(self, pos): #looping case boundary
        
        if pos[0] >= self.getLength():
            pos = pos[0] % self.getLength(), pos[1]
            
        if self.d == 100:
            self.d = 0
            return self.getLength()
            
        if self.lanes[pos[1]][pos[0]] == None:
            self.d += 1
            return self.ncvtype1((pos[0]+1, pos[1]))                
        
        else:
            self.d = 0
            return (self.lanes[pos[1]][pos[0]]).vtype
        
    def ncvtype2(self, pos): #regular case
        return self.nxtcartype2((pos[0]+1, pos[1]))
 
       
    def nxtcartype2(self, pos): #regular case       
        if pos[0] >= self.getLength():
            return self.getLength()
            
        if self.lanes[pos[1]][pos[0]] == None:
            return self.ncvtype2((pos[0]+1, pos[1]))                
        
        else:
            return (self.lanes[pos[1]][pos[0]]).vtype    
  
    def loopfix(self, pos):
        
        if pos[0] >= self.getLength():
            pos = pos[0] % self.getLength(), pos[1]
            self.vcount += 1 #for flow

        if self.c == 200:
            self.c = 0
            return self.getLength()
            
        if self.lanes[pos[1]][pos[0]] == None:
            self.c += 1
            return 1 + self.loopfix((pos[0]+1, pos[1]))                
        else:
            self.c = 0
            return 0
        
    def dton(self, pos):
        return self.loopfix((pos[0]+1, pos[1]))
    
    def d2n(self, pos):
        v = min(self.getSpeedLimitAt(pos), self.dton(pos))
        return v
    
    """
    def newSpeedLimit_loop(self, pos): #for aware case
        #for aware case ---> loop case
        return 1000
    """
    
    def getMaxSpeedAt(self, pos):
        v = min(self.getSpeedLimitAt(pos), self.distanceToNextThing(pos))
        return v #compares the distance to the next thing and the speedlimit to return the smaller value as max speed
        
        """  need to change getSpeedLimitAt to to be dependent on type  also traffic limit """

    def findPrevCar(self, pos): #gives lane element from lanes
        if not self.inBounds(pos) or self.getSpeedLimitAt(pos) == 0: return None
        else:
            if self.lanes[pos[1]][pos[0]] != None:
                return self.lanes[pos[1]][pos[0]]
            else:
                return self.findPrevCar( (pos[0] - 1, pos[1]) ) #looping conditon --> checks backwards
        
    def possibleLaneChangeUp(self, pos):
        return self.__possibleLaneChange(pos, pos[1]-1)
    
    def possibleLaneChangeDown(self, pos):
        return self.__possibleLaneChange(pos, pos[1]+1)
    
    def __possibleLaneChange(self, pos, destLane): #returns boolean
       # print("Pos[0]" + str(((pos[0]- (self.getLength()))%100)))
        if not self.inBounds( (0, destLane) ) or self.lanes[destLane][pos[0]] != None:
              return False  #False if the destLane pos has a car or the pos is out of bounds
        else:
            sourceLane = pos[1]
            oneMoreLane = destLane + (destLane - sourceLane)
            if not self.inBounds( (0, oneMoreLane) ):  
                return True
            else:
                return self.lanes[oneMoreLane][pos[0]] == None
     
    def inflow(self, amount):
        self.amount = amount
        
        # Altered for dynamic control        
    def dyn_possibleLaneChangeUp(self, pos):
        return self.dyn__possibleLaneChange(pos, pos[1]-1) #inputs passed ((speed, sourcelane), destlane)
    
    def dyn_possibleLaneChangeDown(self, pos):
        return self.dyn__possibleLaneChange(pos, pos[1]+1)
    
    def dyn__possibleLaneChange(self, pos, destLane): #returns boolean
        if not self.inBounds( (0, destLane) ) or self.lanes[destLane][pos[0]] != None or destLane == 0:
              return False  #False if the destLane pos has a car or the pos is out of bounds
        else:
            sourceLane = pos[1]
            oneMoreLane = destLane + (destLane - sourceLane)
            if not self.inBounds( (0, oneMoreLane) ) or sourceLane == 0:  
                return True
            else:
                return self.lanes[oneMoreLane][pos[0]] == None
            
    def dynav_possibleLaneChangeUp(self, pos):
        return self.dynav__possibleLaneChange(pos, pos[1]-1) #inputs passed ((speed, sourcelane), destlane)
    
    def dynav_possibleLaneChangeDown(self, pos):
        return self.dynav__possibleLaneChange(pos, pos[1]+1)
    
    def dynav__possibleLaneChange(self, pos, destLane): #returns boolean
        sourceLane = pos[1]
        if not self.inBounds( (0, destLane) ) or self.lanes[destLane][pos[0]] != None or sourceLane == 0:
              return False  #False if the destLane pos has a car or the pos is out of bounds
        else:
            oneMoreLane = destLane + (destLane - sourceLane)
            if not self.inBounds( (0, oneMoreLane) ) or destLane == 0:  
                return True
            else:
                return self.lanes[oneMoreLane][pos[0]] == None       
            
            
    def loopinbounds(self, pos):
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] >= self.getLength() and pos[1] < self.getLanesCount()    
        #   Altered code above ^ 
    
    
    """ FOR INCREASING DENSITY """
    
    def inBounds(self, pos):
       #           **************************LOOK HERE: the following should be commented for same density levels!!!****************
        if self.updates != 0 and (self.updates % time_period) == 0: #important for looping and refreshing
            return False
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < self.getLength() and pos[1] < self.getLanesCount()
    
    #THE CODE BELOW IS FOR STEADY STATE
    """
    def inBounds(self, pos):
      # print(self.inBounds)   #constraints movement of vehicle to these chosen parameters
#        if self.updates != 0 and (self.updates % 100) == 0: #important for looping and refreshing
#            return False
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < self.getLength() and pos[1] < self.getLanesCount()
    """
    
    def clearAt(self, pos):
        self.lanes[pos[1]][pos[0]] = None
    
    def placeObjects(self, entities):
        return all(self.placeObject(entity) for entity in entities)

    def placeObject(self, entity): #function that takes in input of car object and returns Bolean output whether object is placed in a certain lanes[entity.pos[0]][entity.pos[1]] or not
        if (not self.inBounds(entity.pos)
                or self.lanes[entity.pos[1]][entity.pos[0]] != None #entity.pos[0] = 0 for cars being generated; entity.pos[1] = lane
                or self.getSpeedLimitAt(entity.pos) == 0 ):
            return False  #essentially empty cells return False
        else:
            self.lanes[entity.pos[1]][entity.pos[0]] = entity
            if entity.vtype == 1:
                self.rv += 1 
            else: 
                self.av += 1        
            return True # condition met --> True for placing an object
        
    def getLength(self): #gives length of each road --> user input
      #  print("getLenght: " + str(len(self.lanes[0])))
        return len(self.lanes[0]) #number of elements in one array of lanes
    def getLanesCount(self):
      #  print("getLane: " + str(len(self.lanes)))
        return len(self.lanes) #number of lanes
    def getCellCount(self):
        #print(self.getLengthincoming() * self.getLanesCount())
        return self.getLength() * self.getLanesCount() #total number of cells
    
    def getLengthincoming(self):
        lane = self.lanes[0]
      #  print(lane[0:7])
     #   print(none)
        cellincome = len(lane[0:8])
       # print(cellincome)
        return cellincome
    
    def incomingcars(self):
        lane = self.lanes[0]
        none = lane[0:8].count(None)
        cellincome = len(lane[0:7])
        carnumber = cellincome - none
        return carnumber * self.getLanesCount()
        
    def getCellCountincoming(self):
    #    print(self.getLengthincoming() * self.getLanesCount())
        return self.getLengthincoming() * self.getLanesCount() 
    
    def getAvgCarSpeed(self): #counts the number of cars and avg speed
        total = 0
        cars = 0

      #  print(self.lanes)
        for lane in self.lanes:
        #    print("Lane: " + str(lane))
            for entity in lane:
                if entity != None:
                    cars += 1 
                    total += entity.velocity #include further if conditions to calculate the number of AVs and RVs and caclulate their speed seperately
                                                           
        return (cars, total/cars if cars > 0 else 0)
    
    def flow(self):
        self.vcount += 1 
     #   return self.vcount
       # print(self.vcount)
    
    def fdav(self):
        total = 0
        cars = 0
      #  print(self.lanes)
        for lane in self.lanes:
        #    print("Lane: " + str(lane))
            for entity in lane:
                if entity != None:
                    if entity.vtype == 2: #av
                        cars += 1
                        total += entity.velocity                                      
        return (cars, total/cars if cars > 0 else 0)
    
    def fdrv(self):        
        total = 0
        cars = 0
      #  print(self.lanes)
        for lane in self.lanes:
        #    print("Lane: " + str(lane))
            for entity in lane:
                if entity != None:
                    if entity.vtype == 1: #rv
                        cars += 1
                        total += entity.velocity                                      
        return (cars, total/cars if cars > 0 else 0)

    def generateEmptyLanes(lanesCount, length):
        lanes = [] #initialize lane array
        for x in range(lanesCount): #loops for number of lanes to be created 
            lanes.append( [None] * length ) #creates empty lane of None values with desired length
        return lanes

    def getAvgCarSpeedincoming(self): #counts the number of cars and avg speed
        total = 0
        cars = 0
        lanes = self.lanes
     #   print(self.lanes)
        for lane in lanes:
            #print("Lane: " + str(lane))
            for entity in lane[9:141]:
                if entity != None:
                    cars += 1 
                    total += entity.velocity 
        return (cars, total/cars if cars > 0 else 0)


    def cluster(self):
        cars = []  #stores all car objects
        cars_type = [] #stores all car types
        cars_pos = []  #stores all car pos(x,y)
        cars_x = [] #stores x pos values
        cars_lane = [] #stores lane numbers of cars
        cars_0l = [] #cars in lane 0
        cars_1l = [] #cars in lane 1
        cars_2l = [] #cars in lane 2
        carstype_0l = [] #car type in lane 0
        carstype_1l = [] #car type in lane 1
        carstype_2l = [] #car type in lane 2
        gap = 3
        cluster_thresh = 4
        
        
        for lane in self.lanes:
            for entity in lane:
                if entity != None: 
                    cars.append(entity)
                    cars_type.append(entity.vtype)
                    cars_pos.append(entity.pos)
                    cars_x.append(entity.pos[0])
                    cars_lane.append(entity.pos[1])
                    if entity.pos[1] == 0: #lane 0
                        cars_0l.append(entity)
                        carstype_0l.append(entity.vtype)
                    if entity.pos[1] == 1: # lane 1
                        cars_1l.append(entity)
                        carstype_1l.append(entity.vtype)
                    if entity.pos[1] == 2: #lane 2
                        cars_2l.append(entity)
                        carstype_2l.append(entity.vtype)
        avs = []
        avs_pos = []
        avs_x = []
        for car in cars:
            if car.vtype == 2:
                avs.append(car)
                avs_pos.append(car.pos)
                avs_x.append(car.pos[0])
        
        avs_x.sort()
     #   print("")
     #   print(avs_x)      

        
        MC = []
        MC.append([])
        u = 0
        count = 0
        car_clus = 0
        for i in range(len(avs_x)):
            j=i+1
            if j < len(avs_x) and (avs_x[j] - avs_x[i]) <= gap:
                MC[u].append(avs_x[i])  
                if j == (len(avs_x) - 1):
                    MC[u].append(avs_x[j])
                elif (j < len(avs_x)) and (avs_x[j+1] - avs_x[j]) > gap:
                    MC[u].append(avs_x[j])  
                    MC.append([])
                    u += 1 
    #    print("\nPosition Cluster: " + str(MC))
        new_cl = []
        for arr in MC:
            if len(arr) >= cluster_thresh:
                self.clusterform_size.append((len(arr),self.updates))
                new_cl.append(len(arr))
                car_clus += len(arr) #sas new add 2020
                count+=1
        
        self.cluster_num_car = car_clus
      #  print(self.cluster_num_car)
        self.clunum = count        
        new = self.clusterform_size
        clstr = []
        
    #    print("\ncluster size: "+str(new))
        
        clinfo = []
        
        avg_size = 0
        for size in new_cl:
            avg_size += size                 
            clinfo.append((size, self.updates))
            
        if count == 0:
            off_size = 0
        else:
            off_size = avg_size / count
        self.avgclus = off_size
        self.clarr = clinfo
   #     print("\nnumber of clusters " + str(count)) #distribute this count over time
   ##     print("\nCL info: " + str(clinfo))
    #    print("\navg size " + str(off_size)) #distribute this over time
        
        """ NEW CODE """
        
        new = sorted(new , key= lambda k: [k[0], k[1]])
        
        for i in range(len(new)):
            j=i+1
            if j < len(new) and (new[i][0] == new[j][0] and (new[j][1] - new[i][1]) == 1):
                clstr.append(new[j])
                
        
        final = [item for item in new if item not in clstr]       
      #  size = []
     #   print("(Cluster size, time step created): "+ str(final)) 
      #  self.clarr = final   #old version
        #for i in range(len(final)):
           # self.clsize = (ele[0])
       #     if i == (len(final)-1):
             #   print(i)
              #  print("Latest cluster size: " +str(final[i][0]))
             # print("")
        self.clnum = len(final)
         
        
     #   print("Total number of clusters: " + str(len(final)))        
     #   print(self.clsize)  
       # print("")  

        
        
        
    def lane_form(self):          
        
        cars = []  #stores all car objects
        cars_type = [] #stores all car types
        cars_pos = []  #stores all car pos(x,y)
        cars_x = [] #stores x pos values
        cars_lane = [] #stores lane numbers of cars
        cars_0l = [] #cars in lane 0
        cars_1l = [] #cars in lane 1
        cars_2l = [] #cars in lane 2
        carstype_0l = [] #car type in lane 0
        carstype_1l = [] #car type in lane 1
        carstype_2l = [] #car type in lane 2
        lane_size = 0
        
        j = 0
        for lane in self.lanes:
            for entity in lane:
                if entity != None: 
                    cars.append(entity)
                    cars_type.append(entity.vtype)
                    cars_pos.append(entity.pos)
                    cars_x.append(entity.pos[0])
                    cars_lane.append(entity.pos[1])
                    if entity.pos[1] == 0: #lane 0
                        cars_0l.append(entity)
                        carstype_0l.append(entity.vtype)
                    if entity.pos[1] == 1: # lane 1
                        cars_1l.append(entity)
                        carstype_1l.append(entity.vtype)
                    if entity.pos[1] == 2: #lane 2
                        cars_2l.append(entity)
                        carstype_2l.append(entity.vtype)
       
        for i in range(len(carstype_0l)):
            j+=1 
            if j < len(carstype_0l) and carstype_0l[i] == carstype_0l[j] == 2:
                lane_size += 1
        if (lane_size + 1) >= 5:
            self.laneform_count += 1
            self.laneform_size.append(lane_size+1)
        lane_size = 0
        
        for i in range(len(carstype_1l)):
            j+=1 
            if j < len(carstype_1l) and carstype_1l[i] == carstype_1l[j] == 2:
                lane_size += 1
        if (lane_size + 1) >= 5:
            self.laneform_count += 1
            self.laneform_size.append(lane_size+1)
        lane_size = 0
        
        
        for i in range(len(carstype_2l)):
            j+=1 
            if j < len(carstype_2l) and carstype_2l[i] == carstype_2l[j] == 2:
                lane_size += 1
        if (lane_size + 1) >= 5:
            self.laneform_count += 1
            self.laneform_size.append(lane_size + 1)
        lane_size = 0        
        
        