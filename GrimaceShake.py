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

#Function will call the gasLevelGauge to determine our gas level and then find a close gas station
#by calling the listOfGasStations function if we are on Low or Quarter Tank or Empty
def gasLevelAlert():
    milesToGasStationLow = random.uniform(0,25)
    milesToGasStationQuarterTank = random.uniform(25.1,50)
    #gasLevelGauge = gasLevelGauge()
    print(milesToGasStationLow)
    print(milesToGasStationQuarterTank)

gasLevelAlert()