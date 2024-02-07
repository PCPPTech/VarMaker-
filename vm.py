
# System imports
import os, time
from tkinter import *
from PIL import Image, ImageTk
import webbrowser
# Function, variable, class, and much more imports
from Assets.add_date import addDateFunc
from Assets.add_value import addValueFunc
from Assets.add_element import addElementFunc
from Assets.remove_date import removeDateFunc
from Assets.remove_value import removeValueFunc
from Assets.remove_element import removeElementFunc
from Assets.donate import donateFunc
from Assets.feedback import feedbackFunction
from Assets.app_use import idk10
from Assets.report_problems import reportProblems
from Assets.list_of_positive_users import positiveUsers
from Assets.see_table import seeTable
from Assets.settings import settingsFunction
from Assets.help import helpFunc
from Assets.bored import Bored
from Assets.news import newsFunc
from Assets.save_to_file import saveToFileFunc
from Assets.load_saved_file import loadFile
from Assets.remove_save import RemoveSaveFunc
from Assets.visit_website import OpenWebsite


if os.path.isfile("Data\\tetelek.txt"):
    pass
else:
    f = open("Data\\tetelek.txt", "x")

if os.path.isfile("Data\\ertekek.txt"):
    pass
else:
    v = open("Data\\ertekek.txt", "x")

if os.path.isfile("Data\\datum.txt"):
    pass
else:
    lol = open("Data\\datum.txt", "x")

if os.path.isfile("Data\\rememberme.txt"):
    pass
else:
    rememberyaxd = open("Data\\rememberme.txt")

def exit():
    quit()


#menu
def menu():

    menu = Tk()
    # Button Styles
    button_addElement = PhotoImage(file="button_styles/button_add-element.png")
    button_addValue = PhotoImage(file="button_styles/button_add-value.png")
    button_addDate = PhotoImage(file="button_styles/button_add-date.png")

    button_removeElement = PhotoImage(file="button_styles/button_remove-element.png")
    button_removeValue = PhotoImage(file="button_styles/button_remove-value.png")
    button_removeDate = PhotoImage(file="button_styles/button_remove-date.png")

    button_apps_use = PhotoImage(file="button_styles/button_apps-use.png")
    button_bored = PhotoImage(file="button_styles/button_bored.png")
    button_help = PhotoImage(file="button_styles/button_help.png")
    button_donate = PhotoImage(file="button_styles/button_donate.png")
    button_progress = PhotoImage(file="button_styles/button_app-progress.png")
    button_send_feedback = PhotoImage(file="button_styles/button_send-feedback.png")
    button_settings = PhotoImage(file="button_styles/button_settings.png")

    button_see_table = PhotoImage(file="button_styles/button_see-table.png")
    button_report_bugs = PhotoImage(file="button_styles/button_report-bugs.png")
    button_app_progress = PhotoImage(file="button_styles/button_app-progress.png")
    button_SaveFile = PhotoImage(file="button_styles/button_save-to-a-file.png")
    button_LoadFile = PhotoImage(file="button_styles/button_load-save.png")
    button_RemoveFile = PhotoImage(file="button_styles/button_remove-save.png")
    button_see_website = PhotoImage(file="button_styles/button_go-to-website.png")

    iconPhoto = PhotoImage(file="Varmaker ICON/varmaker-logo.png")

    menu.geometry("925x585")
    menu.title("VM - Menu")
    menu.iconphoto(False, iconPhoto)
    menu.resizable(False, False)

    title = Label(menu, text=" VARMAKER™", font=("Calibri", 25, 'bold'))
    title.grid(row=0, column=1, columnspan=10)

    choice1 = Button(menu, font=("Calibri", 15), command=addElementFunc, image=button_addElement, border=0)
    choice1.grid(row=1, column=2)

    choice2 = Button(menu, font=("Calibri", 15),  command=addValueFunc, image=button_addValue, border=0)
    choice2.grid(row=2, column=2)

    choice3 = Button(menu, font=("Calibri", 15), command=addDateFunc, image=button_addDate, border=0)
    choice3.grid(row=3, column=2)

    choice4 = Button(menu, font=("Calibri", 15), command=removeElementFunc, image=button_removeElement, border=0)
    choice4.grid(row=1, column=3, padx=30)

    choice5 = Button(menu, font=("Calibri", 15), command=removeValueFunc, image=button_removeValue, border=0)
    choice5.grid(row=2, column=3, padx=10)

    choice6 = Button(menu, font=("Calibri", 15), command=removeDateFunc, image=button_removeDate, border=0)
    choice6.grid(row=3, column=3, padx=10)

    choice7 = Button(menu, font=("Calibri", 15), command=seeTable, image=button_see_table, border=0)
    choice7.grid(row=4, column=3, padx=10)

    choice8 = Button(menu, font=("Calibri", 15), command=settingsFunction, image=button_settings, border=0)
    choice8.grid(row=1, column=4, padx=10)

    choice9 = Button(menu, font=("Calibri", 15), command=feedbackFunction, image=button_send_feedback, border=0)
    choice9.grid(row=2, column=4, padx=10)

    choice10 = Button(menu, font=("Calibri", 15), command=donateFunc, image=button_donate, border=0)
    choice10.grid(row=3, column=4, padx=10)

    choice11 = Button(menu, font=("Calibri", 15), command=helpFunc, image=button_help, border=0)
    choice11.grid(row=4, column=4, padx=10)

    choice12 = Button(menu, font=("Calibri", 15), command=idk10, image=button_apps_use, border=0)
    choice12.grid(row=1, column=5, padx=10)

    choice13 = Button(menu, font=("Calibri", 15), command=Bored, image=button_bored, border=0, state=DISABLED)
    choice13.grid(row=2, column=5, padx=10)
    
    choice14 = Button(menu, font=("Calibri", 15), command=reportProblems, image=button_report_bugs, border=0)
    choice14.grid(row=3, column=5, padx=10)

    choice15 = Button(menu, image=button_app_progress, border=0, command=newsFunc)
    choice15.grid(row=5, column=3)

    choice16 = Button(menu, image=button_SaveFile, border=0, command=saveToFileFunc)
    choice16.grid(row=4, column=2)

    choice17 = Button(menu, image=button_LoadFile, border=0, command=loadFile)
    choice17.grid(row=5, column=2)

    choice18 = Button(menu, image=button_RemoveFile, border=0, command=RemoveSaveFunc)
    choice18.grid(row=6, column=2)

    choice19 = Button(menu, image=button_see_website, border=0, command=OpenWebsite)
    choice19.grid(row=6, column=3)

    menu.mainloop()


