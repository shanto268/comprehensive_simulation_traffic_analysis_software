# No selective headway case
from config.case import *
import random

#constants 
max_hv = int(data[5])  #SAS 2020
max_av_av = int(data[3])  #SAS 2020
max_av_hv = int(data[2])  #SAS 2020
limitCycle = int(data[11])*100 #SAS 2020

class Car:
    #LOOK INTO UPDATE X CODES --> UPDATE LANE --> ROAD.PY
    laneChangeProbability = 0
    slowDownProbability = 0
    lanetotup = []    #saves all the lane changes --> sum returns total number of lane changes
    L0 = []
    laneAv =  []      #saves all av lane changes --> sum returns av total number of lane changes
    
    def __init__(self, road, pos, velocity = 0, vtype = 0, seen = False):   #track function that updates velocity and use that as vtype
        self.velocity = velocity
        self.road = road
        self.pos = pos
        self.prevPos = pos
        self.vtype = vtype #vtype = 1 HV ; VTYPE = 2 AV
        self.time = 0
        self.lanechngup = 0
        self.lanechngdwn = 0
        self.lanechngavup = 0
        self.lanechngavdwn = 0
        self.lanechngL0 = 0
        self.contspeed = 3
        self.contprop = 30
        self.seen = seen 
        self.count = 0   #counting number of cars
        self.clusternum = 0 #number of clusters > 3
        self.clustersize = 0 #size of clusters
        self.freq = 0
        self.freqtot = 0
        self.CAVdist = 0
        self.terminate = False # SAS 2020
        self.numer = 0  #P(lanechange) = numer / denumer 2020
        self.denumer = 0 #SAS 2020

    def cluster(self):
        if self.seen == False:
            if self.vtype == 2 and self.road.ncvtype2(self.pos) == 2 and self.road.distanceToNextThing(self.pos) < 5:
                self.count += 1
            #    print(self.count)
        
            
    def cluster_loop(self):
        if self.seen == False:
            if self.vtype == 2 and self.road.ncvtype1(self.pos) == 2 and self.road.dton(self.pos) < 5 :
                self.count += 1
             #   print(self.count)

    def updateLane(self):
        self.prevPos = self.pos
        if self.vtype == 1: Car.laneChangeProbability = (1 -float(data[7]))  #SAS 2020
        else: Car.laneChangeProbability = (1 - float(data[6]))  #SAS 2020
        self.updateLaneLogic()
        return self.pos    
    
    def lanecountup(self):
        self.lanechngup += 1
        Car.lanetotup.append(self.lanechngup)
        if self.vtype == 2:
            self.lanechngavup += 1
            Car.laneAv.append(self.lanechngavup)
            
    def lanecountdwn(self):
        self.lanechngdwn += 1
        Car.lanetotup.append(self.lanechngdwn)
        if self.vtype == 2:
            self.lanechngavdwn += 1
            Car.laneAv.append(self.lanechngavdwn)
       
    def lanecountL0(self):
        self.lanechngL0 += 1
        Car.L0.append(self.lanechngL0)
    
    
    def updateLaneLogic(self):
        if self.willingToChangeUp():
            self.denumer += 1
            x = random.random()
            if x >= Car.laneChangeProbability:
                self.numer +=1
                self.lanecountup()
                self.pos = self.pos[0], self.pos[1]-1
        elif self.willingToChangeDown():
            self.denumer += 1
            y = random.random()
            if y >= Car.laneChangeProbability:
                self.numer +=1
                self.lanecountdwn()
                self.pos = self.pos[0], self.pos[1]+1
                if self.pos[1] == 2:
                    self.lanecountL0()
        if self.denumer != 0 and self.vtype == 2: #SAS 2020
            print("P(lc): " + str(float(self.numer /self.denumer)))
    ''' new code '''
    def dynamicupdateLane(self):
        self.prevPos = self.pos
        if self.vtype == 1: Car.laneChangeProbability = (1 -float(data[7]))  #SAS 2020 
        else: Car.laneChangeProbability = (1 -float(data[6]))  #SAS 2020
        if True: #dedicated case
      #  if self.trigger1() and self.trigger2():  #dynamic case
     #   if self.trigger2():  #dynamic case
            #'''RV case'''    
            self.road.triggerplot1()
            if self.vtype == 1 and self.pos[1] == 2: #lane 2
                if self._safetycheck(self.pos[1],self.pos[1]-1):
                    self.lanecountup()
                    self.pos = self.pos[0], self.pos[1]-1          
                elif self.willingToChangeDown():
                    y = random.random()
                    if y >= Car.laneChangeProbability:
                        self.lanecountdwn()
                        self.pos = self.pos[0], self.pos[1]+1
                        
            elif self.vtype == 1 and self.pos[1] == 1: #lane 1
                if self.willingToChangeUp():
                    x = random.random()
                    if x >= Car.laneChangeProbability:
                        self.lanecountup()
                        self.pos = self.pos[0], self.pos[1]-1
                elif self.willingToChangeDown():
                    y = random.random()
                    if y >= 2: #not a possibility #include slowing down instead 
                        self.lanecountdwn()
                        self.pos = self.pos[0], self.pos[1]+1 
                        if self.pos[1] == 2:
                            self.lanecountL0()
                
            elif self.vtype == 1 and self.pos[1] == 0: #lane 0
                if self.willingToChangeUp():
                    x = random.random()
                    if x >= Car.laneChangeProbability:
                        self.lanecountup()
                        self.pos = self.pos[0], self.pos[1]-1
                elif self.willingToChangeDown():
                    y = random.random()
                    if y >= Car.laneChangeProbability:
                        self.lanecountdwn()
                        self.pos = self.pos[0], self.pos[1]+1
    #'''AV case'''                
            elif self.vtype == 2 and self.pos[1] == 2: #lane 2
                self.pos = self.pos[0], self.pos[1]   
                if self.willingToChangeUp():
                    x = random.random()
                    if x >= Car.laneChangeProbability:
                        self.lanecountup()
                        self.pos = self.pos[0], self.pos[1]-1
                elif self.willingToChangeDown():
                    y = random.random()
                    if y >= Car.laneChangeProbability:
                        self.lanecountdwn()
                        self.pos = self.pos[0], self.pos[1]+1
                
            elif self.vtype == 2 and self.pos[1] == 1: #lane 1
                if self.willingToChangeUp():
                    x = random.random()
                    if x >= Car.laneChangeProbability:
                        self.lanecountup()
                        self.pos = self.pos[0], self.pos[1]-1
                elif self.willingToChangeDown():
                    y = random.random()
                    if y >= Car.laneChangeProbability:
                        self.lanecountdwn()
                        self.pos = self.pos[0], self.pos[1]+1     
                        if self.pos[1] == 2:
                            self.lanecountL0()
                            
            elif self.vtype == 2 and self.pos[1] == 0: #lane 0
                if self.willingToChangeUp():
                    x = random.random()
                    if x >= Car.laneChangeProbability:
                        self.lanecountup()
                        self.pos = self.pos[0], self.pos[1]-1
                elif self.willingToChangeDown():
                    y = random.random()
                    if y >= Car.laneChangeProbability:
                        self.lanecountdwn()
                        self.pos = self.pos[0], self.pos[1]+1  
                        
            
            return self.pos     
        else:
            self.road.triggerplot2()
            self.updateLaneLogic()          #Or self.updateLane() --> Case for regular heteregeneous flow
            
            return self.pos

    def trigger1(self):
        if ((self.road.avee / self.road.amount) * 100) >= 15:
            return True
        else: return False
    
    def trigger2(self): #avgspeed < 5 static dynamic lane
        if self.road.avg <= 1.5 :
            return True
        else: return False
     
    ''' end code '''
    def feedlaneroadpy(self):
        return sum(Car.lanetotup)
    
    def feedav(self):
        return sum(Car.laneAv)
    
    def feedlaneroadLO(self):
        return sum(Car.L0)
    
    def _updateX(self):
        self.velocity = self.calcNewVelocity()

        if self.velocity > 0 and random.random() <= Car.slowDownProbability:
            self.velocity -= 1

        self.pos = self.pos[0] + self.velocity, self.pos[1]
        if (self.pos[0] + self.velocity) >= self.road.getLength():
                self.pos = (self.pos[0] + self.velocity) % self.road.getLength(), self.pos[1]
        return self.pos
           
    def didAVfinish(self,moved):    
        self.CAVdist += moved
        if (self.CAVdist < limitCycle):
                self.terminate = False
        else:
                self.terminate = True

    def updateX(self): #stochastic slowing down
     #   print(self.vlead(self.pos))      
    #    print(self.road.ncvtype(self.pos))
        if self.vtype == 1: Car.slowDownProbability = float(data[9]) #SAS 2020
        else: Car.slowDownProbability = float(data[8]) #SAS 2020
        if self.pos[0] < (self.road.getLength() - 5) and self.pos[0] >= 0:
            self.velocity = self.calcNewVelocity()
            self.cluster()   # need to use distancetonextthing                                                                  
            if self.velocity > 0 and random.random() <= Car.slowDownProbability:
                self.velocity -= 1
            self.pos = self.pos[0] + self.velocity, self.pos[1] 
            if self.vtype == 2:
                self.didAVfinish(self.velocity) #SAS new Add 2020
        elif self.pos[0] < self.road.getLength() and self.pos[0] >= (self.road.getLength() - 5):
            self.velocity = self.newvelocity()
            self.cluster_loop()    #need to use d2n
            if self.velocity > 0 and random.random() <= Car.slowDownProbability:
                self.velocity -= 1
            if (self.pos[0] + self.velocity) >= self.road.getLength():
                self.pos = (self.pos[0] + self.velocity) % self.road.getLength(), self.pos[1]
            else:
                self.pos = self.pos[0] + self.velocity, self.pos[1]
            if self.vtype == 2:
                self.didAVfinish(self.velocity) #SAS new add 2020
        return self.pos    

    def newvelocity(self): 
        return min(self.velocity + 1, self.road.d2n(self.pos), self.v1leadcopy(self.pos),self.maxSpeedofVehicle()) #regular v (M2)
       # return min(self.velocity + 1, self.road.d2n(self.pos), self.v1lead(self.pos)) # M1

    def calcNewVelocity(self):
        return min(self.velocity + 1, self.road.getMaxSpeedAt(self.pos), self.v2leadcopy(self.pos),self.maxSpeedofVehicle()) #regular v  (M2)
       # return min(self.velocity + 1, self.road.getMaxSpeedAt(self.pos), self.v2lead(self.pos)) # M1
    
    def maxSpeedofVehicle(self): #SAS new update 2020
        if self.vtype == 1:
            return max_hv
        else:
            return max_av_av
        
    def v2lead(self, pos): #regular case
        if self.vtype == 1: #RV
            self.freqtot += 1
            return 3
        elif self.vtype == 2: #AV
            if self.road.ncvtype2(self.pos) == 1: #AV - RV -->
                self.freqtot += 1
                return 4
            elif self.road.ncvtype2(self.pos) == 2: #AV - AV -->
                self.freqtot += 1
                self.freq += 1
                return 5
            else:
                return self.road.ncvtype2(self.pos)
            
    def v1lead(self, pos):  #looping boundary case
        if self.vtype == 1: #RV
            self.freqtot += 1
            return 3
        elif self.vtype == 2: #AV
            if self.road.ncvtype1(self.pos) == 1: #AV - RV -->
                self.freqtot += 1
                return 4
            elif self.road.ncvtype1(self.pos) == 2: #AV - AV -->
                self.freqtot += 1
                self.freq += 1
                return 5
            else:
                return self.road.ncvtype1(self.pos)
            
    
    def v2leadcopy(self, pos): #regular case
        if self.vtype == 1: #RV
            self.freqtot += 1
            return 300
        elif self.vtype == 2: #AV
            if self.road.ncvtype2(self.pos) == 1: #AV - RV -->
                self.freqtot += 1
                return 400
            elif self.road.ncvtype2(self.pos) == 2: #AV - AV -->
                self.freqtot += 1
                self.freq += 1
                return 500
            else:
                return 500
            
    def v1leadcopy(self, pos):  #looping boundary case
        if self.vtype == 1: #RV
            self.freqtot += 1
            return 300
        elif self.vtype == 2: #AV
            if self.road.ncvtype1(self.pos) == 1: #AV - RV -->
                self.freqtot += 1
                return 400
            elif self.road.ncvtype1(self.pos) == 2: #AV - AV -->
                self.freqtot += 1
                self.freq += 1
                return 500
            else:
                return 500        

    def willingToChangeUp(self):
        return self.road.possibleLaneChangeUp(self.pos) and self.__willingToChangeLane(self.pos[1], self.pos[1] - 1)
    
    def willingToChangeDown(self):
        return self.road.possibleLaneChangeDown(self.pos) and self.__willingToChangeLane(self.pos[1], self.pos[1] + 1)
    #regular 

    def __willingToChangeLane(self, sourceLane, destLane):                           
        srcLaneSpeed =  self.road.getMaxSpeedAt( (self.pos[0], sourceLane) )  #gets max speed at sourcelane
        destLaneSpeed =  self.road.getMaxSpeedAt( (self.pos[0], destLane) )#gets max speed at destlane
        if destLaneSpeed <= srcLaneSpeed: return False #no incentive
        prevCar = self.road.findPrevCar( (self.pos[0], destLane) )  #NaSch lane change rule safety
        if prevCar == None: return True #safety check 1
        else:
            distanceToPrevCar = self.pos[0] - prevCar.pos[0] #safety check 2
            return distanceToPrevCar > prevCar.velocity #True only if no collision
           
    
    def _safetycheck(self,sourceLane, destLane):
        prevCar = self.road.findPrevCar( (self.pos[0], destLane) )  #NaSch lane change rule safety
        if prevCar == None: return True #safety check 1
        else:
            distanceToPrevCar = self.pos[0] - prevCar.pos[0] #safety check 1
            return distanceToPrevCar > prevCar.velocity
        
    
    def dyn_willingToChangeUp(self):
        return self.road.dyn_possibleLaneChangeUp(self.pos) and self.dyn__willingToChangeLane(self.pos[1], self.pos[1] - 1)
    
    def dyn_willingToChangeDown(self):
        return self.road.dyn_possibleLaneChangeDown(self.pos) and self.dyn__willingToChangeLane(self.pos[1], self.pos[1] + 1)
    
    def dyn__willingToChangeLane(self, sourceLane, destLane):                          
        srcLaneSpeed = self.road.getMaxSpeedAt( (self.pos[0], sourceLane) ) #gets speed
        destLaneSpeed = self.road.getMaxSpeedAt( (self.pos[0], destLane) ) #gets speed
        if destLaneSpeed <= srcLaneSpeed or destLane == 0: return False #no incentive
        prevCar = self.road.findPrevCar( (self.pos[0], destLane) )  #NaSch lane change rule safety
        if prevCar == None: return True #safety check 1
        else:
            distanceToPrevCar = self.pos[0] - prevCar.pos[0] #safety check 1
            return distanceToPrevCar > prevCar.velocity #True only if no collision    
        
    def dynav_willingToChangeUp(self):
        return self.road.dynav_possibleLaneChangeUp(self.pos) and self.dynav__willingToChangeLane(self.pos[1], self.pos[1] - 1)
    
    def dynav_willingToChangeDown(self):
        return self.road.dynav_possibleLaneChangeDown(self.pos) and self.dynav__willingToChangeLane(self.pos[1], self.pos[1] + 1)
    
    def dynav__willingToChangeLane(self, sourceLane, destLane):                          
        srcLaneSpeed = self.road.getMaxSpeedAt( (self.pos[0], sourceLane) ) #gets speed
        destLaneSpeed = self.road.getMaxSpeedAt( (self.pos[0], destLane) ) #gets speed
        if destLaneSpeed <= srcLaneSpeed: return False #no incentive --> Might need to change this
        prevCar = self.road.findPrevCar( (self.pos[0], destLane) )  #NaSch lane change rule safety
        if prevCar == None or destLane == 0: return True #safety check 1
        else:
            distanceToPrevCar = self.pos[0] - prevCar.pos[0] #safety check 1
            return distanceToPrevCar > prevCar.velocity #True only if no collision
    
    
    
