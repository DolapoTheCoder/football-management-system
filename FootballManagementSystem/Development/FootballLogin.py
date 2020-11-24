from tkinter import *
#allows me to access the operating system etc
import os 

def deleten():
    screen3.destroy()
    
def loginSuccess():
    global screen3 
    screen3 = Toplevel(screen)
    screen3.title("Succes")
    screen3.geometry("300x300")
    Label(screen3, text = "Login Success").pack()
    Button(screen3, text = "OK", command = deleten).pack()
    

def PwordNotRecognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password Not Recognised")
    screen4.geometry("300x300")
    Label(screen4, text = "Password Not Recognised").pack()

def UserNorFound():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User Not Found")
    screen5.geometry("300x300")
    Label(screen5, text = "User Not Found").pack()

def register_user():
    Uname_info = Uname.get()
    Pword_info = Pword.get()

    #FILE WORK
    file = open(Uname_info, "w") #creating a new file to open and store the username and password
    file.write(Uname_info+"\n")
    file.write(Pword_info)
    file.close()

    #deleting the current aspects in the entry box to allow for someone to register again
    Uname_entry.delete(0, END)
    Pword_entry.delete(0, END)

    Label(screen1, text= "Registration Success", fg = "green", font = ("Time", 11)).pack()

def login_verify():
    Uname1 = Uname_verify.get()
    Pword1 = Pword_verify.get()

    #deleting the current aspects in the entry box to allow for someone to register again
    Uname_entry1.delete(0, END)
    Pword_entry1.delete(0, END)

    #creating a list of the text files
    listOfFiles = os.listdir()
    if Uname1 in listOfFiles:
        file1 = open(Uname1, "r")
        verify = file1.read().splitlines()
        if Pword1 in verify:
            loginSuccess()
        else:
            PwordNotRecognised()
    else:
        UserNorFound()
        
        
        
def register(): 
    global screen1
    screen1 = Toplevel(screen) #creating a new screen to allow for registering
    screen1.title("Register")
    screen1.geometry("300x300")
    
    global Uname
    global Pword
    global Pword_entry
    global Uname_entry
    Uname = StringVar()
    Pword = StringVar()

    #creating the aspects of the screen
    Label(screen1, text = "Please Enter Details Below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username").pack()
    Uname_entry = Entry(screen1, textvariable= Uname)
    Uname_entry.pack()
    Label(screen1, text = "Password").pack()
    Pword_entry = Entry(screen1, textvariable= Pword)
    Pword_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = "10", height = "1", command = register_user).pack()
    Button(screen1, text = "Cancel", width = "10", height = "1", command = delete1).pack()
    
def login():
    global screen2
    screen2 = Toplevel(screen) #creating a new screen to allow for registering
    screen2.title("Login")
    screen2.geometry("300x300")
    Label(screen2, text = "Please Enter Details Below To Login").pack()
    Label(screen2, text = "").pack()
    
    global Pword_verify
    global Uname_verify
    Uname_verify = StringVar()
    Pword_verify = StringVar()

    global Pword_entry1
    global Uname_entry1
    #creating the aspects of the screen
    Label(screen2, text = "Username").pack()
    Uname_entry1 = Entry(screen2, textvariable = Uname_verify)
    Uname_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password").pack()
    Pword_entry1 = Entry(screen2, textvariable = Pword_verify)
    Pword_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = "10", height = "1", command = login_verify).pack()
    Button(screen2, text = "Cancel", width = "10", height = "1", command = delete2).pack()



def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x300")
    #creating the aspects of the screen
    screen.title("Football Management System")
    Label(text = "Football Management Login", bg = "grey", width = "300", height = "2",font = ("Time", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    Button(text = "Cancel", height = "2", width = "30", command = delete).pack()

    screen.mainloop()

def delete():
    screen.destroy()
def delete1():
    screen1.destroy()
def delete2():
    screen2.destroy()
main_screen()
