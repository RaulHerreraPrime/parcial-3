import serial
import time

arduino=serial.Serial("COM4",9600)
time.sleep(2)

i=1
while(i>0):
    dato=input("Presiona s si deseas encender LED\nPresiona n si deseas apagar LED\nPresiona x si deseas salir\n")
    time.sleep(1)
    arduino.write(dato.encode())
    if (dato=="x"):
        i=0
arduino.close()