#password verification
def verify():
    if passwordver.get() == "{@31vZq0/eJ":
        password.destroy()
        menu()
    else:
        print("Error: Incorrect password.")
        quit()

result = ""

with open("Data\\rememberme.txt", "r+") as file:
    lines = file.readlines()
    for i in lines:
        if i == "N":
            result = "passed"
        else:
            result = "failed"

if result == "passed":
    menu()
else:
    password = Tk()
    
    url = "https://varmakerblog.wordpress.com/"
    new = 1

    def openToS():
        webbrowser.open(url, new=new)

    password.geometry('1700x800')
    password.resizable(False, False)
    password.title("Password Verification")

    button_continue = PhotoImage(file="button_styles/button_continue.png")
    button_tos = PhotoImage(file="button_styles/button_terms-of-service.png")

    varmakerIcon = Image.open("Varmaker ICON/varmaker-logo.png")
    resized = varmakerIcon.resize((900, 800), Image.BICUBIC)
    converted_image = ImageTk.PhotoImage(resized)

    varmakerIcon2 = PhotoImage(file="Varmaker ICON/varmaker-logo-2.png")
    password.iconphoto(False, varmakerIcon2)

    side_chick = Label(password, image=converted_image)
    side_chick.pack(side=LEFT)

    label = Label(password, text="Enter Password:", font=("Calibri", 12))
    label.pack()

    pls = Label(password, text="By pressing 'Continue', you'll automatically agree to my ToS.", font=('Fixedsys', 12))
    pls.pack()

    label2 = Label(password, text="The code can be found in the 'HOWTOSETUP.txt' file. If you don't like this feature, report at my discord server: https://discord.gg/xQXnhtpnNf")
    label2.pack()

    passwordver = Entry(password, font=("Calibri", 20), show="*", border=3, relief='solid')
    passwordver.pack()

    continue_button = Button(password, image=button_continue, command=verify, border=0)
    continue_button.pack()

    tos_button = Button(password, image=button_tos, border=0, command=openToS)
    tos_button.pack()

    password.mainloop()