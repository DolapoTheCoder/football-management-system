from tkinter import *

def PlayerScreen():
    #allow the entries and screen to be accessed by other functions
    global screen
    screen = Tk()

    global PnameEntry
    Pname = StringVar()

    global GoalsEntry
    Goals = IntVar()

    global InjuryEntry
    Injury = StringVar()

##    global CardsEntry
##    Cards = IntVar()
##    global RecordEntry
##    Record = StringVar()

    
    screen.geometry("500x650")
    screen.title("Football Management System")
    Label(text = "Player Page", bg = "grey", height = "2", width = "30").pack()
    
##    Label(text = "").pack()

    #Creating entries and displaying the entry boxes and data we want
    Label(text = "Player Name:", font = ("Time", 11)).pack()
    PnameEntry = Entry(textvariable = Pname)
    PnameEntry.pack()
    
##    Label(text = "").pack()
    Label(text = "Data from the last 10 matches", font = ("Time", 12))
    Label(text = "Goals:", font = ("Time", 11)).pack()
    GoalsEntry = Entry(textvariable = Goals)
    GoalsEntry.pack()

    Label(text = "").pack()
    
    Label(text = "Injury (N/A if no injuries):", font = ("Time", 11)).pack()
    InjuryEntry = Entry(textvariable = Injury)
    InjuryEntry.pack()

##    Label(text = "").pack()
    
##    Label(text = "Cards (sum of amount of cards Red = 2, Yellow = 1):", font = ("Time", 11)).pack()
##    CardsEntry = Entry(textvariable = Cards)
##    CardsEntry.pack()
    #allowing accesss from other functions
    global RedEntry
    Reds = IntVar()
    
    global YellowEntry
    Yellows = IntVar()
    
    
    Label(text = "").pack()
    
    #collecting data from user
    Label( text = "Reds:", font = ("Time", 11)).pack()
    RedEntry = Entry( textvariable = Reds)
    RedEntry.pack()

    Label( text = "").pack()
    
    Label( text = "Yellow:", font = ("Time", 11)).pack()
    YellowEntry = Entry(textvariable = Yellows)
    YellowEntry.pack()
    
    Label(text = "").pack()
##    
##    Label(text = "Record:", font = ("Time", 11)).pack()
##    RecordEntry = Entry(textvariable = Record)
##    RecordEntry.pack()
    global WinEntry
    global DrawEntry
    global LoseEntry
   
 
    Win = IntVar()
    Lose = IntVar()
    Draw = IntVar()
    
    Label(text = "Wins:", font= ("Time", 11)).pack()
    WinEntry = Entry(textvariable = Win)
    WinEntry.pack()
    Label(text="").pack()
    
    Label(text = "Loses:", font= ("Time", 11)).pack()
    LoseEntry = Entry(textvariable = Lose)
    LoseEntry.pack()
    Label(text="").pack()
    
    Label(text = "Draws:", font= ("Time", 11)).pack()
    DrawEntry = Entry(textvariable = Draw)
    DrawEntry.pack()


##    #Buttons linking to new pages to allows for more indepth data retreivial
##    Button(text = "Card Input (This screen must be filled in)", command = CardInput).pack()
##    Label(text = "").pack()
##
###extra text was added here to guarntee input as the code only works if everything is inputted that is required
##    Button(text = "Record Input (This screen must be filled in)", command = RecordInput).pack()
##    Label(text = "").pack()
##
####    while PnameEntry != "" and GoalsEntry != 0 and InjuryEntry != "" and RedEntry != 0 and YellowEntry != 0 and WinEntry != 0 and DrawEntry != 0 and LoseEntry != 0:
    Button(text = "Player's Screen", command = PlyScreen).pack()    


    #allowing the user to leave the screen
    Label(text = "").pack()
    Button(text = "Cancel", command = screen.destroy).pack()

    screen.mainloop()
    
##def delete():
##    screen.destroy()


##def CardInput():
##    global CardInp
##    
##    CardInp = Toplevel(screen)
##    CardInp.geometry("300x300")
##    CardInp.title("Football Management System")
##    Label(CardInp, text = "Card Input", bg = "grey", height = "2", width = "30", font = ("Time", 13)).pack()
##
##    #allowing accesss from other functions
##    global RedEntry
##    Reds = IntVar()
##    
##    global YellowEntry
##    Yellows = IntVar()
##    
##    
##    Label(CardInp, text = "").pack()
##    
##    #collecting data from user
##    Label(CardInp, text = "Reds:", font = ("Time", 11)).pack()
##    RedEntry = Entry(CardInp, textvariable = Reds)
##    RedEntry.pack()
##
##    Label(CardInp, text = "").pack()
##    
##    Label(CardInp, text = "Yellow:", font = ("Time", 11)).pack()
##    YellowEntry = Entry(CardInp, textvariable = Yellows)
##    YellowEntry.pack()
##
##    #allowing the user to leave the screen
##    Label(CardInp, text = "").pack()
##    Button(CardInp, text = "Cancel", command = CardInp.destroy).pack()

    
##def RecordInput():
##    
##    global RecordInp
##    RecordInp = Toplevel(screen)
##    RecordInp.geometry("400x400")
##    RecordInp.title("Football Management System")
##    Label(RecordInp, text = "Record Input", bg = "grey", height = "2", width = "30", font = ("Time", 13)).pack()
##
##    global WinEntry
##    global DrawEntry
##    global LoseEntry
##   
## 
##    Win = IntVar()
##    Lose = IntVar()
##    Draw = IntVar()
##    
##    Label(RecordInp, text = "Wins:", font= ("Time", 11)).pack()
##    WinEntry = Entry(RecordInp, textvariable = Win)
##    WinEntry.pack()
##    Label(RecordInp, text="").pack()
##    
##    Label(RecordInp, text = "Loses:", font= ("Time", 11)).pack()
##    LoseEntry = Entry(RecordInp, textvariable = Lose)
##    LoseEntry.pack()
##    Label(RecordInp, text="").pack()
##    
##    Label(RecordInp, text = "Draws:", font= ("Time", 11)).pack()
##    DrawEntry = Entry(RecordInp, textvariable = Draw)
##    DrawEntry.pack()
##
##
##    Label(RecordInp, text="").pack()
##    Button(RecordInp, text = "Cancel", command = RecordInp.destroy).pack()


