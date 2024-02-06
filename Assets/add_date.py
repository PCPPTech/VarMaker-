from tkinter import *


def addDateFunc():
    def addDate(item):
        with open("Data\\datum.txt", "a") as file:
            file.write(str(item) + "\n")

    def continuelol():
        result_dateadd = date_add.get()
        addDate(result_dateadd)
        date_add.delete(0, 'end')
    dateAdd = Toplevel()
    dateAdd.resizable(False, False)
    dateAdd.title("VM - Add Date")
    dateAdd.geometry("800x500")
    # Change icon photo
    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    dateAdd.iconphoto(False, varmakerIcon)

    button_add = PhotoImage(file="button_styles/button_add.png")


    label = Label(dateAdd, text="Enter here a date to add", font=("Calibri", 20))

    date_add = Entry(dateAdd, font=("Calibri", 20), highlightthickness=2, highlightbackground='black', relief='solid')

    continue_button = Button(dateAdd, image=button_add ,command=continuelol, border=0)

    label.grid(row=0, column=0, pady=(105, 0), padx=(260, 0), columnspan=3)
    date_add.grid(row=1, column=0, padx=260, columnspan=6)
    continue_button.grid(row=2, column=0, padx=(260, 0), columnspan=3)

    dateAdd.mainloop()

if __name__ == "__main__":
    addDateFunc()