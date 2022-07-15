"""
"""

import climatempo as climatempo

token = "putYourTokenHere"
cityId = "5011" # Três de Maio
climatempo = climatempo.ClimaTempo(token, cityId)
print("Forecast for " + climatempo.cityName + " - " + climatempo.state + " - " + climatempo.country)


#statusCode, weather = climatempo.getCurrentWeather()
#print(statusCode)
#print(weather)
#print(weather['id'])


#statusCode, json = climatempo.getForecast72Hours()
#print(statusCode)
#print(json)