from tkinter import *

def removeValueFunc():
    def removeValue(item):
        with open("Data\\ertekek.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip() != str(item):
                    file.write(line)
            file.truncate()

    def continue4():
        result_valuermv = value_rmv.get()
        removeValue(result_valuermv)
        value_rmv.delete(0, 'end')


    valueRMV = Toplevel()

    valueRMV.title("VM - Remove Value")
    valueRMV.geometry('800x500')
    valueRMV.resizable(False, False)

    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    valueRMV.iconphoto(False, varmakerIcon)

    button_remove = PhotoImage(file="button_styles/button_remove.png")

    label = Label(valueRMV, text="Enter here the value you'd like to remove", font=("Calibri", 20))

    value_rmv = Entry(valueRMV, font=("Calibri", 20), highlightthickness=2, highlightbackground='black', relief='solid')

    continue_button = Button(valueRMV, image=button_remove, border=0, command=continue4)

    label.grid(row=0, column=0, pady=(105, 0), padx=(45, 0), columnspan=3)
    value_rmv.grid(row=1, column=0, padx=260, columnspan=6)
    continue_button.grid(row=2, column=0, padx=350, columnspan=3)

    valueRMV.mainloop()

if __name__ == '__main__':
    removeValueFunc()