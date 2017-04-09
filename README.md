# DarkPi
An ambient weather display for Raspberry Pi Zero W, Pimoroni Blinkt, and Dark Sky API

I thought this would be a useful way to gauge whether the kids needed to bring a jumper or coat to school each day. It uses the Dark Sky api to pull down the forecasts for the next 8 hours, and display some vaguely appropriate colours. The lights are dimmer at night.

## Requirements

- [python-forecast.io](https://github.com/ZeevG/python-forecast.io)
- [Raspberry Pi Zero W and Blinkt LEDs](https://shop.pimoroni.com/products/pi-zero-w-starter-kit)
- [Blinkt libraries](https://github.com/pimoroni/blinkt)
- You'll need an api key for [Dark Sky api](https://darksky.net/dev/)

![Powered by Dark Sky](https://darksky.net/dev/img/attribution/poweredby-oneline.png)

## Installation

Install the Blinkt libraries: https://github.com/pimoroni/blinkt
`sudo pip install python-forecastio`

Put the darkypi.py script somewhere

Set the environment variables (I put them in `~/.bash_profile`)

```shell
DARKSKY_API="somethingsomething"; export DARKSKY_API
LAT="50.7"; export LAT
LON="-10.5"; export LON
```

## Run

`python darkpi.py`

## Scheduling

We want the display to update every hour, and when we power on the device. 

I wrote a little shell script called `run.sh` to hold the environment variables because cron is... awkward

```shell
DARKSKY_API="something"; export DARKSKY_API
LAT="50.5"; export LAT
LON="-8.5"; export LON

python ~/darkpi/darkpi.py
```

Run `crontab -e` and add these entries to the crontab

```
0 * * * * /darkpi/run.sh
@reboot   /darkpi/run.sh
```

## Examples

![Partly cloudy](https://github.com/ideasasylum/DarkPi/blob/master/partlycloudy.JPG)

![Output](https://github.com/ideasasylum/DarkPi/blob/master/output.JPG)

![Rainy now](https://github.com/ideasasylum/DarkPi/blob/master/rainynow.JPG)

![Clear and partly cloudy](https://github.com/ideasasylum/DarkPi/blob/master/clear-and-partly-cloudy.JPG)
