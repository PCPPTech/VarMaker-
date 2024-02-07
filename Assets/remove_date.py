from tkinter import *

def removeDateFunc():
    def removeDate(item):
        with open("Data\\datum.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip() != str(item):
                    file.write(line)
            file.truncate()

    def continue5():
        result_datermv = date_rmv.get()
        removeDate(result_datermv)
        date_rmv.delete(0, 'end')
    dateRMV = Toplevel()

    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    dateRMV.iconphoto(False, varmakerIcon)

    dateRMV.title("VM - Remove Date")
    dateRMV.geometry("800x500")

    dateRMV.resizable(False, False)

    button_remove = PhotoImage(file="button_styles/button_remove.png")

    title = Label(dateRMV, text="Enter here a date you'd like to remove", font=("Calibri", 20))

    date_rmv = Entry(dateRMV, font=("Calibri", 20), highlightthickness=2, highlightbackground='black', relief='solid')

    continue_Button = Button(dateRMV, image=button_remove, command=continue5, border=0)

    title.grid(row=0, column=0, pady=(105, 0), padx=(150, 0), columnspan=5)
    date_rmv.grid(row=1, column=0, padx=260, columnspan=6)
    continue_Button.grid(row=2, column=0, padx=(125, 0), columnspan=5)
    
    dateRMV.mainloop()

if __name__ == '__main__':
    removeDateFunc()