# MicropythonMQTTTempSensor
An MQTT Temperature sensor to a broker using Micropython

This is so that an ESP8266 or ESP32 module can be used battery powered and to take itself up from sleep and report to the temperature status using a DHT11/22 to an MQTT broker.

I've used the umqttsimple library from here: https://github.com/RuiSantosdotme/ESP-MicroPython/blob/master/code/MQTT/umqttsimple.py

You'll need to download this file and upload it to your ESP32/8266.

There are two versions, one with a boot.py and main.py and another with simply a boot.py (boot_.py) script. Either can be used, but the single file was better on the memory usage.
