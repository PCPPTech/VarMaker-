from tkinter import *

def newsFunc():
    news = Toplevel()
    varmakerIcon = PhotoImage(file="Varmaker ICON/varmaker-logo.png")
    news.iconphoto(False, varmakerIcon)
    news.geometry("900x600")
    news.title("VM - News")

    def insertNews(text):
        text_area.insert(END, f"{text}\n")

    

    # Actual News
    
    # Step 1 - Scroll Bar
    scroll_bar = Scrollbar(news)
    scroll_bar.pack(side=RIGHT, fill=Y)

    # Step 2 - Text Area

    text_area = Text(news, font=("Calibri", 15))
    text_area.pack()

    # News
    insertNews("2023.12.25")
    insertNews("• Revamped the menu for a more elegant look.")
    insertNews("• Integraded paddings between buttons to make them more readable.\n")
    
    insertNews("2024.01.04")
    insertNews("• Fixed bugs occuring with icon images and buttons.")
    insertNews("• Integraded more button functionalities.\n")

    insertNews("2024.01.14")
    insertNews("• Integraded more button functionalities.")
    insertNews("• Integraded saving system.\n")
    
    insertNews("2024.01.18")
    insertNews("• Fixed errors occuring with the saving system.")
    insertNews("• Integraded 'load a saved file' system.")
    insertNews("• Integraded a 'remove a saved file' system.\n")

    insertNews("2024.01.23")
    insertNews("• Fixed errors occuring with the 'Remove a saved file' system.")
    insertNews("• Fixed errors occuring with the 'Load a Saved File' system.")
    insertNews("• Integraded a website via wordpress.com for the application.")
    insertNews("• Integraded ToS for the application.")
    insertNews("• Changed 'News' button's name to 'App Progress'.")
    insertNews("• Fixed the 'Different Colored Buttons' error.")
    insertNews("• Released VarMaker™.")

    # Step 3 - Configure Text Area

    text_area.configure(yscrollcommand=scroll_bar.set)
    scroll_bar.configure(text_area.yview)


    news.mainloop()

if __name__ == "__main__":
    newsFunc()