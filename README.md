# DarkPi
An ambient weather display for Raspberry Pi Zero W, Pimoroni Blinkt, and Dark Sky API

I thought this would be a useful way to gauge whether the kids needed to bring a jumper or coat to school each day. It uses the Dark Sky api to pull down the forecasts for the next 8 hours, and display some vaguely appropriate colours. The lights are dimmer at night.

## Requirements

[python-forecast.io](https://github.com/ZeevG/python-forecast.io)
[Raspberry Pi Zero W and Blinkt LEDs](https://shop.pimoroni.com/products/pi-zero-w-starter-kit)
[Blinkt libraries](https://github.com/pimoroni/blinkt)
You'll need an api key for [Dark Sky api](https://darksky.net/dev/)

## Installation

Install the Blinkt libraries: https://github.com/pimoroni/blinkt
`sudo pip install python-forecastio`

Put the darkypi.py script somewhere

Set the environment variables (I put them in `~/.bash_profile`)

```bash
DARKSKY_API="somethingsomething"; export DARKSKY_API
LAT="50.7"; export LAT
LON="-10.5"; export LON
```

## Run

`python darkpi.py`

## Scheduling

We want the display to update every hour, and when we power on the device. 
Run `crontab -e` and add these entries to the crontab

```
0 * * * * python ~/darkpi/darkpi.py
@reboot python ~/darkpi/darkpi.py
```

![Powered by Dark Sky](https://darksky.net/dev/img/attribution/poweredby-oneline.png)
