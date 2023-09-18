import os
import json
import tkinter
from tkinter import *
from PIL import Image, ImageTk

folder_path = './imgs/'
file =  "DSCN0463.JPG"
currPhoto = [-1]

def loadImg(number):
    c.create_image(x, y, image=img, anchor=NW)

# def click func
def click():
    text_info_1 = text1.get()
    label4.config(text="DSCN"+text_info_1+".JPG")
    currPhoto[0] = text_info_1
    loadphoto()

def loadphoto():
    c.delete("all")
    print("./imgs/DSCN" + currPhoto[0] + ".JPG")
    newimg =  Image.open("./imgs/DSCN" + currPhoto[0] + ".JPG")
    photoI = ImageTk.PhotoImage(newimg)
    print(photoI)
    d = Canvas(root, width=500, height=500)
    d.pack()

# Gui Config
root = Tk()
root.geometry('600x700')
root.title('Labeling Pictures')

# The actual gui
label1 = Label(root, text='What Photo To Start At?')
label1.pack()

spacing1 = Label(root)
spacing1.pack()

text1 = Entry(root)
text1.pack(ipadx=20)

spacing3 = Label(root)
spacing3.pack()

button = Button(root, text='Start Labeling!', command=click)
button.pack()

label4 = Label(root, text='choosePhoto')
label4.pack()

label2 = Label(root, text='Name')
label2.pack()

text4 = Entry(root)
text4.pack(ipadx=60)

label3 = Label(root, text='Tags (comma seperated)')
label3.pack()

# Create a photoimage object of the image in the path
image1 = Image.open("./imgs/DSCN0078.JPG")
test = ImageTk.PhotoImage(image1)

c = Canvas(root, width=500, height=500)
c.pack()

# img = ImageTk.PhotoImage(Image.open("\imgs\DSCN0076.JPG"))
c.create_image(0, 0, image=test, anchor=NW)

# Making the gui run
root.mainloop()