#players screen using the input we have recieved
def PlyScreen():
##        global name
##        global goal
##        global injury
##        global red
##        global yellow
##        global win
##        global draw
##        global lose
    
    #getting all the inputs from the previous screens
        name = PnameEntry.get()
        goal = GoalsEntry.get()
        injury = InjuryEntry.get()
##problem with the entries from other screens that weren't opened PROBLEM (Testing)        
        red = RedEntry.get()
        yellow = YellowEntry.get()
        win = WinEntry.get()
        draw = DrawEntry.get()
        lose = LoseEntry.get()

##        if name != "" and goal != 0 and injury != "" and red != 0 and yellow != 0 and win != 0 and draw != 0 and lose != 0:
##            PlayerScreen()
##        else:
##            print("Working...")
        
        screen2 = Toplevel(screen)
        screen2.geometry("400x600")
        screen2.title("Football Management Sytsem")
        
        #name Display
        Label(screen2, text = name, bg = "grey", height = "2", width = "30", font = ("Time", 13)).pack()
        Label(screen2, text = "").pack()
        Label(screen2, text = "").pack()
        
        #Goal Display
        Label(screen2, text = "Goals:", font = ("Time", 13)).pack()
        Label(screen2, text = goal, font = ("Time", 11)).pack()
        Label(screen2, text = "").pack()
        
        #Injury Display
        Label(screen2, text = "Injury:", font = ("Time", 13)).pack()
        Label(screen2, text = injury, font = ("Time", 11)).pack()
        Label(screen2, text = "").pack()
        
        #Cards Display multiple variables cant be stored on one line
        Label(screen2, text = "Cards:", font = ("Time", 13)).pack()
        Label(screen2, text = "Red:", font = ("Time", 12)).pack()
        Label(screen2, text = red, font = ("Time", 11)).pack()
        Label(screen2, text = "Yellows:", font = ("Time", 12)).pack()
        Label(screen2, text = yellow, font = ("Time", 11)).pack()
        Label(screen2, text = "").pack()

        #Record Display
        Label(screen2, text = "Record:", font = ("Time", 13)).pack()
        Label(screen2, text = "Wins:", font = ("Time", 12)).pack()
        Label(screen2, text = win, font = ("Time", 11)).pack()
        Label(screen2, text = "Draw:", font = ("Time", 12)).pack()
        Label(screen2, text = draw, font = ("Time", 11)).pack()
        Label(screen2, text = "Lose:", font = ("Time", 12)).pack()
        Label(screen2, text = lose , font = ("Time", 11)).pack()
        
        Label(screen2, text = "").pack()
        
#Button's on screen 
        Button(screen2, text = "Advised Training", command = AdvTraining).pack()
        Label(screen2, text = "").pack()
        Button(screen2, text = "Cancel", command = screen2.destroy).pack()

        


#ADVISED TRAINING
def AdvTraining():
    Train = Toplevel(screen)
    Train.geometry("300x300")
    Train.title("Football Management System")
    Label(Train, text = "Advised Training", bg = "grey", height = "2", width = "30", font=("Time", 13)).pack()

    #getting all the inputs from the previous screens
    name = PnameEntry.get()
    goal = GoalsEntry.get()
    injury = InjuryEntry.get()
##problem with the entries from other screens that weren't opened PROBLEM (Testing)        
    red = RedEntry.get()
    yellow = YellowEntry.get()
    win = WinEntry.get()
    draw = DrawEntry.get()
    lose = LoseEntry.get()

    #Requirements for advised training DOESN'T WORK
##    if red or yellow != 0:
##        Label(Train, text = "Anger Management", font = ("Time", 12)).pack()
        
    if injury != "N/A" or "n/a" or "na":
        Label(Train, text = "Rest, Stretch and Recovery Exercises suited to the injury that you have.", font = ("Time", 12)).pack()
        
    elif goal < 5:
        Label(Train, text = "Shooting, Volley and Headering Drills", font = ("Time", 12)).pack()
        
    elif lose > 5 or draw > 5:
        Label(Train, text = "Practice Corners and other set-pieces as a team, Piggy In The Middle and other chemistry building excrecises", font = ("Time", 12)).pack()

    elif win < 4:
        Label(Train, text = "Practice Corners and other set-pieces as a team, Piggy In The Middle and other chemistry building excrecises", font = ("Time", 12)).pack()

    #should be a rare case
    else:
        Label(Train, text = "Your data from the last 10 matches didn't alert any of our advised training requirements", font = ("Time", 12))


    
    Label(Train, text = "").pack()
    Button(Train, text = "Cancel", command = Train.destroy).pack()
    

    
        


PlayerScreen()
