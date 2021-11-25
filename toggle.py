from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led_1 = LED(26)
led_2 = LED(19)
led_3 = LED(20)



def ledToggle1():
    if led_1.is_lit:
        led_1.off()
        ledButton1["text"] = "Turn led_1 ON"
        
    else:
        led_1.on()
        ledButton1["text"] = "Turn led_1 OFF"
        
def ledToggle2():
    if led_2.is_lit:
        led_2.off()
        ledButton2["text"] = "Turn led_2 ON"
        
    else:
        led_2.on()
        ledButton2["text"] = "Turn led_2 OFF"
        
def ledToggle3():        
    if led_3.is_lit:
        led_3.off()
        ledButton3["text"] = "Turn led_3 ON"
        
    else:
        led_3.on()
        ledButton3["text"] = "Turn led_3 OFF"
        
def close():
    RPi.GPIO.cleanup()
    win1.destroy()


win1 = Tk()
win1.title("led_1 toggler")
myFont = tkinter.font.Font(family = 'Arial', size = 12, weight = 'bold')

ledButton1 = Button(win1, text = 'Turn led_1 ON', font = myFont, command = ledToggle1, bg = 'white', height = 1, width = 24)
ledButton1.grid(row=1,column=0)

ledButton2 = Button(win1, text = 'Turn led_2 ON', font = myFont, command = ledToggle2, bg = 'white', height = 1, width = 24)
ledButton2.grid(row=2,column=0)

ledButton3 = Button(win1, text = 'Turn led_3 ON', font = myFont, command = ledToggle3, bg = 'white', height = 1, width = 24)
ledButton3.grid(row=3,column=0)

exitButton = Button(win1, text = 'EXIT', font = myFont, command = close, bg = 'grey', height = 1, width = 24)
exitButton.grid(row=4,column=0)
