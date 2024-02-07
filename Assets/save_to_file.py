from tkinter import *
import os

element_copy = None
value_copy = None
date_copy = None

def saveToFileFunc():
    #? Paths

    element_path_join = os.path.join("..", "VM", "Data", "tetelek.txt")
    value_path_join = os.path.join("..", "VM", "Data", "ertekek.txt")
    date_path_join = os.path.join("..", "VM", "Data", "datum.txt")

    element_path = os.path.realpath(element_path_join)
    value_path = os.path.realpath(value_path_join)
    date_path = os.path.realpath(date_path_join)

    file1_save_element_join = os.path.join("..", "VM", "save_files", "file1_save", "element_save.txt")
    file1_save_value_join = os.path.join("..", "VM", "save_files", "file1_save", "value_save.txt")
    file1_save_date_join = os.path.join("..", "VM", "save_files", "file1_save", "date_save.txt")

    file1_save_element = os.path.realpath(file1_save_element_join)
    file1_save_value = os.path.realpath(file1_save_value_join)
    file1_save_date = os.path.realpath(file1_save_date_join)



    file2_save_element_join = os.path.join("..", "VM", "save_files", "file2_save", "element_save.txt")
    file2_save_value_join = os.path.join("..", "VM", "save_files", "file2_save", "value_save.txt")
    file2_save_date_join = os.path.join("..", "VM", "save_files", "file2_save", "date_save.txt")

    file2_save_element = os.path.realpath(file2_save_element_join)
    file2_save_value = os.path.realpath(file2_save_value_join)
    file2_save_date = os.path.realpath(file2_save_date_join)



    file3_save_element_join = os.path.join("..", "VM", "save_files", "file3_save", "element_save.txt")
    file3_save_value_join = os.path.join("..", "VM", "save_files", "file3_save", "value_save.txt")
    file3_save_date_join = os.path.join("..", "VM", "save_files", "file3_save", "date_save.txt")

    file3_save_element = os.path.realpath(file3_save_element_join)
    file3_save_value = os.path.realpath(file3_save_value_join)
    file3_save_date = os.path.realpath(file3_save_date_join)



    file4_save_element_join = os.path.join("..", "VM", "save_files", "file4_save", "element_save.txt")
    file4_save_value_join = os.path.join("..", "VM", "save_files", "file4_save", "value_save.txt")
    file4_save_date_join = os.path.join("..", "VM", "save_files", "file4_save", "date_save.txt")

    file4_save_element = os.path.realpath(file4_save_element_join)
    file4_save_value = os.path.realpath(file4_save_value_join)
    file4_save_date = os.path.realpath(file4_save_date_join)



    file5_save_element_join = os.path.join("..", "VM", "save_files", "file5_save", "element_save.txt")
    file5_save_value_join = os.path.join("..", "VM", "save_files", "file5_save", "value_save.txt")
    file5_save_date_join = os.path.join("..", "VM", "save_files", "file5_save", "date_save.txt")

    file5_save_element = os.path.realpath(file5_save_element_join)
    file5_save_value = os.path.realpath(file5_save_value_join)
    file5_save_date = os.path.realpath(file5_save_date_join)



    file6_save_element_join = os.path.join("..", "VM", "save_files", "file6_save", "element_save.txt")
    file6_save_value_join = os.path.join("..", "VM", "save_files", "file6_save", "value_save.txt")
    file6_save_date_join = os.path.join("..", "VM", "save_files", "file6_save", "date_save.txt")

    file6_save_element = os.path.realpath(file6_save_element_join)
    file6_save_value = os.path.realpath(file6_save_value_join)
    file6_save_date = os.path.realpath(file6_save_date_join)



    #Functions

    def save1():
        global element_copy
        global value_copy
        global date_copy


        

        with open(element_path, "r+") as file:
            element_copy = file.readlines()
            with open(file1_save_element, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in element_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        with open(date_path, "r+") as file:
            date_copy = file.readlines()
            with open(file1_save_date, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()

                else:
                    for i in date_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        with open(value_path, "r+") as file:
            value_copy = file.readlines()
            with open(file1_save_value, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()

                else:
                    for i in value_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()

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

    def save2():
        global element_copy
        global value_copy
        global date_copy


        with open(element_path, "r+") as file:
            element_copy = file.readlines()
            with open(file2_save_element, "r+") as file2:

                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                
                else:
                    for i in element_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        with open(date_path, "r+") as file:
            date_copy = file.readlines()
            with open(file2_save_date, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()

                else:
                    for i in date_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        with open(value_path, "r+") as file:
            value_copy = file.readlines()
            with open(file2_save_value, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()

                else:
                    for i in value_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        done1 = Toplevel()
        done1.title('VM - Operation Success')
        varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
        done1.iconphoto(False, varmakerIcon)
            
        def q():
            done1.destroy()

        removeDone1 = Label(done1, text="Operation Done! Feel free to close this window!", font=("Calibri", 15))
        close1 = Button(done1, text="CLOSE", font=("Calibri", 15), command=q)

        removeDone1.pack()
        close1.pack()

        done1.mainloop()

    def save3():
        global element_copy
        global value_copy
        global date_copy

        with open(element_path, "r+") as file:
            element_copy = file.readlines()
            with open(file3_save_element, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in element_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        with open(date_path, "r+") as file:
            date_copy = file.readlines()
            with open(file3_save_date, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in date_copy:
                        file2.write(i)
                    date_path.seek(0)
                    date_path.truncate()
        
        with open(value_path, "r+") as file:
            value_copy = file.readlines()
            with open(file3_save_value, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in value_copy:
                        file2.write(i)
                    value_path.seek(0)
                    value_path.truncate()
                
        done2 = Toplevel()
        done2.title('VM - Operation Success')
        varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
        done2.iconphoto(False, varmakerIcon)
            
        def q():
            done2.destroy()

        removeDone2 = Label(done2, text="Operation Done! Feel free to close this window!", font=("Calibri", 15))
        close2 = Button(done2, text="CLOSE", font=("Calibri", 15), command=q)

        removeDone2.pack()
        close2.pack()

        done2.mainloop()

    def save4():
        global element_copy
        global value_copy
        global date_copy

        with open(element_path, "r+") as file:
            element_copy = file.readlines()
            with open(file4_save_element, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in element_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        with open(date_path, "r+") as file:
            date_copy = file.readlines()
            with open(file4_save_date, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in date_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        with open(value_path, "r+") as file:
            value_copy = file.readlines()
            with open(file4_save_value, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in value_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()

        done3 = Toplevel()
        done3.title('VM - Operation Success')
        varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
        done3.iconphoto(False, varmakerIcon)
            
        def q():
            done3.destroy()

        removeDone3 = Label(done3, text="Operation Done! Feel free to close this window!", font=("Calibri", 15))
        close3 = Button(done3, text="CLOSE", font=("Calibri", 15), command=q)

        removeDone3.pack()
        close3.pack()

        done3.mainloop()  

    def save5():
        global element_copy
        global value_copy
        global date_copy


        with open(element_path, "r+") as file:
            element_copy = file.readlines()
            with open(file5_save_element, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in element_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        with open(date_path, "r+") as file:
            date_copy = file.readlines()
            with open(file5_save_date, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in date_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        with open(value_path, "r+") as file:
            value_copy = file.readlines()
            with open(file5_save_value, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in value_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        done4 = Toplevel()
        done4.title('VM - Operation Success')
        varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
        done4.iconphoto(False, varmakerIcon)
            
        def q():
            done4.destroy()

        removeDone4 = Label(done4, text="Operation Done! Feel free to close this window!", font=("Calibri", 15))
        close4 = Button(done4, text="CLOSE", font=("Calibri", 15), command=q)

        removeDone4.pack()
        close4.pack()

        done4.mainloop()
        
      
    def save6():
        global element_copy
        global value_copy
        global date_copy


        with open(element_path, "r+") as file:
            element_copy = file.readlines()
            with open(file6_save_element, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in element_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        with open(date_path, "r+") as file:
            date_copy = file.readlines()
            with open(file6_save_date, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in date_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        with open(value_path, "r+") as file:
            value_copy = file.readlines()
            with open(file6_save_value, "r+") as file2:
                if len(file2.readlines()) >= 1:
                    failed = Toplevel()
                    failed.title('VM - Error')
                    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
                    failed.iconphoto(False, varmakerIcon)

                    def quitWindow():
                        failed.destroy()

                    errorLabel = Label(failed, text="ERROR: This save file already has some element in it. Please use the 'Remove Save' function to remove elements from this file save.", font=("Calibri", 15))
                    errorLabel.pack()

                    closebtn = Button(failed, text="CLOSE", font=("Calibri", 15), command=quitWindow)
                    closebtn.pack()

                    failed.mainloop()
                else:
                    for i in value_copy:
                        file2.write(i)
                    file.seek(0)
                    file.truncate()
        
        done5 = Toplevel()
        done5.title('VM - Operation Success')
        varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
        done5.iconphoto(False, varmakerIcon)
            
        def q():
            done5.destroy()

        removeDone5 = Label(done5, text="Operation Done! Feel free to close this window!", font=("Calibri", 15))
        close5 = Button(done5, text="CLOSE", font=("Calibri", 15), command=q)

        removeDone5.pack()
        close5.pack()

        done5.mainloop()

        
         

    saveMenu = Toplevel()
    saveMenu.geometry("1100x500")
    saveMenu.title("VM - Save to File")
    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    saveMenu.iconphoto(False, varmakerIcon)

    #Buttons
    file_save1_btn = PhotoImage(file="button_styles/button_file-1.png")
    file_save2_btn = PhotoImage(file="button_styles/button_file-2.png")
    file_save3_btn = PhotoImage(file="button_styles/button_file-3.png")
    file_save4_btn = PhotoImage(file="button_styles/button_file-4.png")
    file_save5_btn = PhotoImage(file="button_styles/button_file-5.png")
    file_save6_btn = PhotoImage(file="button_styles/button_file-6.png")
    


    title = Label(saveMenu, text="Select a file to save", font=("Calibri", 30, 'bold'))
    warning = Label(saveMenu, text="!!! If you don't see any pop-up windows saying the operation was success, it's not an error. Just click the button once, and the file will just load perfectly. !!!", font=("Calibri", 12))

    title.pack()
    warning.pack()

    file_save1 = Button(saveMenu, image=file_save1_btn, border=0, command=save1)
    file_save1.pack()

    file_save2 = Button(saveMenu, image=file_save2_btn, border=0, command=save2)
    file_save2.pack()

    file_save3 = Button(saveMenu, image=file_save3_btn, border=0, command=save3)
    file_save3.pack()

    file_save4 = Button(saveMenu, image=file_save4_btn, border=0, command=save4)
    file_save4.pack()

    file_save5 = Button(saveMenu, image=file_save5_btn, border=0, command=save5)
    file_save5.pack()

    file_save6 = Button(saveMenu, image=file_save6_btn, border=0, command=save6)
    file_save6.pack()
    

    saveMenu.mainloop()

if __name__ == "__main__":
    saveToFileFunc()