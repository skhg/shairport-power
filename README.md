# shairport-power

## Background
I recently got and old pair of speakers, and wanted to set them up to stream wirelessly with [AirPlay](https://www.apple.com/airplay/). One of the best ways to do this with 3rd-party software seems to be to run [shairport-sync](https://github.com/mikebrady/shairport-sync) on a [Raspberry Pi](https://www.raspberrypi.org/).

However, it turned out that my speakers had a bit of a "hum" when no audio was playing, so I needed a way to switch them off when not in use. Also saving a couple of watts of power.

## The finished product
(Youtube Video)

[![Video of it switching off](http://img.youtube.com/vi/Is1vkanx2_s/0.jpg)](http://www.youtube.com/watch?v=Is1vkanx2_s)






Inspired by
https://github.com/mikebrady/shairport-sync/issues/931

Fix GPIO permissions
https://raspberrypi.stackexchange.com/questions/40105/access-gpio-pins-without-root-no-access-to-dev-mem-try-running-as-root
https://github.com/mikebrady/shairport-sync/issues/775

Pinout
https://www.electronicwings.com/raspberry-pi/raspberry-pi-gpio-access

Have to use GPIO library because we want state to remain after script exits
https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/

This doesnt work with https://gpiozero.readthedocs.io/en/stable/faq.html

How to connect a relay
https://howtomechatronics.com/tutorials/arduino/control-high-voltage-devices-arduino-relay-tutorial/
