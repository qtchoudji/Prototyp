
"""--------------------------------------------------------------------------------------------------"""
"""--------------------------Simulation of collision ----------------------------------------------- """
"""--------------------------------------------------------------------------------------------------"""



import traci
import traci.constants as tc

sumoBinary = "C:/Program Files (x86)/DLR/Sumo/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "autobahn.sumocfg"]


traci.start(sumoCmd, label = "sim3")

conn1 = traci.getConnection("sim3")

""" -----------------------------------------Simulation Rear Collision-----------------------------------------------------------"""

#Information des Ego vehicle
veh = "veh0"

# Variable to begin step.
i = 0


"""------------------------------------Add Route dynamicaly-----------------------------------------------------------------------"""
traci.route.add("route0", ['Lane1','Lane2','Lane4','Lane5'])

"""------------------------------------Add Vehicle dynamicaly---------------------------------------------------------------------"""
traci.vehicle.add(veh, "route0", depart=0, pos=0, speed=10, lane=0, typeID='Car')
traci.vehicle.add("veh1", "route0", depart=0, pos=0, speed=10, lane=2, typeID='Car1')

"""-----------------------------Change  Vehicle information like LaneChangeMode, SetSpeedMode, setSpeedMode, setMinGap------------"""
traci.vehicle.setLaneChangeMode('veh1',0)
traci.vehicle.setSpeedMode('veh1',0)
traci.vehicle.setLaneChangeMode('veh0',0)
traci.vehicle.setSpeedMode('veh0',0)
traci.vehicletype.setMinGap("Car",0)
traci.vehicletype.setMinGap("Car1",0)
    
#print(traci.vehicletype.getMaxSpeed('Car'))


"""--------------------------------Print each spet of the simulation between 0 and 5------------------------------------------------"""
for step in range (5):
    print("step", i )
    traci.vehicle.changeLane('veh1', 2 , 25)
    i = i+1
    print(traci.simulation.getEndingTeleportIDList())
    print(veh + " drives with " + str(traci.vehicle.getSpeed('veh0')))
    print('veh1' + " drives with " + str(traci.vehicle.getSpeed('veh1')))
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

"""--------------------------------Print each spet of the simulation between 0 and 5------------------------------------------------"""

for step in range (5):
    print("step", i )
    traci.vehicle.changeLane('veh1', 1 , 25)
    i = i+1
    print(traci.simulation.getEndingTeleportIDList())
    print(veh + " drives with " + str(traci.vehicle.getSpeed('veh0')))
    print('veh1' + " drives with " + str(traci.vehicle.getSpeed('veh1')))
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

"""--------------------------------Print each spet of the simulation between 0 and 5------------------------------------------------"""
for step in range (5):
    print("step", i )
    traci.vehicle.changeLane('veh1', 1 , 25)
    i = i+1
    print(traci.simulation.getEndingTeleportIDList())
    traci.vehicle.setSpeed('veh1',4)
    traci.vehicle.setSpeed(veh,6)
    print(veh + " drives with " + str(traci.vehicle.getSpeed('veh0')))
    print('veh1' + " drives with " + str(traci.vehicle.getSpeed('veh1')))
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")


"""--------------------------------Print each spet of the simulation between 0 and 2------------------------------------------------"""

for step in range (2):
    print("step", i)
    traci.vehicle.changeLane('veh1', 0 , 25)
    i= i+1
    print(traci.simulation.getEndingTeleportIDList())
    print(veh + " drives with " + str(traci.vehicle.getSpeed('veh0')))
    print('veh1' + " drives with " + str(traci.vehicle.getSpeed('veh1')))
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

    
traci.vehicle.setSpeed('veh1',10)

for step in range (2):
    print("step", i)
    traci.vehicle.changeLane('veh1', 0 , 25)
    i= i+1
    print("Number of teleporting vehicle "+ str(traci.simulation.getStartingTeleportNumber()))
    print(traci.simulation.getStartingTeleportIDList())
    print(traci.simulation.getEndingTeleportIDList())
    print(veh + " drives with " + str(traci.vehicle.getSpeed('veh0')))
    print('veh1' + " drives with " + str(traci.vehicle.getSpeed('veh1')))
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

"""-------------------Simulation Collision during the Lane Changing of the vehicle 3 and the vehicle 4 in the middle lane ------------------------------------------"""


