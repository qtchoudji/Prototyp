
"""--------------------------------------------------------------------------------------------------"""
"""--------------------------Simulation of Lane Change---------------------------------------------- """
"""--------------------------------------------------------------------------------------------------"""



import traci
import traci.constants as tc

sumoBinary = "C:/Program Files (x86)/DLR/Sumo/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "autobahn.sumocfg"]

traci.start(sumoCmd, label = "sim1")
conn1 = traci.getConnection("sim1")




veh = "veh0"   #Ego Vehicle
i = 0 #Variable to show different step


# Add Route on the scenario
traci.route.add("route0", ['Lane1','Lane2','Lane4','Lane5'])
traci.route.add("route1", ['Lane1','Lane2','Lane3'])
traci.route.add("route2", ['Lane6','Lane2','Lane4','Lane5'])
traci.route.add("route3", ['Lane6','Lane2','Lane3'])

#Add Ego Vehicle and others vehicles
traci.vehicle.add(veh, "route0", depart=0, pos=0, speed=10, lane=0, typeID='Car1')
traci.vehicle.add("veh1", "route0", depart=0, pos=15, speed=5, lane=0, typeID='Car3')
traci.vehicle.add("veh2", "route0", depart=0, pos=15, speed=10, lane=2, typeID='Car3')
traci.vehicle.add("veh3", "route1", depart=0, pos=0, speed=7, lane=2, typeID='Car3')
traci.vehicle.add("veh4", "route0", depart=0, pos=0, speed=8, lane=1, typeID='Car3')
traci.vehicle.add("veh5", "route0", depart=0, pos=30, speed=6, lane=1, typeID='Car3')
traci.vehicle.add("veh6", "route2", depart=0, pos=30, speed=7, lane=0, typeID='Car')
traci.vehicle.add("veh7", "route3", depart=0, pos=5, speed=6, lane=0, typeID='Car')
traci.vehicle.add("veh8", "route2", depart=0, pos=0, speed=6, lane=0, typeID='Car4')


    
#print(traci.vehicletype.getMaxSpeed('Car'))

traci.vehicle.setSpeed("veh1", 5)
traci.vehicle.setSpeed("veh2", 10)
traci.vehicle.setSpeed("veh3", 7)
traci.vehicle.setSpeed("veh4", 8)
traci.vehicle.setSpeed("veh4", 6)


for step in range (5):
    print("step", i )

    #traci.vehicle.changeLane('veh1', 2 , 25)
    i = i+1
        
    print(veh + " drives with " + str(traci.vehicle.getSpeed('veh0')))
    print('veh1' + " drives with " + str(traci.vehicle.getSpeed('veh1')))
    print('veh2' + " drives with " + str(traci.vehicle.getSpeed('veh2')))
    print('veh3' + " drives with " + str(traci.vehicle.getSpeed('veh3')))
    print('veh4' + " drives with " + str(traci.vehicle.getSpeed('veh4')))
    print('veh5' + " drives with " + str(traci.vehicle.getSpeed('veh5')))
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"LaneChange"+str(i)+".png")




for step in range (15):
    print("step", i )
    traci.vehicle.changeLane(veh, 0 , 25)
    traci.vehicle.changeLane('veh1', 0 , 25)
    traci.vehicle.changeLane('veh2', 2 , 25)
    traci.vehicle.changeLane('veh3', 2 , 25)
    traci.vehicle.changeLane('veh4', 1 , 25)
    traci.vehicle.changeLane('veh5', 1 , 25)
    i = i+1
        
    print(veh + " drives with " + str(traci.vehicle.getSpeed('veh0')))
    print('veh1' + " drives with " + str(traci.vehicle.getSpeed('veh1')))
    print('veh2' + " drives with " + str(traci.vehicle.getSpeed('veh2')))
    print('veh3' + " drives with " + str(traci.vehicle.getSpeed('veh3')))
    print('veh4' + " drives with " + str(traci.vehicle.getSpeed('veh4')))
    print('veh5' + " drives with " + str(traci.vehicle.getSpeed('veh5')))

    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"LaneChange"+str(i)+".png")


for step in range (40):
    print("step", i )
    i = i+1
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Autobahn/" +"LaneChange"+str(i)+".png") 



traci.close()
