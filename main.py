import time
from machine import Pin, PWM, reset
import esp
esp.osdebug(None)

try:
   import usocket as socket
except:
   import socket
   
import gc
gc.collect()

#use a pushbutton sensor for future use
#p14 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

#def callback(p):
#   print(p)
#   BIN1.duty(0)
#   BIN2.duty(0)
#   AIN1.duty(0)
#   AIN2.duty(0)
#   machine.reset()

pin1 = Pin(5, Pin.OUT)  # D1
pin2 = Pin(4, Pin.OUT)  # D2
pin3 = Pin(0, Pin.OUT)  # D3
pin4 = Pin(2, Pin.OUT)  # D4

BIN1 = PWM(pin1, freq=750)
BIN2 = PWM(pin3, freq=750)
AIN1 = PWM(pin2, freq=750)
AIN2 = PWM(pin4, freq=750)

def web_page():

   #generate blank page
   html = """ """
   return html

#Let's create a simple web server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#listening on port 80. Will use HTTPS (port 443) in V2
s.bind(('', 80))
s.listen(5)
   
def main_loop():
   while True:
      #p14.irq(trigger=Pin.IRQ_FALLING, handler=callback)
      conn, addr = s.accept()
      print('Got a connection from %s' % str(addr))
      request = conn.recv(1024)
      request = str(request)
      print('Content = %s' % request)
      forward = request.find('/?direction=up')
      backward = request.find('/?direction=down')
      stop = request.find('/?direction=stop')
      #The duty numbers and timers are derivated from trial/error calibration since one motor is slightly slower than the other.This is also important to make sure the nylon string is not too loose on the way down.
      if forward == 6:
         print('UP')
         BIN1.duty(1800)
         BIN2.duty(0)
         AIN1.duty(2000)
         AIN2.duty(0)
         time.sleep(1.8)
         BIN1.duty(0)
         BIN2.duty(0)
         AIN1.duty(0)
         AIN2.duty(0)
      if backward == 6:
         print('DOWN')
         BIN1.duty(730)
         BIN2.duty(730)
         AIN1.duty(860)
         AIN2.duty(860)
         time.sleep(0.75)
         BIN1.duty(0)
         BIN2.duty(0)
         AIN1.duty(0)
         AIN2.duty(0)
      if stop == 6:
         print('STOP')
         BIN1.duty(0)
         BIN2.duty(0)
         AIN1.duty(0)
         AIN2.duty(0)
      response = web_page()
      conn.send('HTTP/1.1 200 OK\n')
      conn.send('Content-Type: text/html\n')
      conn.send('Connection: close\n\n')
      conn.sendall(response)
      conn.close()

main_loop()
