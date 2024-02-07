from tkinter import *
import os

def RemoveSaveFunc():
    #? File Path (Join)

    element_path_join = os.path.join("..", "VM", "Data", "tetelek.txt")
    value_path_join = os.path.join("..", "VM", "Data", "ertekek.txt")
    date_path_join = os.path.join("..", "VM", "Data", "datum.txt")

    file1_save_element_join = os.path.join("..", "VM", "save_files", "file1_save", "element_save.txt")
    file1_save_value_join = os.path.join("..", "VM", "save_files", "file1_save", "value_save.txt")
    file1_save_date_join = os.path.join('..', 'VM', 'save_files', 'file1_save', 'date_save.txt')
    

    file2_save_element_join = os.path.join("..", "VM", "save_files", "file2_save", "element_save.txt")
    file2_save_value_join = os.path.join("..", "VM", "save_files", "file2_save", "value_save.txt")
    file2_save_date_join = os.path.join('..', 'VM', 'save_files', 'file2_save', 'date_save.txt')
    

    file3_save_element_join = os.path.join("..", "VM", "save_files", "file3_save", "element_save.txt")
    file3_save_value_join = os.path.join("..", "VM", "save_files", "file3_save", "value_save.txt")
    file3_save_date_join = os.path.join('..', 'VM', 'save_files', 'file3_save', 'date_save.txt')
    

    file4_save_element_join = os.path.join("..", "VM", "save_files", "file4_save", "element_save.txt")
    file4_save_value_join = os.path.join("..", "VM", "save_files", "file4_save", "value_save.txt")
    file4_save_date_join = os.path.join('..', 'VM', 'save_files', 'file4_save', 'date_save.txt')
    

    file5_save_element_join = os.path.join("..", "VM", "save_files", "file5_save", "element_save.txt")
    file5_save_value_join = os.path.join("..", "VM", "save_files", "file5_save", "value_save.txt")
    file5_save_date_join = os.path.join('..', 'VM', 'save_files', 'file5_save', 'date_save.txt')
    

    file6_save_element_join = os.path.join("..", "VM", "save_files", "file6_save", "element_save.txt")
    file6_save_value_join = os.path.join("..", "VM", "save_files", "file6_save", "value_save.txt")
    file6_save_date_join = os.path.join('..', 'VM', 'save_files', 'file6_save', 'date_save.txt')
    
    
    #? File Path (Realpath)

    element_path = os.path.realpath(element_path_join)
    value_path = os.path.realpath(value_path_join)
    date_path = os.path.realpath(date_path_join)

    file1_save_element = os.path.realpath(file1_save_element_join)
    file1_save_value = os.path.realpath(file1_save_value_join)
    file1_save_date = os.path.realpath(file1_save_date_join)

    file2_save_element = os.path.realpath(file2_save_element_join)
    file2_save_value = os.path.realpath(file2_save_value_join)
    file2_save_date = os.path.realpath(file2_save_date_join)

    file3_save_element = os.path.realpath(file3_save_element_join)
    file3_save_value = os.path.realpath(file3_save_value_join)
    file3_save_date = os.path.realpath(file3_save_date_join)

    file4_save_element = os.path.realpath(file4_save_element_join)
    file4_save_value = os.path.realpath(file4_save_value_join)
    file4_save_date = os.path.realpath(file4_save_date_join)

    file5_save_element = os.path.realpath(file5_save_element_join)
    file5_save_value = os.path.realpath(file5_save_value_join)
    file5_save_date = os.path.realpath(file5_save_date_join)

    file6_save_element = os.path.realpath(file6_save_element_join)
    file6_save_value = os.path.realpath(file6_save_value_join)
    file6_save_date = os.path.realpath(file6_save_date_join)

    #? Buttons Styles Path

    file1_button = PhotoImage(file="button_styles/button_file-1.png")
    file2_button = PhotoImage(file="button_styles/button_file-2.png")
    file3_button = PhotoImage(file="button_styles/button_file-3.png")
    file4_button = PhotoImage(file="button_styles/button_file-4.png")
    file5_button = PhotoImage(file="button_styles/button_file-5.png")
    file6_button = PhotoImage(file="button_styles/button_file-6.png")
    
    button_continue = PhotoImage(file="button_styles/button_continue.png")
    

    #! FUNCTIONS
    def removeSave1():
        
        def continueFunc():
            with open(file1_save_element, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file1_save_value, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file1_save_date, "r+") as file:
                file.seek(0)
                file.truncate()
            jtms.destroy()

            done = Toplevel()
            done.title('VM - Operation Success')
            varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
            done.iconphoto(False, varmakerIcon)
            
            def q():
                done.destroy()

            removeDone = Label(done, text="Operation Done! Feel free to close this window!", font=("Calibri", 15))
            close = Button(done, text="CLOSE", font=("Calibri", 15), command=q)

            removeDone.pack()
            close.pack()

            done.mainloop()

        jtms = Toplevel()
        varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
        jtms.iconphoto(False, varmakerIcon)
        jtms.geometry('1100x200')

        warning = Label(jtms, text="BY CLICKING 'Continue' YOU ARE SENDING THIS FILE SAVE TO THE SHADOW REALM. ARE YOU POSITIVE YOU'D LIKE TO CONTINUE?", font=('Calibri', 15))
        
        cont_button = Button(jtms, image=button_continue, border=0, command=continueFunc)

        warning.pack()
        cont_button.pack()

        jtms.mainloop()

    def removeSave2():
        
        def continueFunc2():
            with open(file2_save_element, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file2_save_value, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file2_save_date, "r+") as file:
                file.seek(0)
                file.truncate()
            jtms1.destroy()

        jtms1 = Toplevel()
        varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
        jtms1.iconphoto(False, varmakerIcon)
        jtms1.geometry('1100x200')

        warning1 = Label(jtms1, text="BY CLICKING 'Continue' YOU ARE SENDING THIS FILE SAVE TO THE SHADOW REALM. ARE YOU POSITIVE YOU'D LIKE TO CONTINUE?", font=('Calibri', 15))
        
        cont_button1 = Button(jtms1, image=button_continue, border=0, command=continueFunc2)

        warning1.pack()
        cont_button1.pack()

        jtms1.mainloop()

    def removeSave3():
        
        def continueFunc3():
            with open(file3_save_element, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file3_save_value, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file3_save_date, "r+") as file:
                file.seek(0)
                file.truncate()
            jtms2.destroy()

        jtms2 = Toplevel()
        varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
        jtms2.iconphoto(False, varmakerIcon)
        jtms2.geometry('1100x200')

        warning = Label(jtms2, text="BY CLICKING 'Continue' YOU ARE SENDING THIS FILE SAVE TO THE SHADOW REALM. ARE YOU POSITIVE YOU'D LIKE TO CONTINUE?", font=('Calibri', 15))
        
        cont_button = Button(jtms2, image=button_continue, border=0, command=continueFunc3)

        warning.pack()
        cont_button.pack()

        jtms2.mainloop()

    def removeSave4():
        
        def continueFunc4():
            with open(file4_save_element, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file4_save_value, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file4_save_date, "r+") as file:
                file.seek(0)
                file.truncate()
            jtms4.destroy()

        jtms4 = Toplevel()
        varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
        jtms4.iconphoto(False, varmakerIcon)
        jtms4.geometry('1100x200')

        warning = Label(jtms4, text="BY CLICKING 'Continue' YOU ARE SENDING THIS FILE SAVE TO THE SHADOW REALM. ARE YOU POSITIVE YOU'D LIKE TO CONTINUE?", font=('Calibri', 15))
        
        cont_button = Button(jtms4, image=button_continue, border=0, command=continueFunc4)

        warning.pack()
        cont_button.pack()

        jtms4.mainloop()

    def removeSave5():
        
        def continueFunc5():
            with open(file5_save_element, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file5_save_value, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file5_save_date, "r+") as file:
                file.seek(0)
                file.truncate()
            jtms5.destroy()

        jtms5 = Toplevel()
        varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
        jtms5.iconphoto(False, varmakerIcon)
        jtms5.geometry('1100x200')

        warning = Label(jtms5, text="BY CLICKING 'Continue' YOU ARE SENDING THIS FILE SAVE TO THE SHADOW REALM. ARE YOU POSITIVE YOU'D LIKE TO CONTINUE?", font=('Calibri', 15))
        
        cont_button = Button(jtms5, image=button_continue, border=0, command=continueFunc5)

        warning.pack()
        cont_button.pack()

        jtms5.mainloop()

    def removeSave6():
        
        def continueFunc6():
            with open(file6_save_element, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file6_save_value, "r+") as file:
                file.seek(0)
                file.truncate()
            with open(file6_save_date, "r+") as file:
                file.seek(0)
                file.truncate()
            jtms6.destroy()

        jtms6 = Toplevel()
        varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
        jtms6.iconphoto(False, varmakerIcon)
        jtms6.geometry('1100x200')

        warning = Label(jtms6, text="BY CLICKING 'Continue' YOU ARE SENDING THIS FILE SAVE TO THE SHADOW REALM. ARE YOU POSITIVE YOU'D LIKE TO CONTINUE?", font=('Calibri', 15))
        
        cont_button = Button(jtms6, image=button_continue, border=0, command=continueFunc6)

        warning.pack()
        cont_button.pack()

        jtms6.mainloop()

    
    #* Menu

    removeSaveMenu = Toplevel()
    removeSaveMenu.geometry('1100x500')
    removeSaveMenu.title('VM - Remove Save')
    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    removeSaveMenu.iconphoto(False, varmakerIcon)

    title = Label(removeSaveMenu, text="Select a save to remove", font=("Calibri", 30, 'bold'))
    warning = Label(removeSaveMenu, text="!!! If you don't see any pop-up windows saying the operation was success, it's not an error. Just click the button once, and the file will just remove the save perfectly. !!!", font=("Calibri", 12))

    title.pack()
    warning.pack()

    file1btn = Button(removeSaveMenu, image=file1_button, border=0, command=removeSave1)
    file1btn.pack()

    file2btn = Button(removeSaveMenu, image=file2_button, border=0, command=removeSave2)
    file2btn.pack()

    file3btn = Button(removeSaveMenu, image=file3_button, border=0, command=removeSave3)
    file3btn.pack()

    file4btn = Button(removeSaveMenu, image=file4_button, border=0, command=removeSave4)
    file4btn.pack()

    file5btn = Button(removeSaveMenu, image=file5_button, border=0, command=removeSave5)
    file5btn.pack()

    file6btn = Button(removeSaveMenu, image=file6_button, border=0, command=removeSave6)
    file6btn.pack()


    removeSaveMenu.mainloop()


if __name__ == "__main__":
    RemoveSaveFunc()