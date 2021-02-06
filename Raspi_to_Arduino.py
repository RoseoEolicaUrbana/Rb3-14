#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 03:15:42 2021

@author: ai5
"""

import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
def blink(pin):

    
    GPIO.output(pin,GPIO.HIGH)  
    time.sleep(1)  
    GPIO.output(pin,GPIO.LOW)  
    time.sleep(1)  
    return

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
while True:
    
    read_ser=ser.readline()
    print(read_ser)
    blink(17)
    if(read_ser=="Hello From Arduino!"):
        blink(17)