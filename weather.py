import pyowm

api_key = "74c8a5ed2adad61f64819dfed080f662"
owm = pyowm.OWM(api_key)

observation = owm.weather_at_place("London,GB")
w = observation.get_weather()
print(w)