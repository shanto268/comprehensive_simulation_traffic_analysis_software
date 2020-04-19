#Usage of code python3 nagel.py name_of_data_text_file.txt number_of_cars max_speed
# $1 = rawdata.txt
# $2 = number of cars
# $3 = max speed on the road
# $4 = max speed of AV (AV-AV)
# $5 = AV-HV speed
# $6 = max speed of HV 
# $7 = Probability of lane change of AV
# $8 = Probability of lane change of HV
# $9 = Probability of braking of AV
# $10 = Probability of braking of HV
# $11 = Number of AVs
# $12 = Limit Cycle
#           NOT IMPLEMENTED YET
# ~~~~~~~~~~~~~~~~~ Optional ~~~~~~~~~~~~~~~~
# $13 = Probability of AV
# $14 = Number of lanes
# $15 = Number of Cells in a lane
# $16 = Simulation time
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#change car.py
cd simulation
mv car_nh.py car.py
cd ..

#different density simulations
echo "The initial AV model is Base Scenario (HV Like)"
echo Numbers of vehicles in simulation is $2
python3 nagel.py trial.txt 100 5 3 3 3 0.6 0.6 0.4 0.4 1 10
echo Simultation is complete!

#change back car files
cd simulation
mv car.py car_nh.py
cd ..

#echo Executing analysis files now....
# execute plot files
#echo Analysis plots created!

