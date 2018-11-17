from tkinter import *
from PasswordHashing import *

# This is the class for the login window, I don't know how we should divide up the classes for each GUI element right now,
# maybe we will have them in seperate files or maybe just keep them in one file.
class Login:
    # This is the initilization function that first runs in the class.
    def __init__(self, master):
        # Master refers to the window itself and self is the class
        self.master = master
        # We set the title for our window here
        master.title("Hoot - A Library Manager'paEKnbzpodihtdzougteuihx")
        # Creating labels is pretty easy, right now almost all of the GUI elements are at default width and height
        self.label = Label(master, text="Login to Hoot!")
        # Packing elements actually publishes them to the GUI window
        self.label.pack()

        # This creates a text entry element with a width of 15
        self.username = Entry(master, width=15)
        self.username.pack()
        # This creates a password text entry element also with a width of 15, the "show="*"" makes the text appear like a
        # password
        self.password = Entry(master, show="*", width=15)
        self.password.pack()

        # Creates the login button which calls the verifyLogin function
        self.login = Button(master, text="Sign In", command=self.verifyLogin)
        self.login.pack()

        # Creates the register button which calls the registerUser function
        self.register = Button(master, text="Register", command=self.registerUser)
        self.register.pack()

    # This function is used to pass the username and password that the user entered to our verifyUser function
    def verifyLogin(self):
        # Passes the username and the password to the verifyUser function for verification
        if verifyUser(self.password.get(), self.username.get()).replace('"', ''):
            # Closes the login window
            self.master.destroy()
            # Starts up the main window for Hoot
            mainWindowLaunch()
        else:
            # This is for errors
            self.label.config(text="Either user doesn't exist or password is wrong!")

    # This function is for registering users to our database
    def registerUser(self):
        # Sends the username and password for registration
        print(createHash(self.password.get(), self.username.get()))
        self.label.config(text='You are registered!')  

# Here we create the first window which is our login window which will be seperate from the main program window
root = Tk()
my_gui = Login(root)
root.mainloop()

# This is the class for the main window of our application
class Hoot_Main:
    # The initilization function for the main window
    def __init__(self, master):
        self.master = master
        master.title("Hoot - A Library Manager")

# Function for launching the main window
def mainWindowLaunch():
    root = Tk()
    my_gui = Main(root)
    root.mainloop()
