import serial
import time
from tkinter import*

global x1,x2,x3,x4,x5,x6,y
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
y=0

arduino=serial.Serial('COM4',9600)
time.sleep(2)

def led1():
    global x1
    if(x1==0):
        arduino.write('a'.encode())
        x1=1
        b1.config(bg="red",text="OFF puerta")
    else:
        arduino.write('b'.encode())
        x1=0
        b1.config(bg="green",text="ON puerta")

def led2():
    global x2
    if(x2==0):
        arduino.write('c'.encode())
        x2=1
        b2.config(bg="red",text="OFF cuarto")
    else:
        arduino.write('d'.encode())
        x2=0
        b2.config(bg="green",text="ON cuarto")

def led3():
    global x3
    if(x3==0):
        arduino.write('e'.encode())
        x3=1
        b3.config(bg="red",text="OFF cochera")
    else:
        arduino.write('f'.encode())
        x3=0
        b3.config(bg="green",text="ON cochera")

def led4():
    global x4
    if(x4==0):
        arduino.write('g'.encode())
        x4=1
        b4.config(bg="red",text="OFF sala")
    else:
        arduino.write('h'.encode())
        x4=0
        b4.config(bg="green",text="ON sala")

def led5():
    global x5
    if(x5==0):
        arduino.write('i'.encode())
        x5=1
        b5.config(bg="red",text="OFF cocina")
    else:
        arduino.write('j'.encode())
        x5=0
        b5.config(bg="green",text="ON cocina")

def led6():
    global x6
    if(x6==0):
        arduino.write('k'.encode())
        x6=1
        b6.config(bg="red",text="OFF baño")
    else:
        arduino.write('l'.encode())
        x6=0
        b6.config(bg="green",text="ON baño")

def intruso():
     global y,x1,x2,x3,x4,x5,x6
     arduino.flushInput()
     dato=arduino.readline()
     time.sleep(0.1)
     y=int(dato.decode())*5.0/1023
     if(y>0):
         label.config(text="intruso detectado",bg="red",fg="yellow",font="arial 14")
         x1=1
         b1.config(bg="red",state=DISABLED,text="OFF puerta")
         x2=1
         b2.config(bg="red",state=DISABLED,text="OFF cuaro")
         x3=1
         b3.config(bg="red",state=DISABLED,text="OFF cochera")
         x4=1
         b4.config(bg="red",state=DISABLED,text="OFF sala")
         x5=1
         b5.config(bg="red",state=DISABLED,text="OFF cocina")
         x6=1
         b6.config(bg="red",state=DISABLED,text="OFF baño")
         b7.config(text="apagar")

     else:
         label.config(text="\t\t\t",bg="blue")
         b1.config(state=NORMAL)
         b2.config(state=NORMAL)
         b3.config(state=NORMAL)
         b4.config(state=NORMAL)
         b5.config(state=NORMAL)
         b6.config(state=NORMAL)
         b7.config(text="Alarma")
        

def exi():
    arduino.close()
    ventana.destroy()

ventana=Tk()
ventana.geometry("450x400")
label=Label(ventana,text="",bg="blue",font="arial 14")
label.place(x=0,y=0,width=450,height=50)
b1=Button(ventana,text="ON puerta",bg="green",fg="white",font="arial 14",command=led1)
b1.place(x=0,y=100,width=150,height=100)
b2=Button(ventana,text="ON cuarto",bg="green",fg="white",font="arial 14",command=led2)
b2.place(x=150,y=100,width=150,height=100)
b3=Button(ventana,text="ON cochera",bg="green",fg="white",font="arial 14",command=led3)
b3.place(x=300,y=100,width=150,height=100)
b4=Button(ventana,text="ON sala",bg="green",fg="white",font="arial 14",command=led4)
b4.place(x=0,y=200,width=150,height=100)
b5=Button(ventana,text="0N cocina",bg="green",fg="white",font="arial 14",command=led5)
b5.place(x=150,y=200,width=150,height=100)
b6=Button(ventana,text="ON baño",bg="green",fg="white",font="arial 14",command=led6)
b6.place(x=300,y=200,width=150,height=100)
b7=Button(ventana,text="Alarma",bg="grey",fg="white",font="arial 14",command=intruso)
b7.place(x=150,y=300,width=150,height=50)
ex=Button(ventana,text="EXIT",bg="gold",fg="black",font="arial 14",command=exi)
ex.place(x=200,y=350,width=50,height=50)
ventana.mainloop()
