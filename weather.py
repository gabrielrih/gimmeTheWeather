"""
    Gimme the weather
    <gabrielrih>
"""
from datetime import datetime

# Private libraries
import libs.climatempo as climatempo
import libs.config as config
from callmebot import send_free_notification # Module from GitHub

def main():
    
    # Get configs
    configs = config.YmlConfig('config.yml')

    # Start ClimaTempo class
    clima = climatempo.ClimaTempo(configs.token, configs.cityId)
    content = "Clima para " + clima.cityName + " - " + clima.state + " - " + clima.country
    
    # Get forecast for 15 days
    statusCode, response = clima.getForecast15Days()
    if statusCode != 200:
        raise Exception("Error: " + str(response))

    # Filter results and gets just the today forecast
    day = getForecastForToday(response['data'])
    #print(day)
        
    # Get current weather
    statusCode, response = clima.getCurrentWeather()
    if statusCode != 200:
        raise Exception("Error: " + str(response))
    currentWeather = response
    #print(currentWeather)

    # Print forecast for today
    content += "\n" + "Dia: " + str(day['date_br'])
    content += "\n" + str(day['text_icon']['text']['phrase']['reduced'])
    content += "\n" + "Chuva - Probabilidade: " + str(day['rain']['probability']) + "% Precipitação: " + str(day['rain']['precipitation']) + "mm"
    content += "\n" + "Sensação térmica: " + str(currentWeather['data']['sensation']) + "°"
    content += "\n" + "Temperatura atual: " + str(currentWeather['data']['temperature']) + "°"
    content += "\n" + "Manhã - Max: " + str(day['temperature']['morning']['max']) + "° Min: " + str(day['temperature']['morning']['min']) + "°"
    content += "\n" + "Tarde - Max: " + str(day['temperature']['afternoon']['max']) + "° Min: "+ str(day['temperature']['afternoon']['min']) + "°"
    content += "\n" + "Noite - Max: " + str(day['temperature']['night']['max']) + "° Min: "+ str(day['temperature']['night']['min']) + "°"
    content += "\n" + "Nascer do sol: " + str(day['sun']['sunrise'])
    content += "\n" + "Por do sol: " + str(day['sun']['sunset'])

    # Print in stdout
    print(content)

    # Send forecast for each configured phoneNumber
    for receiver in configs.phoneNumbers:
        wasSent, response = send_free_notification(content, receiver['phoneNumber'], receiver['apiKey'], False)
        if not wasSent:
            print("Error: " + str(response))

def getForecastForToday(response):
    from datetime import date
    currentDate = date.today()
    for day in response:
        date = convertStringToData(day['date'])
        if date == currentDate:
            return(day)

def convertStringToData(string):
    date = datetime.strptime(string, '%Y-%m-%d').date()
    return date

if __name__ == '__main__':
    main()