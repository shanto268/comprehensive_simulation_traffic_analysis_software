"""
Need to do:
    Code for changing the .py files
    Having default values for the inputs saved and returned after running the sim
    Fixing the directiry issues
    Linking the code bug free
    Include analysis reports direct from the GUI
    Include different scenarios in the GUI for sim and ana
"""
#important libraries
from tkinter import *
import os

c1 = True
tot_sim_time = 1500
sim_time_update = 100
arr = [] #stores all info

base_dir = "/Users/sshanto/techmrt/Python_new/"
cmd1 = "cd " + base_dir
cmd = "ls "
cmd2 = "python nagel.py config.case"
chdir1 = r"/Users/sshanto/techmrt/Python_new/"

#key down functions:

def check():
    #if all data fields are accurately field, disable the button and create run simulation button
    b2["state"] = "disabled"
    Label (window, text="Inputs compiled successfully!", bg="snow3", fg="blue", font="none 15").grid(row=9,column=0,columnspan=3)
    b3 = Button(window, text="RUN SIMULATION", width=15, command=click, fg="red")
    b3.grid(row=10,column=1,sticky=NE, columnspan=4)
    
def click():
    #purpose: run sim and create new button asking for analysis of plots 
    nlanes = float(t1.get())
    ncell = float(t7.get())
    ncars = float(t2.get())
    avpercent = float(t3.get())
    if c1 == False:
        nsim = float(t5.get())
        nsim_update = float(t6.get())
    else:
        nsim = tot_sim_time
        nsim_update = sim_time_update
   # arr.append(nlanes, ncars, avpercent, nsim, nsim_update)
    os.chdir(chdir1)
    os.system(cmd)
    os.system(cmd2)
    b1["row"] = 11
    Label(window, text="     ", bg="snow3", fg="snow3").grid(row=12,column=0, columnspan = 3)
    Label(window, text="     ", bg="snow3", fg="snow3").grid(row=13,column=0, columnspan = 3)
    lc1["row"] = 14
    b4 = Button(window, text="CREATE ANALYSIS PLOTS", width=20, command=click, fg="red")
    b3.grid(row=10,column=0,sticky=NE, columnspan=3)
   # l1 = Label(window, text=str(int(etext1)+int(etext2)),bg="snow3", fg="black", font="none 12").grid(row=5,column=0,sticky=W)

def close():
    window.destroy()
    exit()

def Select_model(m):
    return m

def density(i):
    window.geometry("725x350")
    x = " "
    text_l = "Enter the total simulation run time: " + str(64*x)
    text_r = "Enter the simulation run time after which the density will update (period): "
    if i == 1:
        c1 = False
        l5 = Label(window, text=text_l, bg="snow3", fg="black", font="none 15").grid(row=7,column=0,sticky=W)
        t5 = Entry(window, width=5, bg="white", borderwidth=3)
        t5.grid(row=7, column=2,sticky=NE)
        l2 = Label (window, text="Enter the total number of cars: "+str(30*x), bg="snow3", fg="black", font="none 15").grid(row=8,column=0,sticky=W)
        t2 = Entry(window, width=5, bg="white", borderwidth=3)
        t2.grid(row=8, column=2,sticky=NE)
    elif i == 2:
        c1 = False
        l5 = Label(window, text=text_r, bg="snow3", fg="black", font="none 15").grid(row=7,column=0,sticky=W)
        t6 = Entry(window, width=5, bg="white", borderwidth=3)
        t6.grid(row=7, column=2,sticky=NE)
        lvi = Label(window, text="Enter the amount of cars to be added per period ", bg="snow3", fg="black", font="none 15").grid(row=8,column=0,sticky=W)
        t7 = Entry(window, width=5, bg="white", borderwidth=3)
        t7.grid(row=8, column=2,sticky=NE)
        
        
def scroll_av(s):
  if s=="neigbor aware":
    one=Label(window,text="Type Aware",width=12, fg="red")
   # one.grid(column=1,row=4)
  if s=="opportunistic":
    two=Label(window,text="Type Unware",width=12, fg="blue")
   # two.grid(column=1,row=4)        
  if s=="base scenario - HV":
    three=Label(window,text="HV Model",width=12, fg="green")
   # three.grid(column=1,row=4)  

#main functions
window = Tk()
window.title("NaSch CA Traffic Analysis Software")
window.configure(background="snow3")


#Entering pictures
background_image = PhotoImage(file="/Users/sshanto/techmrt/Python_new/paper_draft/draft/fd1.png")

 
#create label
l1 = Label(window, text="Enter the number of lanes: ", bg="snow3", fg="black", font="none 15").grid(row=0,column=0,sticky=W)
t1 = Entry(window, width=5, bg="white", borderwidth=3)
t1.grid(row=0, column=2,sticky=NE, columnspan=4)

l3 = Label (window, text="Enter the percentage of AV: ", bg="snow3", fg="black", font="none 15").grid(row=3,column=0,sticky=W)
t3 = Entry(window, width=5, bg="white", borderwidth=3)
t3.grid(row=3, column=2,sticky=NE)

l4 = Label (window, text="Select an AV model: ", bg="snow3", fg="black", font="none 15").grid(row=4,column=0,sticky=W)
init_opt=StringVar(window)
init_opt.set("Select ...")
av1=OptionMenu(window,init_opt,"neigbor aware","opportunistic","base scenario - HV",command=scroll_av)
av1.grid(column=2,row=4,sticky=NE)


l5 = Label (window, text="System Density: ", bg="snow3", fg="black", font="none 15").grid(row=6,column=0,sticky=W)
o1 = Button(window, text="CONSTANT", width=10, command=lambda i = 1: density(i), fg="red").grid(row=6,column=1,sticky=NE)
o2 = Button(window, text="INCREASING", width=12, command=lambda i = 2: density(i), fg="blue").grid(row=6,column=2,sticky=NE)


Label(window, text="     ", bg="snow3", fg="snow3").grid(row=8,column=0, columnspan = 3)
Label(window, text="     ", bg="snow3", fg="snow3").grid(row=9,column=0, columnspan = 3)
Label(window, text="     ", bg="snow3", fg="snow3").grid(row=11,column=0, columnspan = 3)
lc1 = Label(window, text="Made by Sadman Ahmed Shanto © 2019", bg="snow3", fg="black")
lc1.grid(row=13,column=0, columnspan = 3)


#buttons
b1 = Button(window, text="EXIT", width=6, command=close, fg="red")
b1.grid(row=10,column=0,sticky=NW,padx=10)
b2 = Button(window, text="SUBMIT", width=10, command=check, fg="green")
b2.grid(row=10,column=2)

#picture insertion
#Label(window, image=var, bg = "snow3").grid(row=9, column=2)
 
#run the main loop
window.mainloop()


