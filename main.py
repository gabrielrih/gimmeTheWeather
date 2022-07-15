"""
    Gimme the weather
    <gabrielrih>
"""
from time import sleep

import libs.climatempo as climatempo
import libs.config as config

# Get configs
configs = config.Config('credentials.ini')

# Start ClimaTempo class
climatempo = climatempo.ClimaTempo(configs.token, configs.cityId)
print("Forecast for " + climatempo.cityName + " - " + climatempo.state + " - " + climatempo.country)

while (True):

    # Get current weather
    climatempo.getCurrentWeather()
    print("Temperature (Celsius): " + str(climatempo.currentTemperature) + "°")
    print("Sensation (Celsius): " + str(climatempo.currentSensation) + "°")
    print("Wind direction: " + str(climatempo.currentWindDirection))
    print("Wind velocity: " + str(climatempo.currentWindVelocity))
    print("Humidity: " + str(climatempo.currentHumidity))
    print("Condition: " + str(climatempo.currentCondition))
    print("Last update: " + str(climatempo.lastDateTime))
    sleep(600) # wait 10 minutes