import requests, json
api_key = "API"
#city = input("Введіть назву міста: ")
city = "Delhi"
response = requests.get("http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city)
print(response)

weather = response.json()

w = weather["main"]

temperature = w["temp"]
pressure = w["pressure"]
humidity = w["humidity"]

z = w["weather"]

weather_description = z[0]["description"]

print(" Temperature (in kelvin unit) = " +
                    str(temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(pressure) +
          "\n humidity (in percentage) = " +
                    str(humidity) +
          "\n description = " +
                    str(weather_description))
