from blinkt import set_pixel, set_clear_on_exit, show, clear
import forecastio
import os

# API details
api_key = os.environ['DARKSKY_API']
lat = float(os.environ['LAT'])
lng = float(os.environ['LON'])

# Colours
off = [0,0,0]
blue = [29, 90, 254]
pink = [255, 0, 30]
red = [255, 0, 0]
yellow = [255, 120, 0]
orange = [255, 40, 0]
dark_blue = [0, 0, 60]
white = [255, 255, 255]
grey = [20, 20, 20]
green = [0, 255, 20]

set_clear_on_exit(False)
clear()

def display_weather(pixel, colour, brightness):
  print(pixel, colour, brightness)
  set_pixel(pixel, colour[0], colour[1], colour[2], brightness)

forecast = forecastio.load_forecast(api_key, lat, lng)

daily = forecast.daily()
sunrise = daily.data[0].sunriseTime
sunset = daily.data[0].sunsetTime

hourly = forecast.hourly()
for i in range(0, 8):
  hourlyData = hourly.data[i]
  print(i, hourlyData.icon)

  brightness = 0.05
  if ((hourlyData.time > sunrise) and (hourlyData.time < sunset)):
    brightness = 0.5

  colour = off

  if hourlyData.icon == "wind":
    colour = orange
  elif hourlyData.icon == "rain":
    colour = dark_blue
  elif hourlyData.icon == "snow":
    colour = white
  elif hourlyData.icon == "sleet":
    colour = white
  elif hourlyData.icon == "fog":
    colour = green
  elif hourlyData.icon == "cloudy":
    colour = pink
  elif hourlyData.icon == "clear-day":
    colour = yellow
  elif hourlyData.icon == "partly-cloudy-day":
    colour = orange
  elif hourlyData.icon == "clear-night":
    colour = yellow
  elif hourlyData.icon == "partly-cloudy-night":
    colour = orange
  else:
    colour = off

  display_weather(i, colour, brightness)

show()

