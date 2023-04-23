import pyqrcode
from pyqrcode import *
from PIL import *
import tkinter as tk 
from tkinter import *


window = Tk()  
window.geometry('300x350')
window.title('GreatPrilojenie')

Label(window,text='Lets Create QR Code',font='arial 15').pack()
# String which represents the QR code
s = tk.StringVar()
  
# Generate QR code
def create_qrcode():
    s1=s.get()
    qr = pyqrcode.create(s1)
    qr.png('myqr.png', scale = 6)
    Label(window,text='QR Code is created and saved successfully').pack()

Entry(window,textvariable=s,font='arial 15').pack()
Button(window,text='create',bg='pink',command=create_qrcode).pack()
window.mainloop()