from tkinter import *

def reportProblems():
    report = Toplevel()
    report.title("VM - Report Bugs")
    report.iconphoto(False, PhotoImage(file="Varmaker ICON/varmaker-logo.png"))

    label = Label(report, text="Report bugs or problems here: discord.gg/justarandomdiscordserver", font=("Calibri", 20, "bold"))
    label.pack()

    report.mainloop()

if __name__ == "__main__":
    reportProblems()