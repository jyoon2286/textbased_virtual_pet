import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk


class Pet:
    """
    The Pet class has 7 attributes which are name, hungriness, boredom,
    tiredness, sickness, age, and waste
    One of methods get the mood states of the per based on thresholds level
    """
    max_age = random.randint(10000, 100000)
    boredom_threshold = 15
    max_boredom = 55
    hungriness_threshold = 20
    max_hungriness = 55
    tiredness_threshold = 15
    max_tiredness = 55
    max_waste = 55

    def __init__(self, name, hungriness=0, boredom=0, tiredness=0,
                 sickness=False, age=0, waste=0):
        self.__name = name
        self.hungriness = hungriness
        self.boredom = boredom
        self.tiredness = tiredness
        self.sickness = sickness
        self.age = age
        self.waste = waste

    def mood(self):
        """
        This function will print out the mood of the pet and return it

        The mood will be printed out the order of the priority levels.
        For example, the hungriness is more important than boredom and tiredness
        so it shows the "I'm hungry" even though the boredom or tiredness
        is higher.

        The mood states will be printed in red color for noticeable to users.

        :return: the mood of the pet based on the logic, the return value is for
        the future test script
        """
        if self.sickness is True:
            print('\033[91m'+"I'm sick" + '\033[0m')
            return "sick"
        # The pet can't die just because the pet is old unless user play for
        # couple hours and it will print out "..." and exit the game or
        # users do nothing with their pet.
        # We intend to do that because the pet is not real one.
        if self.age == self.max_age:
            print('\033[91m'+"...."+'\033[0m')
            exit()
            return "..."
        if self.age >= self.max_age - 3:
            print('\033[91m'+"I'm getting old"+'\033[0m')
            return "getting old"
        if self.hungriness > self.hungriness_threshold:
            print('\033[91m' + "I'm hungry" + '\033[0m')
            return "hungry"
        elif self.tiredness > self.tiredness_threshold:
            print('\033[91m'+"I'm tired"+'\033[0m')
            return "tired"
        elif self.boredom > self.boredom_threshold:
            print('\033[91m'+"I'm bored"+'\033[0m')
            return "bored"
        else:
            print('\033[91m'+"I'm happy"+'\033[0m')
            return "happy"


class Action(Pet):
    """
    The Action class give the options that users can choose, and it gives an
    output the mood and the pet's status.
    """

    def __init__(self, name):
        Pet.__init__(self, name, hungriness=0, boredom=0, tiredness=0,
                     sickness=False, age=0, waste=0)
        self.name = name

    def display(self):
        """
        It print out the state of the pet in percentage, boolean and integer.
        :return: None
        """
        print("------------")
        print("hungriness", round((self.hungriness / self.max_hungriness)*100),
              "%")
        print("boredom", round((self.boredom / self.max_boredom)*100), "%")
        print("tiredness", round((self.tiredness / self.max_tiredness)*100),
              "%")
        print("sickness", self.sickness)
        print("waste", round((self.waste / self.max_waste)*100), "%")
        print("age", self.age)
        root.after(5000, self.display)

    def clock_tick(self):
        """
        The state of the pet change based on this method
        :return: None
        """
        self.boredom += 1
        self.hungriness += 1
        self.tiredness += 1
        self.waste += 1
        self.age += 1

        if self.hungriness <= 0:
            self.hungriness = 0
        elif self.boredom <= 0:
            self.boredom = 0
        elif self.tiredness <= 0:
            self.tiredness = 0
        elif self.waste <= 0:
            self.waste = 0

        if self.hungriness >= self.max_hungriness:
            self.hungriness = self.max_hungriness
        elif self.boredom >= self.max_boredom:
            self.boredom = self.max_boredom
        elif self.tiredness >= self.max_tiredness:
            self.tiredness = self.max_tiredness
        elif self.waste >= self.waste:
            self.waste = self.waste

        if self.hungriness >= self.max_hungriness and self.boredom >= \
            self.max_boredom and self.tiredness >= self.max_tiredness and \
            self.waste >= self.waste:
            print("...")
            print("You are a bad owner")
            exit()

        if self.tiredness >= 35 and self.hungriness >= 35 \
                and self.waste >= 35:
            self.sickness = True
        root.after(10000, self.clock_tick)

    def see_vet(self):
        """
        If the pet sick which is when the sickness is true, users can take
        the pet to Veterinary.
        This method will reset the tiredness, hungriness and waste, and
        change the sickness to False.
        :return: None
        """
        if self.sickness is True:
            self.tiredness = 0
            self.hungriness = 0
            self.waste = 0
            self.sickness = False
        self.mood()
        root.after(5000, self.clock_tick)
        root.after(5000, self.display)

    def eat(self):
        """
        Users can feed their pet.
        The hungriness will be decreased by 5 when this method run
        :return: None
        """

        self.hungriness -= 5
        if self.hungriness <= 0:
            self.hungriness = 0
        elif self.hungriness >= self.max_hungriness:
            self.hungriness = self.max_hungriness
        self.mood()
        root.after(5000, self.clock_tick)
        root.after(5000, self.display)

    def sleep(self):
        """
        Users can let the pet sleep
        The tiredness will be decreased by 2 when this method run
        :return: None
        """
        self.tiredness -= 2
        if self.tiredness <= 0:
            self.tiredness = 0
        elif self.tiredness >= self.max_tiredness:
            self.tiredness = self.max_tiredness
        self.mood()
        root.after(5000, self.clock_tick)
        root.after(5000, self.display)

    def clean_up(self):
        """
        Users can clean up the pet's waste
        The waste will be decreased by 5 when this method run
        :return: None
        """
        self.waste -= 5
        if self.waste <= 0:
            self.waste = 0
        elif self.waste >= self.waste:
            self.waste = self.waste
        self.mood()
        root.after(5000, self.clock_tick)
        root.after(5000, self.display)

    def play(self):
        """
        Users can play with the pet
        The boredom will be decreased by 3 when this method run
        :return: None
        """
        self.boredom -= 3
        if self.boredom <= 0:
            self.boredom = 0
        elif self.boredom >= self.max_boredom:
            self.boredom = self.max_boredom
        self.mood()
        root.after(5000, self.clock_tick)
        root.after(5000, self.display)


