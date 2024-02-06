from tkinter import *

def idk10():
    usefulFor = Toplevel()

    usefulFor.title("VM - What is this app useful for?")
    usefulFor.geometry("1400x550")
    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    usefulFor.iconphoto(False, varmakerIcon)

    label = Label(usefulFor, text="It may not be useful for most things, but look, I tried my best.", font=("Calibri", 20))
    label.grid(row=0, column=0, columnspan=1)

    label1 = Label(usefulFor, text="If you are a heavy money spender and if you'd like to save up, you can actually note how much you saved up each month.", font=("Calibri", 20))
    label1.grid(row=1, column=0, columnspan=1)

    label2 = Label(usefulFor, text="If you'd like to see how much money you spend each month, maybe this app is useful for your situation.", font=("Calibri", 20))
    label2.grid(row=2, column=0, columnspan=1)

    usefulFor.mainloop()