from tkinter import *

def feedbackFunction():
    feedback = Toplevel()
    feedback.resizable(False, False)

    feedback.title("VM - Send Feedback")
    feedback.geometry("800x500")

    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    feedback.iconphoto(False, varmakerIcon)

    label = Label(feedback, text="If you have any recomendations to improve this app,", font=("Calibri", 20))
    label.pack()

    label2 = Label(feedback, text="feel free to contact me at eidnoxon213@gmail.com", font=("Calibri", 20))
    label2.pack()

    feedback.mainloop()