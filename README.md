# NaSch_CA_Traffic_Flow_Analysis_Software

This repository contains software for multi-agent simulation model of mixed traﬃc ﬂow of connected (HVs) and automated vehicles
(AVs) in Python using pygame, matplotlib, numpy, scipy and seaborn libraries. The software is capable of simulating many
different cases of traffic flow and creates data files and figures for the purpose of analysis. Currently I am working on
making the front end of the software more user friendly for potential commercialization.

## CA Traffic Analysis Software

A pygame, numpy and matplotlib based software that lets you create simulation of different traffic flow scenarios using
the concepts of Cellular Automata and perform data analysis and visualization.

### Purpose of software:

This software was designed under the supervision of Dr. Jia Li using inspiration from Nagel-Schrekenberg's Cellular Automata Rules for Traffic flow. The software can be used to simulate traffic for many different types of car and traffic situations and record all the important traffic-flow parameters and allows the user to track customized parameters as well. The software also comes with a data analysis and visualization package that helps the user make sense of the data.

### Current Version: 0.2

#### Customization Abilities

The current version of the software deals with simulating heterogeneous traffic flow of Autonomous Vehicles (AVs) and Human-driven Vehicles (HVs) on a three lane circular road. The software has three different models of AVs that is being used in two experiments in a research project led by Dr Li. Through changes in the car.py and road.py files, multiple new models of AVs can be introduced and tested. The software allows simulation traffic with both constant density and increasing density (to generate Fundamental Diagram) the density settings can be changed in simulationManager.py file. 

#### New Version: 0.3 (Work In Progress)
The next version will have a GUI enabled customization screen before each simulation and direct analysis features within the same framework.

![GUI1](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/GUI.png)

![GUI2](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/GUI2.png)

![GUI3](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/GUI3.png)

#![GUI4](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/GUI4.png)

![GUI5](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/GUI4.png)

![GUI6](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/gui3.png)

### NEW VERSION: 1.0
A VERSION OF A REINFORCED LEARNING ALGORITHM APPLIED TO TRAIN THE AV IS CURRENTLY IN THE WORKS IN ONE OF PRIVATE REPOSITORY, I PLAN ON MAKING THAT PUBLIC AS SOON AS I AM DONE WRITING A PAPER USING THAT VERSION. I WANTED TO INCLUDE THIS NEWS IN THIS README JUST TO INFORM Y'ALL THAT REINFORCED LEARNING REGIMES CAN BE EASILY APPLIED ON TO THIS FRAMEWORK.

## SUMMARY OF FILES AND DIRECTORIES
THE FOLLOWING OUTLINES ALL THE RELEVANT DIRECTORIES AND FILES FOR THE SOFTWARE.

**BASE DIRECTORY:** THIS IS THE FOLDER WHERE ALL THE DIRECTORIES ARE FOUND.
- NAGEL.PY
 THIS CODE IS THE INITIATOR OF THE ENTIRE SOFTWARE. IT STARTS THE SIMULATION ENGINE RUNNING ON PYGAME AND RETURNS CONTROL TO THE REST OF THE PROGRAM FILES.
- REPRESENTATION.PY
THIS CODE IS RESPONSIBLE FOR THE VISUALIZATION OF THE ROAD, CAR, AND INFORMATION IN THE PYGAME WINDOW.
- INFODISPLAYER.PY
THIS CODE TAKES DATA FROM THE BACK END OF THE SOFTWARE AND DISPLAYS THAT INFORMATION ON THE PYGAME WINDOW BY SENDING THAT DATA TO THE REPRESENTATION.PY FILE. IT ALSO RECORDS ALL THE PARAMETERS OF INTEREST IN THE TEXT FILES.
- PLOT_EXP1.PY
THIS CODE PRODUCES ALL THE PLOTS NEEDED FOR EXPERIMENT 1 FROM THE RAW DATA TEXT FILE.
- PLOT_EXP2.PY
THIS CODE PRODUCES ALL THE PLOTS NEEDED FOR EXPERIMENT 2 FROM THE RAW DATA TEXT FILE.
- COMBINED_PLOT_EXP1.PY
THIS CODE MAKES PLOT THAT NEEDS INPUT FROM EXPERIMENT 1 TEST CASES USING THE RAW TEXT DATA FILES.
- SIMULATIONMANAGER.PY
THIS CODE IS RESPONSIBLE FOR UPDATING THE TRAFFIC FLOW SIMULATIONS. IT CONSTANTLY TRANSFERS CONTROL BACK AND FORTH FROM THE CAR.PY, ROAD.PY, REPRESENTATION.PY AND INFODISPLAYER.PY FILE.

**"CONFIG" DIRECTORY:** THIS DIRECTORY HOLDS FILES IN CHARGE OF ROAD/TRAFFIC SITUATIONS.
- CASE.PY
THIS FILE DESCRIBES THE DIMENSIONS OF THE PYGAME WINDOW AND THE TYPE OF ROAD/TRAFFIC CONDITION TO BE SIMULATED.

**SIMULATION DIRECTORY:** THIS DIRECTORY HOLDS FILES THAT DESCRIBE OOP CODE FILES.
- CAR.PY
THIS CODE CREATES AN OBJECT CALLED CAR WITH CERTAIN PROPERTIES AND FUNCTIONS THAT DESCRIBES THE VEHICLES BEHAVIOR.
- ROAD.PY
THIS CODE CREATES AN OBJECT CALLED ROAD WITH CERTAIN PROPERTIES AND FUNCTIONS THAT DESCRIBES THE RULES THAT VEHICLES INTERACTING WITH THE ROAD SHOULD ABIDE BY.
- SPEEDLIMITS.PY
THIS CODE CREATES A PROVISION TO MAKE TRAFFIC LIGHTS OR DAMAGED ROAD CONDITIONS.
- TRAFFICGENERATORS.PY
THIS CODE DECIDES HOW TRAFFIC IS GENERATED IN THE SIMULATION.

**"DRAFT_2" DIRECTORY:** IT CONTAINS ALL THE RAW DATA AND RESULTS FROM THE SIMULATION EXPERIMENTS.

## INSTALLATION
INSTALL THE FOLLOWING LIBRARIES FOR PYTHON.
```BASH
PIP INSTALL NUMPY
PIP INSTALL MATPLOTLIB 
PIP INSTALL PYGAME
```

## USAGE

TO RUN THE SIMULATION IN BATCH MODE EXECUTE THE FOLLOWING COMMAND IN THE BASE DIRECTORY.
```PYTHON
PYTHON3 GAMEENGINE.PY BATCH
```

TO RUN THE SIMULATION IN GUI MODE, EXECUTE THE FOLLOWING COMMAND IN THE BASE DIRECTORY.
```PYTHON
PYTHON3 GAMEENGINE.PY GUI
```

USE THE PLOT PYTHON FILES AND CHANGE THE DIRECTORY STURCTURE FOR THE INPUT FILES TO LOOK AT THE ANALYSIS REPORT OF THE SIMULATION.
**THE NEXT VERSION WOULD RESOLVE THIS NASTY DIRECTORY CHANGE ISSUE. SORRY ABOUT THIS FOR THE TIME BEING.** 

Example analysis figures:
![FD](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/flux_analysis.png)


