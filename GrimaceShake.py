print("*********************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random

#Function that lists Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations, randomly choosing one and returning its value

def listOfGasStations():
    gasStationList = ["Shell","Speedway","Marathon","Circle K","Moble","CostCo","Meijer","7-Eleven"]
    gasStationsNearby = random.choice(gasStationList)
    return gasStationsNearby

print(gasLevelGauge())
print(listOfGasStations())