from tkinter import *

def positiveUsers():
    lou = Toplevel()
    #Basic Stuff
    lou.geometry('800x500')
    lou.title('VM - Positive People🙂')

    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    lou.iconphoto(False, varmakerIcon)

    user1 = Label(lou, text="feewully", font=('Calibri', 25, 'bold'))
    user1.grid(row=0, column=0)

    lou.mainloop()

if __name__ == "__main__":
    positiveUsers()