traci.vehicle.add("veh2", "route0", depart=0, pos=0, speed=10, lane=0, typeID='Car')
traci.vehicle.add("veh3", "route0", depart=0, pos=0, speed=10, lane=2, typeID='Car1')
traci.vehicle.setLaneChangeMode('veh2',0)
traci.vehicle.setSpeedMode('veh2',0)
traci.vehicle.setLaneChangeMode('veh3',0)
traci.vehicle.setSpeedMode('veh3',0)
traci.vehicletype.setMinGap("Car",0)
traci.vehicletype.setMinGap("Car1",0)


"""--------------------------------Print each spet of the simulation between 0 and 10------------------------------------------------"""
for step in range (10):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane('veh2', 0 , 25)
    traci.vehicle.changeLane('veh3', 2 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

for step in range (1):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane('veh2', 1 , 25)
    traci.vehicle.changeLane('veh3', 1 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")


"""-------------------Simulation of the Collision of the ego vehicle (veh0) and any vehicle  during the Lane Changing of the ego vehicle to the most right lane ------------------------------------------"""


traci.vehicle.add("veh4", "route0", depart=0, pos=0, speed=10, lane=2, typeID='Car1')
traci.vehicle.add("veh5", "route0", depart=0, pos=4, speed=10, lane=0, typeID='Car')
traci.vehicle.setLaneChangeMode("veh4",0)
traci.vehicle.setSpeedMode("veh4",0)
traci.vehicle.setLaneChangeMode('veh5',0)
traci.vehicle.setSpeedMode('veh5',0)
traci.vehicletype.setMinGap("Car",0)
traci.vehicletype.setMinGap("Car1",0)

"""--------------------------------Print each spet of the simulation between 0 and 12------------------------------------------------"""
for step in range (7):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane("veh4", 2 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

for step in range (5):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane("veh4", 1 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

for step in range (1):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane("veh4", 0 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

    

"""-------------------Simulation of the Collision of the ego vehicle (veh0) and any vehicle  during the Lane Changing of the ego vehicle to the most right lane ------------------------------------------"""

traci.route.add("route1", ['Lane1','Lane2','Lane3'])
traci.route.add("route2", ['Lane6','Lane2','Lane4','Lane5'])
traci.vehicle.add("veh6", "route1", depart=0, pos=3, speed=10, lane=2, typeID='Car1')
traci.vehicle.add("veh7", "route2", depart=0, pos=0, speed=10, lane=0, typeID='Car')
traci.vehicle.setLaneChangeMode("veh6",0)
traci.vehicle.setSpeedMode("veh6",0)
traci.vehicle.setLaneChangeMode('veh7',0)
traci.vehicle.setSpeedMode('veh7',0)
traci.vehicletype.setMinGap("Car",0)
traci.vehicletype.setMinGap("Car1",0)


"""--------------------------------Print each spet of the simulation between 0 and 17------------------------------------------------"""
for step in range (7):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane("veh6", 2 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

for step in range (10):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane("veh6", 1 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

for step in range (1):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane("veh6", 0 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")




"""-------------------Simulation of the Collision of the ego vehicle (veh0) and any vehicle  during the Lane Changing of the other vehicle to the most left lane ------------------------------------------"""


traci.vehicle.add("veh8", "route0", depart=0, pos=0, speed=10, lane=2, typeID='Car1')
traci.vehicle.add("veh9", "route2", depart=0, pos=5, speed=10, lane=0, typeID='Car')
traci.vehicle.setLaneChangeMode("veh8",0)
traci.vehicle.setSpeedMode("veh8",0)
traci.vehicle.setLaneChangeMode('veh9',0)
traci.vehicle.setSpeedMode('veh9',0)
traci.vehicletype.setMinGap("Car",0)
traci.vehicletype.setMinGap("Car1",0)


"""--------------------------------Print each spet of the simulation between 0 and 24------------------------------------------------"""
for step in range (7):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane("veh8", 2 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

for step in range (8):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane("veh8", 2 , 25)
    traci.vehicle.changeLane("veh9", 0 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

for step in range (5):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane("veh8", 1 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

traci.vehicletype.setMaxSpeed("Car1",7)


#The function below is used during the collision of two vehicles if the none option is used in the sumocfg file otherwise it will generate an error
    
for step in range (3):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane("veh9", 0 , 25)
    traci.vehicle.changeLane("veh8", 1 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")

for step in range (1):
    print("step", i)
    i= i+1
    traci.vehicle.changeLane("veh8", 1 , 25)
    traci.vehicle.changeLane("veh9", 1 , 25)
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"Collision"+str(i)+".png")



traci.close()
