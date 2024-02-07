"""
Make UI's Blue & Black themed
"""

everything = []

from tkinter import *

def CALAYmain():

    def gamePlay():
        menu.destroy()

        #Functions to 'window'
        def submitAnswer():
            formerAnswer = answerForm.get()
            everything.append("Name: " + formerAnswer)


            window.destroy()
            # Functions of 'q2'
            def if_hovered(event):
                submitButton1.config(font=("Calibri", 18, 'bold'), bg='black', fg='blue', width=17)
                submitButton1.pack()
            
            def if_not_hovered(event):
                submitButton1.config(font=("Calibri", 15), bg='black', fg='blue', width=15)
                submitButton1.pack()

            
            def submitAnswer2():
                formerAnswer1 = answerForm1.get()
                everything.append("Age: " + str(formerAnswer1))


                q2.destroy()
                
                


            q2 = Tk()
            #Basic Stuff
            q2.resizable(False, False)
            q2.title("CALAY - Question 2")
            q2.config(bg='black')
            q2.geometry('800x500')


            # Labels, Buttons, Entries, etc.
            questionLabel = Label(q2, text="How old are you?", font=("Calibri", 20), fg='blue', bg='black')
            questionLabel.pack()

            warning1 = Label(q2, text="Don't worry, the information you put here won't be saved. It's just for fun.", font=("Calibri", 14), fg='blue', bg='black')
            warning1.pack()

            answerForm1 = Entry(q2, font=("Times New Roman", 20), bg='gray', fg='blue')
            answerForm1.pack()

            submitButton1 = Button(q2, text="Submit", font=("Calibri", 15), bg='black', fg='blue', highlightthickness=1, highlightbackground='blue', command=submitAnswer2)
            submitButton1.pack()

            submitButton1.bind("<Enter>", if_hovered)
            submitButton1.bind("<Leave>", if_not_hovered)

            q2.mainloop()

        def on_enter(event):
            submitButton.config(font=("Calibri", 18, 'bold'), bg='black', fg='blue', width=17)
            submitButton.pack()
        def on_leave(event):
            submitButton.config(font=("Calibri", 15), bg='black', fg='blue', width=15)
            submitButton.pack()


        window = Toplevel()
        window.resizable(False, False)
        #Basic stuff
        window.geometry("800x500")
        window.title("CALAY - Question 1")
        window.config(bg='black')


        #Labels & Buttons & Entries and etc.
        label = Label(window, text="What's your name?", font=("Calibri", 20), fg='blue', bg='black')
        label.pack()
        
        warning = Label(window, text="Don't worry, the information you put here won't be saved. It's just for fun.", font=("Calibri", 14), fg='blue', bg='black')
        warning.pack()

        answerForm = Entry(window, font=("Times New Roman", 20), fg='blue', bg='gray')
        answerForm.pack()

        submitButton = Button(window, text="Submit Answer", font=("Calibri", 15), fg='blue', bg='black', highlightthickness=1, highlightbackground='blue', command=submitAnswer)
        submitButton.pack()
        
        window.mainloop()

    menu = Toplevel()
    varmaker_logo = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    menu.iconphoto(False, varmaker_logo)
    menu.resizable(False, False)
    # Resolution and stuff
    menu.title("VM - Games - CALAY")
    menu.geometry("800x500")
    menu.configure(bg='black')

    button_startGame = PhotoImage(file="button_styles/CALAYgui-button-styles/button_start-the-game.png")

    mainTitle = Label(menu, text="CALAY", font=("Calibri", 20, 'bold'), fg='blue', bg='black')
    mainTitle.pack(pady=(20, 0))

    littleTitle = Label(menu, text="0.0.1 BETA GUI version", font=("Calibri"), fg='blue', bg='black')
    littleTitle.pack()

    # Options
    play = Button(menu, image=button_startGame, border=0, bg='black')
    play.pack()

    menu.mainloop()
