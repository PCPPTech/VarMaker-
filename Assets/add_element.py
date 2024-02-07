from tkinter import *
from PIL import Image, ImageTk
def addElementFunc():
    def addElement(item):
        with open("Data\\tetelek.txt", "a") as file:
            file.write(item + "\n")

    def continueLol1():
        elementAnswer = element_ADD.get()
        addElement(elementAnswer)
        element_ADD.delete(0, 'end')


    add_element = Toplevel()
    add_element.title("VM - Add Element")
    add_element.geometry('800x500')

    button_add = PhotoImage(file="button_styles/button_add.png")
    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    add_element.iconphoto(False, varmakerIcon)
    

    title = Label(add_element, text="Enter here the element you want to add", font=("Calibri", 20))
    element_ADD = Entry(add_element, font=("Calibri", 20), highlightthickness=2, highlightbackground='black', relief='solid')
    submitButton = Button(add_element, image=button_add, command=continueLol1, border=0)

    # Grids
    title.grid(row=0, column=0, pady=(105, 0), padx=(45, 0), columnspan=3)
    element_ADD.grid(row=1, column=0, padx=260, columnspan=6)
    submitButton.grid(row=2, column=0, padx=350, columnspan=3)

    add_element.mainloop()

if __name__ == '__main__':
    addElementFunc()