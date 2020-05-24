# NaSch_CA_Traffic_Flow_Analysis_Software

This repository contains software for multi-agent simulation model of mixed traﬃc ﬂow of connected (HVs) and automated vehicles
(AVs) in python using pygame, matplotlib, numpy, scipy and seaborn libraries. The software is capable of simulating many
different cases of traffic flow and creates data files and figures for the purpose of analysis. Currently I am working on
making the front end of the software more user friendly for potential commercialization.

## CA Traffic Analysis Software

A pygame, numpy and matplotlib based software that lets you create simulation of different traffic flow scenarios using
the concepts of Cellular Automata and perform data analysis and visualization.

### purpose of software:

This software was designed under the supervision of Dr. Jia Li using inspiration from Nagel-Schrekenberg's Cellular Automata Rules for Traffic flow. The software can be used to simulate traffic for many different types of car and traffic situations and record all the important traffic-flow parameters and allows the user to track customized parameters as well. The software also comes with a data analysis and visualization package that helps the user make sense of the data.

### Current Version: 0.2

#### Customization Abilities

The current version of the software deals with simulating heterogeneous traffic flow of Autonomous Vehicles (AVs) and Human-driven Vehicles (HVs) on a three lane circular road. The software has three different models of AVs that is being used in two experiments in a research project led by Dr Li. Through changes in the car.py and road.py files, multiple new models of AVs can be introduced and tested. The software allows simulation traffic with both constant density and increasing density (to generate Fundamental Diagram) the density settings can be changed in simulationManager.py file. 

#### New Version: 0.3 (Work In progress)
The next version will have a GUI enabled customization screen before each simulation and direct analysis features within the same framework.

![GUI1](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/GUI.png)

![GUI2](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/GUI2.png)

![GUI3](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/GUI3.png)

![GUI4](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/GUI4.png)

![GUI5](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/GUI4.png)

![GUI6](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/gui3.png)

### NEW VERSION: 1.0
A version of a reinforced learning algorithm applied to train the av is currently in the works in one of private repository, I plan on making that public as soon as I am done writing a paper using that version. I wanted to include this news in this readme just to inform y'all that reinforced learning regimes can be easily applied on to this framework.

## SUMMARY OF FILES AND DIRECTORIES
The following outlines all the relevant directories and files for the software.

**base directory:** this is the folder where all the directories are found.
- nagel.py
 This code is the initiator of the entire software. It starts the simulation engine running on pygame and returns control to the rest of the program files.
- representation.py
This code is responsible for the visualization of the road, car, and information in the pygame window.
- infodisplayer.py
This code takes data from the back end of the software and displays that information on the pygame window by sending that data to the representation.py file. It also records all the parameters of interest in the text files.
- plot_exp1.py
This code produces all the plots needed for experiment 1 from the raw data text file.
- plot_exp2.py
This code produces all the plots needed for experiment 2 from the raw data text file.
- combined_plot_exp1.py
This code makes plot that needs input from experiment 1 test cases using the raw text data files.
- simulationmanager.py
This code is responsible for updating the traffic flow simulations. It constantly transfers control back and forth from the car.py, road.py, representation.py and infodisplayer.py file.

**"Config" directory:** this directory holds files in charge of road/traffic situations.
- case.py
This file describes the dimensions of the pygame window and the type of road/traffic condition to be simulated.

**simulation directory:** this directory holds files that describe oop code files.
- car.py
This code creates an object called car with certain properties and functions that describes the vehicles behavior.
- road.py
This code creates an object called car with certain properties and functions that describes the vehicles behavior.
- speedlimits.py
This code creates a provision to make traffic lights or damaged road conditions.
- trafficgenerators.py
This code decides how traffic is generated in the simulation.

**"DRAFT_2" DIRECTORY:** It contains all the raw data and results from the simulation experiments.

## INSTALLATION
Install the following libraries in python.
```BASH
pip install numpy 
pip install matplotlib 
pip install pygame
```

## USAGE
To run the simulation in batch mode execute the following command in the base directory.
```python
python3 gameEngine.py batch
```

To run the simulation in gui mode, execute the following command in the base directory.
```python
python3 gameEngine.py gui
```

Use the plot python files and change the directory sturcture for the input files to look at the analysis report of the simulation.

**the next version would resolve this nasty directory change issue. Sorry about this for the time being.**

Example analysis figures:
![FD](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/flux_analysis.png)

# To Do:
- [ ] GUI interface creation
- [ ] FD Creation Mode
- [ ] Full Customization through GUI integration
- [ ] Circular Road Representation
- [ ] Website creation with front end and back end of this software
