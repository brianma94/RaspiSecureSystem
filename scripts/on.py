import serial

arduino = serial.Serial('/dev/ttyACM0',9600)
arduino.write('h')
arduino.close()
