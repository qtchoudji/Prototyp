
import traci
import traci.constants as tc

sumoBinary = "C:/Program Files (x86)/DLR/Sumo/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "kreuzung.sumocfg"]


traci.start(sumoCmd, label = "sim1")
conn1 = traci.getConnection("sim1")


veh = "veh0"
i = 0

"""---------------------Simulation of crossing without traffic light----------------------------------------"""

"""-----------------------------Add Route dynamicaly--------------------------------------------------------"""
traci.route.add("route0", ['lane1_1','-lane3_1','lane10_1'])
traci.route.add("route1", ['lane4_1','-lane3_1','lane10_1'])
traci.route.add("route2", ['lane2_1','-lane3_1','lane10_1'])
traci.route.add("route3", ['-lane10_1','lane3_1','-lane1_1'])
traci.route.add("route4", ['lane9_1','lane3_1','-lane1_1'])
traci.route.add("route5", ['lane4_1','-lane2_1'])
traci.route.add("route6", ['lane9_1','lane10_1'])



"""-----------------------------Add Vehicles dynamicaly--------------------------------------------------------"""



traci.vehicle.add("veh1", "route1", depart=0, pos=0, speed=5, lane=0, typeID='Car3')

for step in range (3):
    print("step", i)
    i = i+1
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Kreuzug/"+str(i)+".png")

    
traci.vehicle.add(veh, "route0", depart=0, pos=0, speed=5, lane=0, typeID='Car1')
traci.vehicle.add("veh2", "route0", depart=0, pos=0, speed=5, lane=0, typeID='Car')

for step in range (3):
    print("step", i)
    i = i+1
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Kreuzug/"+str(i)+".png")

    
traci.vehicle.add("veh3", "route2", depart=0, pos=0, speed=5, lane=0, typeID='Car2') 

for step in range (5):
    print("step", i)
    i = i+1
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Kreuzug/"+str(i)+".png")

traci.vehicle.add("veh4", "route4", depart=0, pos=0, speed=5, lane=0, typeID='Car') 

for step in range (4):
    print("step", i)
    i = i+1
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Kreuzug/"+str(i)+".png")

traci.vehicle.add("veh5", "route4", depart=0, pos=0, speed=5, lane=0, typeID='Car') 
for step in range (8):
    print("step", i)
    i = i+1
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Kreuzug/"+str(i)+".png")


traci.vehicle.add("veh6", "route1", depart=0, pos=0, speed=5, lane=0, typeID='Car3') 
for step in range (10):
    print("step", i)
    i = i+1
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Kreuzug/"+str(i)+".png")

    
traci.vehicle.add("veh7", "route6", depart=0, pos=0, speed=5, lane=0, typeID='Car')

for step in range (20):
    print("step", i)
    i = i+1
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Kreuzug/"+str(i)+".png")


"""-------------------ends simulation of crossing without traffic light-----------------------------------------"""



"""---------------------------Simulation of crossing with traffic light-----------------------------------------"""

"""-----------------------------Add Route dynamicaly--------------------------------------------------------"""
traci.route.add("route10", ['lane5_1','lane8_1'])
traci.route.add("route11", ['lane6_1','lane8_1'])
traci.route.add("route12", ['lane7_1','lane8_1'])
traci.route.add("route13", ['-lane8_1','-lane5_1'])
traci.route.add("route14", ['lane6_1','-lane5_1'])
traci.route.add("route15", ['lane7_1','-lane6_1'])


traci.vehicle.add(veh, "route10", depart=0, pos=0, speed=5, lane=0, typeID='Car1')
traci.vehicle.add("veh1", "route11", depart=0, pos=0, speed=5, lane=0, typeID='Car')
traci.vehicle.add("veh2", "route12", depart=0, pos=0, speed=5, lane=0, typeID='Car3')
traci.vehicle.add("veh3", "route15", depart=0, pos=0, speed=5, lane=0, typeID='Car2')
traci.vehicle.add("veh4", "route14", depart=0, pos=0, speed=5, lane=0, typeID='Car2')
traci.vehicle.add("veh5", "route13", depart=0, pos=0, speed=5, lane=0, typeID='Car2')
traci.vehicle.add("veh8", "route10", depart=0, pos=0, speed=5, lane=0, typeID='Car1')
traci.vehicle.add("veh9", "route11", depart=0, pos=0, speed=5, lane=0, typeID='Car')
traci.vehicle.add("veh10", "route12", depart=0, pos=0, speed=5, lane=0, typeID='Car3')

for step in range (70):
    print("step", i)
    i = i+1
    #Print information of traffic light.
    print(traci.trafficlight.getPhaseDuration("10"))
    print(traci.trafficlight.getPhase("10"))
    conn1.simulationStep()
    traci.gui.screenshot("View #0", "C:/Users/Ulrich/Desktop/projetsumo/Kreuzug/"+str(i)+".png")


"""-------------------ends simulation of crossing with traffic light-----------------------------------------"""   



traci.close()
