import serial
import os
import time

arduino=serial.Serial('/dev/ttyACM0',9600)
arduino.flushInput()
arduino.flushOutput()
while True:
	x = arduino.read(2).rstrip('\n')
	arduino.flushInput()
	arduino.flushOutput()
	if x == ("dd"):
		os.system("/home/demo/getImage.sh > /dev/null")
	elif x.isdigit():
		file = open("/home/demo/temperatura.txt","a+")
		file.write(x + '\n')
		file.close()
	arduino.flushInput()
	arduino.flushOutput()
arduino.close()
