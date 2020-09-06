import socket 
import machine

import time
import network
def wifi_connect():
   #DISABLE ACCESS POINT FUNCTIONALITY
   ap_if = network.WLAN(network.AP_IF)
   ap_if.active(False)
   #ENABLE WIFI STATION (CLIENT) FUNCTIONALITY
   sta_if = network.WLAN(network.STA_IF)
   if not sta_if.isconnected():
      print('Connecting to wifi')
      sta_if.active(True)
      sta_if.connect('YOUR_WIFI_NETWORK', 'PASSWORD')
      while not sta_if.isconnected():
         pass
      print('network config:', sta_if.ifconfig())    
wifi_connect()

#start WebREPL
import webrepl
webrepl.start()

#run import webrepl_setup on the first start to setup the password