from tkinter import *

def managerPage():
    global screen
    screen = Tk()
    screen.geometry("300x300")
    screen.title("Football Management System")
    Label(text = "Manager", bg = "grey",height = "2", width = "30").pack()
    Label(text = "").pack()
    Button(text = "Last Match Roster", height = "2", width = "30", command = LastMatch).pack()
    Button(text = "Game Simulator", height = "2", width = "30", command = GameSim).pack()
    Button(text = "Cancel", height = "2", width = "30", command = delete).pack()

    screen.mainloop()
def delete():
    screen.destroy()
#Last Match Rooster 
def LastMatch():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("400x600")
    screen1.title("Football Management System")
    Label(screen1, text = "Last Match Roster", bg = "grey", height = "2", width = "30").pack()
    #Once a players button is pressed it goes to that players page
    Button(screen1, text = "Player1", height = "2", width = "30", command=Player1).pack()
    Button(screen1, text = "Player2", height = "2", width = "30", command=Player2).pack()
    Button(screen1, text = "Player3", height = "2", width = "30", command=Player3).pack()
    Button(screen1, text = "Player4", height = "2", width = "30", command=Player4).pack()
    Button(screen1, text = "Player5", height = "2", width = "30", command=Player5).pack()
    Button(screen1, text = "Player6", height = "2", width = "30", command=Player6).pack()
    Button(screen1, text = "Player7", height = "2", width = "30", command=Player7).pack()
    Button(screen1, text = "Player8", height = "2", width = "30", command=Player8).pack()
    Button(screen1, text = "Player9", height = "2", width = "30", command=Player9).pack()
    Button(screen1, text = "Player10", height = "2", width = "30", command=Player10).pack()
    Button(screen1, text = "Player11", height = "2", width = "30", command=Player11).pack()
    Button(screen1, text = "Cancel", height = "2", width = "30", command = delete1).pack()

def delete1():
    screen1.destroy()

def Player1():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("300x300")
    screen2.title("Football Management System")
    Label(screen2, text = "Player 1 ", bg = "grey", height = "2", width = "30").pack()

def Player2():
    global screen3
    screen3 = Toplevel(screen)
    screen3.geometry("300x300")
    screen3.title("Football Management System")
    Label(screen3, text = "Player 2 ", bg = "grey", height = "2", width = "30").pack()
    
def Player3():
    global screen4
    screen4 = Toplevel(screen)
    screen4.geometry("300x300")
    screen4.title("Football Management System")
    Label(screen4, text = "Player 3 ", bg = "grey", height = "2", width = "30").pack()
    
def Player4():
    global screen5
    screen5 = Toplevel(screen)
    screen5.geometry("300x300")
    screen5.title("Football Management System")
    Label(screen5, text = "Player 4 ", bg = "grey", height = "2", width = "30").pack()
    
def Player5():
    global screen6
    screen6 = Toplevel(screen)
    screen6.geometry("300x300")
    screen6.title("Football Management System")
    Label(screen6, text = "Player 5 ", bg = "grey", height = "2", width = "30").pack()
    
def Player6():
    global screen7
    screen7 = Toplevel(screen)
    screen7.geometry("300x300")
    screen7.title("Football Management System")
    Label(screen7, text = "Player 6 ", bg = "grey", height = "2", width = "30").pack()
    
def Player7():
    global screen8
    screen8 = Toplevel(screen)
    screen8.geometry("300x300")
    screen8.title("Football Management System")
    Label(screen8, text = "Player 7 ", bg = "grey", height = "2", width = "30").pack()
    
def Player8():
    global screen9
    screen9 = Toplevel(screen)
    screen9.geometry("300x300")
    screen9.title("Football Management System")
    Label(screen9, text = "Player 8 ", bg = "grey", height = "2", width = "30").pack()
    
def Player9():
    global screen10
    screen10 = Toplevel(screen)
    screen10.geometry("300x300")
    screen10.title("Football Management System")
    Label(screen10, text = "Player 9 ", bg = "grey", height = "2", width = "30").pack()
    
def Player10():
    global screen11
    screen11 = Toplevel(screen)
    screen11.geometry("300x300")
    screen11.title("Football Management System")
    Label(screen11, text = "Player 10 ", bg = "grey", height = "2", width = "30").pack()
    
def Player11():
    global screen12
    screen12 = Toplevel(screen)
    screen12.geometry("300x300")
    screen12.title("Football Management System")
    Label(screen12, text = "Player 11 ", bg = "grey", height = "2", width = "30").pack()

#GAME SIMULATOR PAGE
def GameSim():
    global screen13
    screen13 = Toplevel(screen)
    screen13.geometry("400x500")
    screen13.title("Football Management System")
    Label(screen13, text = "GAME SIMULATOR (EXTENSTION)", bg = "grey", height = "2", width = "30", font = ("Time",13)).pack()
    
    Label(screen13, text = "To simulate a game you need to input your current record:", height = "1", width = "50", font = ("Time",11)). pack()
    Label(screen13, text="").pack()

##    global Win
##    global Lose
##    global Draw
    global WinEntry
    global DrawEntry
    global LoseEntry
   

    #PROBLEM HERE 
    Win = IntVar()
    Lose = IntVar()
    Draw = IntVar()
    
    Label(screen13, text = "Wins:", font= ("Time", 11)).pack()
    WinEntry = Entry(screen13, textvariable = Win)
    WinEntry.pack()
    Label(screen13, text="").pack()
    
    Label(screen13, text = "Loses:", font= ("Time", 11)).pack()
    LoseEntry = Entry(screen13, textvariable = Lose)
    LoseEntry.pack()
    Label(screen13, text="").pack()
    
    Label(screen13, text = "Draws:", font= ("Time", 11)).pack()
    DrawEntry = Entry(screen13, textvariable = Draw)
    DrawEntry.pack()
    Button(screen13, text = "Simulate", height = "2", width = "30", command = Simulation).pack()
    
    Label(screen13, text="").pack()
    Button(screen13, text = "Cancel", height = "2", width = "30", command = delete2).pack()
    

def delete2():
    screen13.destroy()

def Simulation():
    global screen14
    screen14 = Toplevel(screen)
    screen14.title("Football Management System")
    screen14.geometry("300x300")
    Label(screen14, text = "SIMULATION", bg = "grey", height = "2", width = "30").pack()
    Label(screen14, text = "").pack()
    Label(screen14, text = "").pack()
    Label(screen14, text = "").pack()
    Label(screen14, text = "").pack()
    win = int(WinEntry.get())
    draw = int(DrawEntry.get())
    lose = int(LoseEntry.get())

    #PROBLEM HERE
    
    sumOfRecord = win + draw + lose
    averageRecord = sumOfRecord // 3
    if averageRecord > draw:
        WIN()
        
    elif averageRecord == draw:
        DRAW()
        
    else:
        LOSE()

    Button(screen14, text = "Cancel", command = leave).pack()

def WIN():
    Label(screen14, text = "You Won!", bg = "green", width = "30", height= "2", font = ("Time", 15)).pack()

def DRAW():
    Label(screen14, text = "You Drew!", bg = "grey", width = "30", height= "2", font = ("Time", 15)).pack()

def LOSE():
    Label(screen14, text = "You Lose!", bg = "red", width = "30", height= "2", font = ("Time", 15)).pack()

def leave():
    screen14.destroy()



managerPage()
