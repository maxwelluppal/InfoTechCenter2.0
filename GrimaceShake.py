print("\n*********************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

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
        print("VRS has been engaged only allowing you to drive 50mph.")
    elif weatherAlert == "blizzardy":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of",weatherAlert,
              "weather conditions.\n")
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions.\n")
        print("VRS has been engaged only allowing you to drive 60mph")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 20 minutes because of the forecast of",weatherAlert,
              "weather conditions.\n")
        print("VRS has been engaged only allowing you to drive 55mph")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 5 minutes because of the forecast of",weatherAlert,
              "weather conditions.\n")
        print("VRS has been engaged only allowing you to drive 70mph")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forecast of",weatherAlert,
              "weather conditions.\n")
        print("VRS has been engaged only allowing you to drive 30mph")
    else:
        print("\nNational Weather Service forecasts",weatherAlert,
              "weather conditions.\n")
        print("VRS has been disengaged! Drive at your own risk.")

vehicleResponseSystem()