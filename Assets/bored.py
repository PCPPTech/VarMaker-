from Games.CALAYgui import CALAYmain
from tkinter import *

def Bored():

    def gameFunctionality_CALAYgui():
        CALAYmain()
    
    
    bored = Toplevel()
    bored.geometry("750x550")
    bored.title("VM - Bored")
    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    bored.iconphoto(False, varmakerIcon)


    mainTitle = Label(bored, text="VM - Games", font=("Calibri", 20, "bold"))
    mainTitle.grid(row=0, column=1, columnspan=10)

    button_CALAYgui = PhotoImage(file="button_styles/button_creating-a-list-about-you-special.png")
    button_CountryWar = PhotoImage(file="button_styles/button_country-war.png")
    button_ComingSoon = PhotoImage(file="button_styles/button_coming-soon-special.png")

    #Games (Buttons)
    CountryWarButton = Button(bored, image=button_ComingSoon, border=0)
    CountryWarButton.grid(row=1, column=2)

    CALAYguiButton = Button(bored, image=button_CALAYgui, command=gameFunctionality_CALAYgui, border=0)
    CALAYguiButton.grid(row=2, column=2)
    bored.mainloop()