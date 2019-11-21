import requests, json, time
from datetime import datetime

def run():
    api_key = "7edf84dd10acde11474dde25976d17a1"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

#    permission_for_location = input("Use current location? (y/n): ")
    permission_for_location = "y"

    if permission_for_location == "y":
      city_name = requests.get("https://ipinfo.io/").json()["city"]
    else:
      city_name = input("Enter a city: ")  

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
        country_code = str(x["sys"]["country"])
        city = str(x["name"])
        latitude = str(x["coord"]["lat"])
        longitude = str(x["coord"]["lon"])

        weather_description = str(x["weather"][0]["main"])
        current_temperature = str(int(x["main"]["temp"]))
        min_temperature = str(int(x["main"]["temp_min"]))
        max_temperature = str(int(x["main"]["temp_max"]))

        pressure = str(x["main"]["pressure"]) # in hpa
        humidity = str(x["main"]["humidity"]) # int %

        wind_speed = str(x["wind"]["speed"]) # in m/s
        
        cloudiness = str(x["clouds"]["all"]) # cloudiness in %
        sunrise_time = str(datetime.fromtimestamp(x["sys"]["sunrise"]).strftime('%H:%M:%S'))
        sunset_time = str(datetime.fromtimestamp(x["sys"]["sunset"]).strftime('%H:%M:%S'))

        file = open("weather_report.txt", "w+")

#        file.write(city + "(" + latitude + ", " + longitude + ")\n")
        file.write(city + "\n")
        file.write(weather_description + "\n")
#        file.write(current_temperature + "°C min: " + min_temperature + "°C max: " + max_temperature + "°C\n")
        file.write(current_temperature + "°C\n")
        file.write("wind: " + wind_speed + "m/s\n")
        file.write("cloudiness: " + cloudiness + "%\n")
        file.write("humidity: " + humidity + "%\n")
        file.write("sunrise: " + sunrise_time + "\n")
        file.write("sunset: " + sunset_time + "\n")
	
        file.close()
    else:
      print("Couldn't get data")
