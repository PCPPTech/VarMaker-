from tkinter import *

def settingsFunction():

    def rememberMeButtonFunctionality():
        with open("Data\\rememberme.txt", "r+") as file:
            file.write("N")
        def close():
            success.destroy()
        success = Tk()
        success.title("Congrats :D")
        operationSuccess = Label(success, text="Operation Success. Feel free to close this window :)", font=("Calibri", 20))
        operationSuccess.pack()
        closewindow = Button(success, text="CLOSE", font=("Calibri", 15), command=close)
        closewindow.pack()
        success.mainloop()
    
    settings = Toplevel()
    settings.geometry("800x500")
    settings.title("VM - Settings")
    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    settings.iconphoto(False, varmakerIcon)

    button_rememberMe = PhotoImage(file="button_styles/button_remember-me.png")

    title = Label(settings, text="Settings", font=("Calibri", 20, 'bold'))
    title.grid(row=0, column=1, columnspan=10)

    rememberMe = Button(settings, image=button_rememberMe, command=rememberMeButtonFunctionality, border=0)
    rememberMe.grid(row=1, column=2)

    settings.mainloop()

if __name__ == "__main__":
    settingsFunction()