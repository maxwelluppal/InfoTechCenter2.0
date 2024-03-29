

#Import Libraries Here
import time
import sys
import random
from time import sleep

#Welcome Branch Starts Here
timeToSleep = 1

print("\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsis add a dot every .5 seconds
x =  0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!\n")

#Gasoline Branch Starts Here
print("\n*****************************************************************************************************"
      "***************************************************************************\n")
print("Gasoline Branch\n")

#Function that lists Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations, randomly choosing one and returning its value
def listOfGasStations():
    gasStationList = ["Shell","Speedway","Marathon","Circle K","Mobil","CostCo","Meijer","7-Eleven"]
    gasStationsNearby = random.choice(gasStationList)
    return gasStationsNearby

#Function will call the gasLevelGauge to determine our gas level and then find a close gas station
#by calling the listOfGasStations function if we are on Low or Quarter Tank or Empty
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(0,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep (2.5)
        print("   ***Calling Triple AAA***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station...\n")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter-tank, checking Google Maps for the closest gas station...\n")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is on a half-tank, which is plenty to reach your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three quarter tank.")
    else:
        print("Your gas tank is full - YEAH!!! - Congratulations! - Vroom Vroom!")

gasLevelAlert()
sleep(3)

print("\n*****************************************************************************************************"
      "***************************************************************************\n")

print("Weather Branch")


#Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["snowy","blizzardy","rainy","foggy","windy","icy","sunny",]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

weatherAlert = weather()

# Variable to call the weather() once VRS(Vehicle Response System) is determined

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of",weatherAlert,
              "weather conditions.\n")
        sleep(2)
        print("VRS has been engaged only allowing you to drive 50mph.")
    elif weatherAlert == "blizzardy":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of",weatherAlert,
              "weather conditions.\n")
        sleep(2)
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions.\n")
        sleep(2)
        print("VRS has been engaged only allowing you to drive 60mph")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 20 minutes because of the forecast of",weatherAlert,
              "weather conditions.\n")
        sleep(2)
        print("VRS has been engaged only allowing you to drive 55mph")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 5 minutes because of the forecast of",weatherAlert,
              "weather conditions.\n")
        sleep(2)
        print("VRS has been engaged only allowing you to drive 70mph")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forecast of",weatherAlert,
              "weather conditions.\n")
        sleep(2)
        print("VRS has been engaged only allowing you to drive 30mph")
    else:
        print("\nNational Weather Service forecasts",weatherAlert,
              "weather conditions.\n")
        sleep(2)
        print("VRS has been disengaged! Drive at your own risk.")

vehicleResponseSystem()

