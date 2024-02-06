from tkinter import *

def main():
    import time
    
    class Country:
        def __init__(self, hp, bomb_dmg, bomb_quantity, airstrike_dmg, airstrike_quantity, nuke_dmg, nuke_quantity):
            self.hp = hp
            self.bomb_dmg = bomb_dmg
            self.bomb_quantity = bomb_quantity
            self.airstrike_dmg = airstrike_dmg
            self.airstrike_quantity = airstrike_quantity
            self.nuke_dmg = nuke_dmg
            self.nuke_quantity = nuke_quantity
        
        def attack(enemyHP, attackingWith):
            if attackingWith == "bomb":
                enemyHP -= self.bomb_dmg
                self.bomb_quantity -= 1
                operationDone = Tk()
                #Resolution
                operationDone.title("Badass😎")
                operationDone.geometry("100x100")
                #Labels
                label = Label(operationDone, text="Operation Successful. You're badass😎", font=("Calibri", 15, "italic"))
                label.pack()
                #Mainloop
                operationDone.mainloop()
            elif attackingWith == "airstrike":
                enemyHP -= self.airstrike_dmg
                self.airstrike_quantity -= 1
                operationDone1 = Tk()
                #Resolution
                operationDone1.title("Badass😎")
                operationDone1.geometry("100x100")
                #Labels
                label = Label(operationDone1, text="Operation Successful. You're badass😎", font=("Calibri", 15, "italic"))
                label.pack()
                #Mainloop
                operationDone1.mainloop()
            elif attackingWith == "nuke":
                enemyHP -= self.nuke_dmg
                self.nuke_quantity -= 1
                operationDone2 = Tk()
                #Resolution
                operationDone2.title("Badass😎")
                operationDone2.geometry("100x100")
                #Labels
                label = Label(operationDone2, text="Operation Successful. You're badass😎", font=("Calibri", 15, "italic"))
                label.pack()
                #Mainloop
                operationDone2.mainloop()
            else:
                print("There is something wrong. The developer has made a mistake. Please report the issue at eidnoxon213@gmail.com, or at (discord server)")
                
    p1_country = 0
    p2_country = 0
    
    p1_SelectedCountry = ""
    p2_SelectedCountry = ""
    
    #Functions (menuwar = Tk())
    def play():
    
        def selectedRussiap1():
            p1_country = Country(1000, 200, 2, 50, 4, 600, 1)
            p1_SelectedCountry = "russia"

            p1_CountrySelection.destroy()
        
        def selectedUSAp1():
            p1_country = Country(1000, 200, 2, 50, 4, 600, 1)
            p1_SelectedCountry = "usa"
                        
            p1_CountrySelection.destroy()
        def selectedMexicop1():
            p1_country = Country(800, 100, 4, 25, 8, 300, 2)
            p1_SelectedCountry = "mexico"
            
            p1_CountrySelection.destroy()
        def selectedCanadap1():
            p1_country = Country(1000, 100, 4, 25, 8, 300, 2)
            p1_SelectedCountry = "canada"
            
            p1_CountrySelection.destroy()
        #Country Selection Mechanics for P2   
        
        def selectedRussiap2():
            p2_country = Country(1000, 200, 2, 50, 4, 600, 1)
            p2_SelectedCountry = "russia"
            
            CountrySelectionMenu.destroy()
        def selectedUSAp2():
            p2_country = Country(1000, 200, 2, 50, 4, 600, 1)
            p2_SelectedCountry = "usa"
            
            CountrySelectionMenu.destroy()
        def selectedMexicop2():
            p2_country = Country(800, 100, 4, 25, 8, 300, 2)
            p2_SelectedCountry = "mexico"
            
            CountrySelectionMenu.destroy()
        def selectedCanadap2():
            p2_country = Country(1000, 100, 4, 25, 8, 300, 2)
            p2_SelectedCountry = "canada"
    
            CountrySelectionMenu.destroy()

        menuwar.destroy()

        CountrySelectionMenu = Tk()
        CountrySelectionMenu.title("Country Selection")
        CountrySelectionMenu.geometry("800x500")


        title = Label(CountrySelectionMenu, text="P1. SELECT YOUR COUNTRY", font=("Calibri", 20, "bold"))
        title.grid(row=0, column=0, columnspan=5)
        #Countries:
        Russia = Button(CountrySelectionMenu, text="Russia", font=("Calibri", 15), command=selectedRussiap1)
        Russia.grid(row=1, column=1)
        
        usa = Button(CountrySelectionMenu, text="United States of America", font=("Calibri", 15), command=selectedUSAp1)
        usa.grid(row=2, column=1)
        
        mexico = Button(CountrySelectionMenu, text="Mexico", font=("Calibri", 15), command=selectedMexicop1)
        mexico.grid(row=3, column=1)
        
        canada = Button(CountrySelectionMenu, text="Canada", font=("Calibri", 15), command=selectedCanadap1)
        canada.grid(row=4, column=1)

        CountrySelectionMenu.mainloop()
        


        title1 = Label(CountrySelectionMenu, text="P2. SELECT YOUR COUNTRY", font=("Calibri", 20, "bold"))
        title1.grid(row=0, column=2, columnspan=10)
        #Countries:
        Russia1 = Button(CountrySelectionMenu, text="Russia", font=("Calibri", 15), command=selectedRussiap2)
        Russia1.grid(row=1, column=3)
        
        usa1 = Button(CountrySelectionMenu, text="United States of America", font=("Calibri", 15), command=selectedUSAp2)
        usa1.grid(row=2, column=3)
        
        mexico1 = Button(CountrySelectionMenu, text="Mexico", font=("Calibri", 15), command=selectedMexicop2)
        mexico1.grid(row=3, column=3)
        
        canada1 = Button(CountrySelectionMenu, text="Canada", font=("Calibri", 15), command=selectedCanadap2)
        canada1.grid(row=4, column=3)
        
        CountrySelectionMenu.mainloop()

        #Actual gameplay
        war = Tk()
        label = Label(war, text="Your Code works YIPPIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE", font=("Calibri", 50, 'italic'))
        label.pack()
        war.mainloop()


    
    menuwar = Tk()
    menuwar.title("VM - Games - Country War")
    menuwar.geometry("800x500")
    mainTitle = Label(menuwar, text="Country War", font=("Calibri", 20, "bold"))
    mainTitle.pack()
    playButton = Button(menuwar, text="Play", font=("Calibri", 15), command=play)
    playButton.pack()
    menuwar.mainloop()