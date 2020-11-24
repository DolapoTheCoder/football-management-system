from tkinter import *

def optionpage():
    global screen
    screen = Tk()
    screen.geometry("300x300")
    screen.title("Football Management System")
    #creating the varous options within the option page consisting of buttons
    Label(text = """    Option Page
        Pick Manager or Player""", bg = "grey", width = "300", height = "2", font = ("Time", 13)).pack()
    Button(text = "Manager", height = "2", width = "30", command=manager).pack()
    Label(text = "").pack()
    Button(text = "Player", height = "2", width = "30", command=player).pack()
    Label(text = "").pack()
    Button(text = "Cancel", height = "2", width = "30", command=delete).pack()

    screen.mainloop()

def manager():
    #creating the manager page
    screen1 = Toplevel(screen)
    screen1.geometry("500x300")
    screen1.title("Football Management System Manager Page")
    
def player():
    #creating the player page
    screen2 = Toplevel(screen)
    screen2.geometry("500x300")
    screen2.title("Football Management System Player Page")
    
def delete():
    screen.destroy()


optionpage()
