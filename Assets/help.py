from tkinter import *

def helpFunc():
    help = Toplevel()
    help.geometry("800x500")
    help.title("VM - Help")

    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    help.iconphoto(False, varmakerIcon)

    question1 = Label(help, text="HOW TO USE VARMAKER?", font=("Calibri", 20, "bold"))
    question1.grid(row=0, column=0)
    
    answer1 = Label(help, text="Simple. Kinda like Excel. Add elements with the", font=("Calibri", 15))
    answer1.grid(row=1, column=0)
    
    answer1_continue = Label(help, text="'Add Element' button, add value, date, with the", font=("Calibri", 15))
    answer1_continue.grid(row=2, column=0)
    
    answer1_continue1 = Label(help, text="'Add Value', 'Add Date' button. To see the results, click on 'See Table' button.", font=("Calibri", 15))
    answer1_continue1.grid(row=3, column=0)
    
    help.mainloop()

if __name__ == "__main__":
    helpFunc()