class Window(Frame):
    """
    This class is for the graphic user interface(GUI) by using tkinter
    It will ask users what they want to name their pet and start the game
    by using entry and buttons.

    """

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        startButton = Button(self, text="Start", command=self.openmenu)
        exitButton = Button(self, text="Exit", command=self.clickExitButton)

        # place buttons
        exitButton.place(x=250, y=100)
        startButton.place(x=200, y=100)

        # greeting text
        greetingText = Label(self, text="Welcome to PyPet!")
        greetingText.place(x=180, y=20)
        # asking user to name the pet
        inputText = Label(self, text="What do you want to name your pet?")
        inputText.place(x=30, y=60)

        # entry box for the name of pet
        self.petnameEntry = Entry(self)
        self.petnameEntry.place(x=250, y=60)

    def clickExitButton(self):
        """
        This method show a message and ask users again whether or not they want
        to quite the game.
        :return: None
        """

        # asking users again to prevent accidentally exciting the game
        msg = messagebox.askyesno("PyPet",
                                  "Are you sure, you want to exit the Pypet?")
        if (msg):
            exit()

    def openmenu(self):
        """
        When users enter the name of the pet and the click the stat button, it
        gives users the options that users can choose.
        :return: None
        """

        # getting the name of pet from user input by using get
        petName = self.petnameEntry.get()
        user_pet = Action(petName)
        print("I am your pet,", petName)

        # a label for better design
        window = tk.Toplevel(root)
        w = Label(window, text="What would you like \nto do with your pet?")
        w.pack()

        # menu buttons including feed, play, Vet, sleep, clean
        btFeed = Button(window, text="Feed", command=lambda: user_pet.eat())
        btFeed.pack(pady=3)
        btPlay = Button(window, text="Play", command=lambda: user_pet.play())
        btPlay.pack(pady=3)
        btVet = Button(window, text="Vet", command=lambda: user_pet.see_vet())
        btVet.pack(pady=3)
        btSleep = Button(window, text="Sleep", command=lambda: user_pet.sleep())
        btSleep.pack(pady=3)
        btClean = Button(window, text="Clean", command=lambda: user_pet.
                         clean_up())
        btClean.pack(pady=3)
        root.mainloop()


if __name__ == '__main__':

    """
    The main method will start the program and run the background functions 
    which are clock_tick and display functions. 
    """
    # the size of window for graphic user interface
    root = Tk()
    app = Window(root)
    root.wm_title("Tkinter button")
    root.geometry("500x140")
    root.mainloop()

