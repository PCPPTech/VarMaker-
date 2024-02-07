from tkinter import *

def donateFunc():
    donateMe = Toplevel()
    donateMe.title("VM - Donate")
    donateMe.geometry("800x500")

    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    donateMe.iconphoto(False, varmakerIcon)

    label = Label(donateMe, text="Every donation is APPRECIATED!!!", font=("Calibri", 15))
    label.pack()

    paypal = Label(donateMe, text="PayPal: @eidnoxon213", font=("Calibri", 15, 'bold'))
    paypal.pack()

    appreciate = Label(donateMe, text="Every single donation is appreciated, even the $1 ones :)", font=("Calibri", 13))
    appreciate.pack()

    dontForget = Label(donateMe, text="Don't forget to join my discord server: https://discord.gg/xQXnhtpnNf", font=("Calibri", 15))
    dontForget.pack()

    goodBye = Label(donateMe, text="Bye :)", font=("Dejavu Sans Mono", 13))
    goodBye.pack()

    donateMe.mainloop()