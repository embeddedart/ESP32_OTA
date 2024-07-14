from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

import machine
import time

# firmware_url = "https://github.com/kevinmcaleer/ota_test/main/"
firmware_url = "https://raw.githubusercontent.com/embeddedart/ESP32_OTA/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

ota_updater.download_and_install_update_if_available()

time.sleep(3)

led = machine.Pin(25, machine.Pin.OUT) #configure GPIO-15 Pin as an output pin and create and led object for Pin class

while True:
  # led.value(True)  #turn on the LED
  # time.sleep(1)   #wait for one second
  # led.value(False)  #turn off the LED
  # time.sleep(1)   #wait for one second
  led.toggle()
  time.sleep(1)
  print("toggle")

