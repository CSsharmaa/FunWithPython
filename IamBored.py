from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry("400x400")

myFont = font.Font(family='Helvetica', size=20, weight='bold')
btnFont = font.Font(family='Helvetica', size=10, weight = 'bold')

MainLabel = Label(window, text= "Are you stupid?")
MainLabel['font'] = myFont
MainLabel.place(x=100, y=100)

def display():
    label = Label(window, text="I know! (:", bd = "10")
    label['font'] = myFont
    label.place(x=130, y=200)
    btn.forget()
    btn1.forget()
    btn2.forget()
    MainLabel.forget()

def changeagain():
    btn['font'] = btnFont
    btn.place(x=190, y=150)
    btn1.forget()

def change():
    btn.forget()
    btn1['font'] = btnFont
    btn1.pack(side = "top")


btn = Button(window, text="No", bd="5", command=change)
btn['font'] = btnFont
btn.place(x = 190, y =150)

btn1 = Button(window, text="No", bd="5", command=changeagain)

btn2 = Button(window, text="Yes", bd="5", command=display)
btn2['font'] = btnFont
btn2.place(x = 150, y =150)


window.mainloop()
