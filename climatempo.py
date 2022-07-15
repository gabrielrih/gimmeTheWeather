"""
    Get weather informations by ClimaTempo
    
    References:
        Forecast 72 hours: http://apiadvisor.climatempo.com.br/doc/index.html#api-Forecast-Forecast72HoursByCity
        Current weather: http://apiadvisor.climatempo.com.br/doc/index.html#api-Weather-CurrentWeatherByCity
"""

import requests
import json

class ClimaTempo:
    def __init__(self, token, cityId):
        self.token = token
        self.cityId = cityId
        self.cityName, self.state, self.country = self._getCityById()

    def getCurrentWeather(self):
        endpoint = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + self.cityId + "/current?token=" + self.token
        statusCode, json = self._callAPIUsingGetMethod(endpoint)
        response = self._jsonToDict(json)
        return statusCode, response

    def getForecast72Hours(self):
        endpoint = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + self.cityId + "/hours/72?token=" + self.token
        statusCode, json = self._callAPIUsingGetMethod(endpoint)
        response = self._jsonToDict(json)
        return statusCode, response
    
    def _getCityById(self):
        endpoint = "http://apiadvisor.climatempo.com.br/api/v1/locale/city/" + self.cityId + "?token=" + self.token
        statusCode, json = self._callAPIUsingGetMethod(endpoint)
        response = self._jsonToDict(json)
        return response['name'], response['state'], response['country']

    def _callAPIUsingGetMethod(self, endpoint):
        response = requests.get(endpoint)
        return response.status_code, response.text

    # Convert JSON to Dictionary
    # Reference: https://www.w3schools.com/python/python_json.asp
    def _jsonToDict(self, string):
        return json.loads(string)
