#!/usr/bin/env python3
import serial
import random

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

while True:
	blink = input()
	if blink == 'l':
		print("led Ligado")
		ser.write(str(blink).encode('utf-8'))
	elif blink == 'd':
		print("led desligado")
		ser.write(str(blink).encode('utf-8'))
