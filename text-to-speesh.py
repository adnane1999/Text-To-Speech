from tkinter import *
from tkinter import ttk
import gtts
from playsound import playsound
import random
import os

def speak():
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)

    randfile = str(r2)+"randomtext"+str(r1) +".mp3"

    text = ytdEntry.get()
    choice = ytdchoices.get()
    if (choice == choices[0]):
       tts = gtts.gTTS(text, lang="en")
    else:
       tts = gtts.gTTS(text, lang="ar")


    tts.save(randfile)
    playsound(randfile)

    print(randfile)
    os.remove(randfile)

root = Tk()
root.title("Adnane's text to speech") #window title    
root.geometry("400x200") #set window 
root.columnconfigure(0,weight=1)#set all content in center 


ytdLabel = Label(root,text="Enter a text",font=("jost",15))
ytdLabel.grid()

ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

choices = ["English","العربية"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

saveEntry = Button(root,width=10,bg="green",fg="white",text="Speak", command = speak)
saveEntry.grid()

ytdLabel = Label(root,text="Devloped by : Adnane Ziadi",font=("jost",15))
ytdLabel.grid()

root.mainloop()
