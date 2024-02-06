import os

os.system("pip install tkinter")
os.system("pip install PIL")
os.system("pip install pyinstaller")

from tkinter import *
success = Tk()
varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
success.iconphoto(False, varmakerIcon)
success.title("VM - Setup Operation Successful!")

lab = Label(success, text="IMPORTANT FILES ARE DOWNLOADED! Feel free to close this window! :)", font=("Arial", 15))
lab.pack()

def closeFunc():
    quit()

close = Button(success, text="Close Window", font=("Arial", 15), command=closeFunc)
close.pack()


success.mainloop()