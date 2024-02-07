from tkinter import *

def seeTable():
    with open("Data\\tetelek.txt", "r") as elements_file:
        elements = elements_file.read().splitlines()

    with open("Data\\ertekek.txt", "r") as values_file:
        values = values_file.read().splitlines()
    
    with open("Data\\datum.txt", "r") as dates_file:
        dates = dates_file.read().splitlines()

    window = Toplevel()
    window.resizable(False, False)
    window.title("VM - Table")
    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    window.iconphoto(False, varmakerIcon)
    window.geometry("800x750")
    elements_label = Label(window, text="Elements", font=("Calibri", 20))
    elements_label.grid(row=0, column=0)

    values_label = Label(window, text="Values", font=("Calibri", 20))
    values_label.grid(row=0, column=1, padx=10)

    dates_label = Label(window, text="Date", font=("Calibri", 20))
    dates_label.grid(row=0, column=2, padx=20)

    for i, element in enumerate(elements, start=1):
        element_label = Label(window, text=element, font=("Calibri", 17))
        element_label.grid(row=i, column=0)

    for i, value in enumerate(values, start=1):
        value_label = Label(window, text=value, font=("Calibri", 17))
        value_label.grid(row=i, column=1)

    for i, date in enumerate(dates, start=1):
        date_label = Label(window, text=date, font=("Calibri", 17))
        date_label.grid(row=i, column=2)

    try:
        total = sum(map(int, values))
    except ValueError:
        total = 0

    vit = Label(window, text=f"VIT (Values In Total): {str(total)}", font=("Calibri", 17))
    vit.grid(row=len(elements)+1, columnspan=2, pady=20)

    window.mainloop()

if __name__ == "__main__":
    seeTable()