from tkinter import *

def addValueFunc():
    def addValue(item):

        with open("Data\\ertekek.txt", "a") as file:
            file.write(str(item) + "\n")

    def continue2():
        result_valueadd = value_add.get()
        addValue(result_valueadd)
        value_add.delete(0, 'end')
    valueset = Toplevel()
    valueset.title("VM - Add Value")
    valueset.geometry('800x500')

    button_add = PhotoImage(file="button_styles/button_add.png")

    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    valueset.iconphoto(False, varmakerIcon)

    text = Label(valueset, text="Enter here the value you want to add", font=("Calibri", 20))

    value_add = Entry(valueset, font=("Calibri", 20), highlightthickness=2, highlightbackground='black', relief='solid')

    continue_button = Button(valueset, image=button_add,  command=continue2, border=0)

    text.grid(row=0, column=0, pady=(105, 0), padx=(200, 0), columnspan=3)
    value_add.grid(row=1, column=0, padx=260, columnspan=6)
    continue_button.grid(row=2, column=0, padx=(185, 0), columnspan=3)

    valueset.mainloop()

if __name__ == '__main__':
    addValueFunc()