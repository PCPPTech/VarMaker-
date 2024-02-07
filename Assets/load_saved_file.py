from tkinter import *
import os

def loadFile():
    #? File Paths
    element_path_join = os.path.join("..", "VM", "Data", "tetelek.txt")
    value_path_join = os.path.join("..", "VM", "Data", "ertekek.txt")
    date_path_join = os.path.join("..", "VM", "Data", "datum.txt")

    element_path = os.path.realpath(element_path_join)
    value_path = os.path.realpath(value_path_join)
    date_path = os.path.realpath(date_path_join)

    #? Saved File Data .txt file path

    file1_save_element_join = os.path.join("..", "VM", "save_files", "file1_save", "element_save.txt")
    file1_save_value_join = os.path.join("..", "VM", "save_files", "file1_save", "value_save.txt")
    file1_save_date_join = os.path.join("..", "VM", "save_files", "file1_save", "date_save.txt")

    file2_save_element_join = os.path.join("..", "VM", "save_files", "file2_save", "element_save.txt")
    file2_save_value_join = os.path.join("..", "VM", "save_files", "file2_save", "value_save.txt")
    file2_save_date_join = os.path.join("..", "VM", "save_files", "file2_save", "date_save.txt")

    file3_save_element_join = os.path.join("..", "VM", "save_files", "file3_save", "element_save.txt")
    file3_save_value_join = os.path.join("..", "VM", "save_files", "file3_save", "value_save.txt")
    file3_save_date_join = os.path.join("..", "VM", "save_files", "file3_save", "date_save.txt")

    file4_save_element_join = os.path.join("..", "VM", "save_files", "file4_save", "element_save.txt")
    file4_save_value_join = os.path.join("..", "VM", "save_files", "file4_save", "value_save.txt")
    file4_save_date_join = os.path.join("..", "VM", "save_files", "file4_save", "date_save.txt")

    file5_save_element_join = os.path.join("..", "VM", "save_files", "file5_save", "element_save.txt")
    file5_save_value_join = os.path.join("..", "VM", "save_files", "file5_save", "value_save.txt")
    file5_save_date_join = os.path.join("..", "VM", "save_files", "file5_save", "date_save.txt")

    file6_save_element_join = os.path.join("..", "VM", "save_files", "file6_save", "element_save.txt")
    file6_save_value_join = os.path.join("..", "VM", "save_files", "file6_save", "value_save.txt")
    file6_save_date_join = os.path.join("..", "VM", "save_files", "file6_save", "date_save.txt")

    #? Path Joints

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

    
    

    #! Functions
    def loadFile1():
        with open(element_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file1_save_element, "r+") as file2:

                lines2 = file2.readlines()
                file2.seek(0)

                for i in lines2:
                    file.write(i)
        
        with open(value_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass


            with open(file1_save_value, "r+") as f2:
                l2 = f2.readlines()
                f2.seek(0)
                for i in l2:
                    file.write(i)
        

        with open(date_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file1_save_date, "r+") as file1:
                lines1 = file1.readlines()
                file1.seek(0)
                for i in lines1:
                    file.write(i)

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

    def loadFile2():
        with open(element_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file2_save_element, "r+") as file2:

                lines2 = file2.readlines()
                file2.seek(0)

                for i in lines2:
                    file.write(i)
        
        with open(value_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass


            with open(file2_save_value, "r+") as f2:
                l2 = f2.readlines()
                f2.seek(0)
                for i in l2:
                    file.write(i)
        

        with open(date_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file2_save_date, "r+") as file1:
                lines1 = file1.readlines()
                file1.seek(0)
                for i in lines1:
                    file.write(i)
                
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

    def loadFile3():
        with open(element_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file3_save_element, "r+") as file2:

                lines2 = file2.readlines()
                file2.seek(0)

                for i in lines2:
                    file.write(i)
        
        with open(value_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass


            with open(file3_save_value, "r+") as f2:
                l2 = f2.readlines()
                f2.seek(0)
                for i in l2:
                    file.write(i)
        

        with open(date_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file3_save_date, "r+") as file1:
                lines1 = file1.readlines()
                file1.seek(0)
                for i in lines1:
                    file.write(i)

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


    def loadFile4():
        with open(element_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file4_save_element, "r+") as file2:

                lines2 = file2.readlines()
                file2.seek(0)

                for i in lines2:
                    file.write(i)
        
        with open(value_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass


            with open(file4_save_value, "r+") as f2:
                l2 = f2.readlines()
                f2.seek(0)
                for i in l2:
                    file.write(i)
        

        with open(date_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file4_save_date, "r+") as file1:
                lines1 = file1.readlines()
                file1.seek(0)
                for i in lines1:
                    file.write(i)

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

    def loadFile5():
        with open(element_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file5_save_element, "r+") as file2:

                lines2 = file2.readlines()
                file2.seek(0)

                for i in lines2:
                    file.write(i)
        
        with open(value_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass


            with open(file5_save_value, "r+") as f2:
                l2 = f2.readlines()
                f2.seek(0)
                for i in l2:
                    file.write(i)
        

        with open(date_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file5_save_date, "r+") as file1:
                lines1 = file1.readlines()
                file1.seek(0)
                for i in lines1:
                    file.write(i)

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

    def loadFile6():
        with open(element_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file6_save_element, "r+") as file2:

                lines2 = file2.readlines()
                file2.seek(0)

                for i in lines2:
                    file.write(i)
        
        with open(value_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass


            with open(file6_save_value, "r+") as f2:
                l2 = f2.readlines()
                f2.seek(0)
                for i in l2:
                    file.write(i)
        

        with open(date_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if len(lines) >= 1:
                file.truncate()
            else:
                pass

            with open(file6_save_date, "r+") as file1:
                lines1 = file1.readlines()
                file1.seek(0)
                for i in lines1:
                    file.write(i)

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


    loadFile = Toplevel()
    file_loadFile1_btn = PhotoImage(file="button_styles/button_file-1.png")
    file_loadFile2_btn = PhotoImage(file="button_styles/button_file-2.png")
    file_loadFile3_btn = PhotoImage(file="button_styles/button_file-3.png")
    file_loadFile4_btn = PhotoImage(file="button_styles/button_file-4.png")
    file_loadFile5_btn = PhotoImage(file="button_styles/button_file-5.png")
    file_loadFile6_btn = PhotoImage(file="button_styles/button_file-6.png")


    loadFile.title('VM - Load Saved File')
    loadFile.geometry("1100x500")
    loadFile.resizable(False, False)
    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    loadFile.iconphoto(False, varmakerIcon)

    title = Label(loadFile, text="Select a file to load", font=("Calibri", 30, 'bold'))
    warning = Label(loadFile, text="!!! If you don't see any pop-up windows saying the operation was success, it's not an error. Just click the button once, and the file will just load perfectly. !!!", font=("Calibri", 12))

    title.pack()
    warning.pack()

    file_loadFile1 = Button(loadFile, image=file_loadFile1_btn, border=0, command=loadFile1)
    file_loadFile1.pack()

    file_loadFile2 = Button(loadFile, image=file_loadFile2_btn, border=0, command=loadFile2)
    file_loadFile2.pack()

    file_loadFile3 = Button(loadFile, image=file_loadFile3_btn, border=0, command=loadFile3)
    file_loadFile3.pack()

    file_loadFile4 = Button(loadFile, image=file_loadFile4_btn, border=0, command=loadFile4)
    file_loadFile4.pack()

    file_loadFile5 = Button(loadFile, image=file_loadFile5_btn, border=0, command=loadFile5)
    file_loadFile5.pack()

    file_loadFile6 = Button(loadFile, image=file_loadFile6_btn, border=0, command=loadFile6)
    file_loadFile6.pack()

    loadFile.mainloop()

if __name__ == "__main__":
    loadFile()