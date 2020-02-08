# textbased_virtual_pet
This is text based virtual pet 
# Description
This project is about a virtual pet which we named pyPet. We were inspired by Japanese Tamagotchi. It has basic functions such as feed, sleep, play, and clean. Based on what we learned in the class, we were able to create the virtual pet game using class materials and GUIs.
# Documentation explaining the purpose of each file and how to run the code 
I only have one file for our project code. You can easily start playing the game by running the python script. Then, a new window will come up on your screen and will ask you to name your pet. After you name your pet, another window will show up and the window will have five action buttons that you can click. While you click the action buttons, a status of the pet will show on python console. You will notice that the display will update every few seconds. Your goal is to make the pet happy.
# Documentation explaining testing procedures
●	Class PET
○	max_age - Since it is a virtual pet, we intended not to kill the pet just because the pet is aged, so we set the age of the pet to between 10000 to 100000 using the random generator.  We changed the pet's age to 5 to test out if the messages, "I'm getting old" and “...”  is actually working in the mood function. It also exits the program when pet  - SUCCEED
○	We also changed the threshold and max to some lower value like 10 to see if the right mood print out. - SUCCEED
○	As we ran the program, we checked that every mood print out in each condition. - SUCCEED
●	Class Action
○	The display function supposed to show the information every five seconds to inform users. It also calculates the value of the hungriness, boredom, tiredness, waste level in percentage and prints out. We kept running the script and test if it prints out right values. - SUCCEED
○	CLOCK_TICK - This function supposed to change the value of each state for every five seconds and every action. We changed the time to different time like 1 sec, 10 sec, etc. to see if the run.after() is actually working. The function also has a special condition when the tiredness, hungriness, and waste go up certain value, the state of sickness change to True. We also changed to a low value like 5  to test if the state of sickness changes to True. If the owner does nothing with their pet and every percentage is 100%, the owner can kill their pet. We also tested it out to see if the program will exit when the pet is dead by the owner. - SUCCEED.
○	SEE_VET - After few testing, we noticed that we need to reset the tiredness, hungriness, and waste to zero because it kept giving me sickness is True since the value of tiredness, hungriness, and waste were still higher than 30. Once we fixed the logic, we ran it a couple more times to see it change back to False condition, and it worked. - SUCCEED
○	EAT, SLEEP, CLEAN_UP, and PLAY functions - We changed the value of each state from percentage to integer value to test out if it increases or decreases the right states. We also check if the value doesn’t go below zero. It will reset to zero if it goes below zero. - SUCCEED
●	Class Window
○	We checked if every button that we created such as “start”, “exit”, “feed”, “play”, “vet”, “sleep”,  and “clean”  actually changed the value of the states by running the program. - SUCCEED
○	We also checked if the name that we entered in the entry box for the name of the pet printed out on the display.  - SUCCEED

# References
●	https://github.com/lunacodes/PyPet/blob/master/pypet_classes.py - Class, method, and attributes
●	http://page.sourceforge.net/ - PAGE for GUI
●	https://docs.python.org/3/library/tk.html - overall tkinter
●	https://www.python-course.eu/tkinter_labels.php - tkinter label 
●	https://www.python-course.eu/tkinter_buttons.php - tkinter button
●	https://www.python-course.eu/tkinter_entry_widgets.php - tkinter entry
●	https://stackoverflow.com/questions/41661396/tkinter-use-root-after-properly?rq=1 - root.after() for clock_tick function, timer
