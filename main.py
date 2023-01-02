import machine
from machine import Pin
import dht
import time
import ubinascii
import network
from umqttsimple import MQTTClient

temp_sensor = dht.DHT11(Pin(2))
ssid = 'YOUR_WIFI_SSID'
password = 'YOUR_WIFI_PASSWORD'
mqtt_server = '0.0.0.0'
mqtt_port = 1883
mqtt_user = "YOUR_MQTT_USERNAME"
mqtt_pass = "YOUR_MQTT_PASSWORD"
client_id = ubinascii.hexlify(machine.unique_id())


station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

try:
   client = MQTTClient(client_id, mqtt_server, mqtt_port, mqtt_user, mqtt_pass)
   client.connect()
   print('Connected to %s MQTT broker' % (mqtt_server))
except OSError as e:
   print('Failed to connect to MQTT broker. Reconnecting...')
   time.sleep(5)
   machine.reset()

try:
   temp_sensor.measure()
   temp = round(temp_sensor.temperature(), 2)
   temperature = str(temp)
   client.publish(b'test/sensor/home/temp', temperature)
   print("the temperature is " + temperature)
   time.sleep(2)
   rtc = machine.RTC()
   rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
   # set RTC.ALARM0 to fire after Xmilliseconds, waking the device
   rtc.alarm(rtc.ALARM0, 60000)
   #put the device to sleep
   machine.deepsleep()
except OSError as e:
   print('Failed to connect to MQTT broker. Reconnecting...')
   time.sleep(5)
   machine.reset()
