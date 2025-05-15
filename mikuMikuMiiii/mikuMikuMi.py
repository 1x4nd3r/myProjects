import random
from tkinter import *
from PIL import Image, ImageTk

width = 640
height = 480

fontFamily = 'Comic Sans MS'
fontSize = 10
fontColor = 'azure'

bgColor = '#122333'

window = Tk()
window.title('My AWESOME app!')
window.geometry("640x480")
window.iconbitmap('')
window.config(bg = bgColor)

global mikuMeterProgress
mikuMeterProgress = 0

def mikuMeter():
    global mikuMeterProgress
    mikuMeterProgress = mikuMeterProgress +1

    if mikuMeterProgress == 1:
        print("ONE!")
    if mikuMeterProgress == 2:
        print("!")
    if mikuMeterProgress == 3:
        print("!")
    if mikuMeterProgress == 4:
        print("!")
    if mikuMeterProgress == 5:
        print("TWO!")
    if mikuMeterProgress == 6:
        print("!")
    if mikuMeterProgress == 7:
        print("!")
    if mikuMeterProgress == 8:
        print("!")
    if mikuMeterProgress == 9:
        print("THREE...")
    if mikuMeterProgress == 10:
        print("...")
    if mikuMeterProgress == 11:
        print("ready?")
    if mikuMeterProgress == 12:
        print("MIKU MIKU MIIIIIIIIII!")
    if mikuMeterProgress >= 13:
        rng = random.randrange(1,10)
        print("!" * rng)

image = Image.open('testing\img\hatsuneMiku.png')
mikuImg = image.resize((170, 300))

myPhoto = ImageTk.PhotoImage(mikuImg)
myButton = Button(window,
                  image = myPhoto,
                  command = mikuMeter,
                  bg = bgColor,
                  activebackground = 'black'
                  )
myButton.place(x = 50, y = 50)

window.mainloop()