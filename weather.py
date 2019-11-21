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
        sunrise_time = str(time.ctime(x["sys"]["sunrise"]))
        sunset_time = str(time.ctime(x["sys"]["sunset"]))

        print(country_code + " " + city + "(" + latitude + ", " + longitude + ")")
        print("Temperature: " + current_temperature + "°C Min: " + min_temperature + "°C Max: " + max_temperature + "°C")
        print(weather_description + " Wind: " + wind_speed + "m/s Cloudiness: " + cloudiness + "% Humidity: " + humidity + "% Pressure: " + pressure + "hpa")
        print("Sunrise: " + sunrise_time)
        print("Sunset: " + sunset_time)

#        while 1:  
#            print("Clock: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S'), end='\r')
#            time.sleep(1)

    else:
      print("Couldn't get data")
