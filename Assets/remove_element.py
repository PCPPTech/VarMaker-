from tkinter import *

def removeElementFunc():
    def removeElement(item):
        with open("Data\\tetelek.txt", "r+") as file:
            files = file.readlines()
            file.seek(0)
            for i in files:
                if i.strip() != item:
                    file.write(str(item) + "\n")
                file.truncate()

    def continue3():
        result_elementrmv = element_rmv.get()
        removeElement(result_elementrmv)
        element_rmv.delete(0, 'end')

    elementRMV = Toplevel()

    elementRMV.title("VM - Remove Element")
    elementRMV.geometry("800x500")

    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    elementRMV.iconphoto(False, varmakerIcon)

    elementRMV.resizable(False, False)

    button_remove = PhotoImage(file="button_styles/button_remove.png")

    label = Label(elementRMV, text="Enter here the element you'd like to remove", font=("Calibri", 20))

    element_rmv = Entry(elementRMV, font=("Calibri", 20), highlightthickness=2, highlightbackground='black', relief='solid')

    continue_button = Button(elementRMV, image=button_remove, command=continue3, border=0)

    label.grid(row=0, column=0, pady=(105, 0), padx=(175, 0), columnspan=3)
    element_rmv.grid(row=1, column=0, padx=260, columnspan=6)
    continue_button.grid(row=2, column=0, padx=(150, 0), columnspan=3)

    elementRMV.mainloop()

if __name__ == '__main__':
    removeElementFunc()