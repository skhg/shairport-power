# shairport-power

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
