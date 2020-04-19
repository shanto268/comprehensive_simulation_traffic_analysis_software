#Only change name
import pygame
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import os
pwd = os.getcwd()

class InfoDisplayer():
    def __init__(self, screen, road, simulationManager,data):
        self.screen = screen
        self.road = road
        self.simulationManager = simulationManager
        self.string = ''
        self.cells = road.getCellCount()
        self.timeFactor = 0
        self.font = pygame.font.SysFont("monospace", 15)
        self.keysInfo = "Space - pause, M - 2x faster, N - 2x slower, S - step, D - 500 steps"
        self.text = [self.keysInfo]
        self.renderLabels()
        self.data = data

    def renderLabels(self):
        self.labels = list(map(lambda x: self.font.render(x, 1, (255, 255, 0)), self.text))
        
    def update(self):
        totalCars, avgSpeed = self.road.getAvgCarSpeed() #total number of cars, average speed overall
        totalAV, AVspeed = self.road.fdav()
        totalRV, RVspeed = self.road.fdrv()
        carNum = self.road.carCount() #total number of cars
        carnum = self.road.carcount()
        deadCars = self.road.deadCars #CARS leaving the screen
        updates = self.road.updates #updates
        netAV = self.road.av 
        freq = self.road.freqAV
      #  L0 = self.road.L0c
        cluster_num = 10                        #needs work
        cluster_size = 10                       #needs work
        numlanechng = self.road.lanechange #number of lane changes 
        avlane = self.road.avlane
        rvlane = self.road.rvlane                                                                                                    # newtotalCars, newavgSpeed = self.getAvgCarSpeedincoming()
        congestion = totalCars*100/self.cells #density * 100
        density = carNum/self.cells #total density
        densityrv = totalRV/self.cells
        densityav = totalAV/self.cells
        flowrv = RVspeed*densityrv
        flowav = AVspeed*densityav
        flow =avgSpeed*density #total flow
        inflow = self.road.amount
        newflow = self.road.vcount / 300
        speed = self.road.avg
        lane_form_count = self.road.laneform_count
        cluster = self.road.clunum
        lane_size = self.road.laneform_size
        avgclus = self.road.avgclus
        av = self.road.avee
        if inflow == 0:
            avprop = 0
        else: avprop = (av / inflow) * 100
        trigpoint = self.road.triggerbin
        if carNum != 0:
            car_in_clus = self.road.cluster_num_car / carNum  #SAS new 2020
        else:
            car_in_clus = -1 #SAS new 2020
        
        text = [self.text[0]]
       # text.append("LO: " + str(L0))
        text.append("P(AV-AV): " + str(freq))
        text.append("Updates: " + str(updates))
        text.append("Total Car count: " + str(carNum))
        text.append("Average size of cluster: " + str(avgclus))
        text.append("Number of self organized cluster formation: " + str(cluster))
       # text.append("AV inflow: " + str(totalAV))
       # text.append("AV speed: " + str(AVspeed))
       # text.append("Proportion of AV: {:0.2f} %".format(avprop))
   #     text.append("Proportion of AV(inflow): {:0.2f} %".format(lanecontrol)) #include percentage for AV as num(AV)/carNum * 100
      #  text.append("Congestion: " + str(congestion))
   #     text.append("Proportion of AV(overall): {:0.2f} %".format(prop_av)) #include percentage for AV as num(AV)/carNum * 100
       # text.append("Dead cars: " + str(deadCars))
        text.append("AV number: "+ str(netAV))
        text.append("Avg speed: {:0.3f}".format(avgSpeed, deadCars))
       # text.append("Avg speed: {:0.3f}".format(newavgSpeed, deadCars))
        text.append("Flow: {:0.3f}".format(flow))
    #    text.append("Flow new: {:0.3f}".format(newflow))
    #    text.append("Control Speed: {:0.3f}".format(speed))
        text.append("Density: {:0.3f}".format(density))
        #text.append("Density: {:0.3f}".format(newdensity))
        text.append("Total Lane changes: " + str(numlanechng))
        text.append("AV Total Lane changes: " + str(avlane))
        text.append("RV Total Lane changes: " + str(rvlane))
        text.append("Clusterability: " + str(car_in_clus))
      #  if trigpoint == 1:
      #      text.append("Control status: on" )
      #  else:
      #      text.append("Control status: off" )
        text.append('')
        text.append(self.keysInfo)
        xs = " " 
        text.append(str(328*xs) + " Made with the support and guidance of Dr. Jia Li")
        text.append(str(316*xs) + "  By Sadman Ahmed Shanto, Undergraduate Researcher")
        text.append(str(298*xs) + " Texas Tech Multidisciplinary Research in Transportation(TechMRT)")
        self.text = text
        self.renderLabels()
              
        """ name change of filea and comments on filen    
        
        name1 = "draft_2/experiment_1/data_files/low_dens_oppo.txt"
        name2 = "draft_2/experiment_1/data_files/low_dens_aware.txt"
        name2a = "draft_2/experiment_1/data_files/low_dens_aware_oppo.txt"
        name3 = "draft_2/experiment_1/data_files/low_dens_base_hv_like.txt"
        name3a = "draft_2/experiment_1/data_files/low_dens_base_hv_hway.txt"
        
        name4 = "draft_2/experiment_1/data_files/crit_dens_oppo.txt"
        name5 = "draft_2/experiment_1/data_files/crit_dens_aware.txt"
        name5a = "draft_2/experiment_1/data_files/crit_dens_aware_oppo.txt"
        name6 = "draft_2/experiment_1/data_files/crit_dens_base_hv_like.txt"
        name6a = "draft_2/experiment_1/data_files/crit_dens_base_hv_hway.txt"
        
        name7 = "draft_2/experiment_1/data_files/high_dens_oppo.txt"
        name8 = "draft_2/experiment_1/data_files/high_dens_aware.txt"
        name8a = "draft_2/experiment_1/data_files/high_dens_aware_oppo.txt"
        name9 = "draft_2/experiment_1/data_files/high_dens_base_hv_like.txt"
        name9a = "draft_2/experiment_1/data_files/high_dens_base_hv_hway.txt"
        
        namea = "draft_2/experiment_2/data_files/fd_oppo.txt"
        nameb = "draft_2/experiment_2/data_files/fd_aware.txt"
        nameba = "draft_2/experiment_2/data_files/fd_aware_oppo.txt"
        namec = "draft_2/experiment_2/data_files/fd_base_hv_like.txt"
        nameca = "draft_2/experiment_1/data_files/fd_base_hv_hway.txt"
        
        namei = "draft_2/experiment_1/data_files/mid_dens_oppo.txt"
        nameii = "draft_2/experiment_1/data_files/mid_dens_aware.txt"
        nameii = "draft_2/experiment_1/data_files/mid_dens_aware_oppo.txt"
        nameiii = "draft_2/experiment_1/data_files/mid_dens_base_hv_like.txt"
        nameiiia = "draft_2/experiment_1/data_files/mid_dens_base_hv_hway.txt"
        """
        
        name = "results/" + str(self.data[0])  #SAS 2020 Update: change 1 for exp 1 and 2 for exp 2
                
       # file1 = open(name,"a+")            
       # file1.write(str(density) + ", " + str(flow) + ","  + str(updates)  + ", "  + str(densityrv)  + ", "   + str(flowrv)  + ", "  + str(densityav)  + ", " + str(flowav)  + ", "   + str(cluster) + ", " + str(avgclus) + ", " + str(freq) + ", " + str(numlanechng) + ", " + str(avlane) + ", " + str(rvlane)+ ", " + str(car_in_clus) + "\n")                             
       # file1.close()


      
    def updateSpeed(self):
        if len(self.text) == 0: return
        if self.timeFactor != self.simulationManager.timeFactor:
            self.timeFactor = self.simulationManager.timeFactor
            self.text[0] = "Frame speed: {0}x".format(self.timeFactor)
            self.renderLabels()

    def draw(self): #draws comments
        self.updateSpeed()
        y = self.screen.get_height() - 300
        for label in self.labels:
            self.screen.blit(label, (20, y))
            y += 20
                  
    
        
