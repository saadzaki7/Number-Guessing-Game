#Name: Saad Zaki
#Date: May 4th, 2021
#File Name: SZ - 749885 - Number Guessing
#Description: Number guessing game.
import random
#Setting up the play again loop in a while loop so that it replays indefinitely until the player says otherwise.
play=True
while play:
    #Picking a random number from 1-100
    num=random.randrange(1,101)
    #Varaibles for error checking while loops
    a=True
    b=True
    #Instructions
    print("    Welcome to Saad's Number guessing game!")
    print("The program will pick a random number from 1-100 and its up to you to guess it.")
    print("Each time after guessing you will be told if your guess was too high or too low.\n")
    print("What difficulty would you like to play at?")
    print(" Easy: 15 guesses(Enter 1) \n Medium: 10 guesses(Enter 2)")
    print(" Hard: 5 guesses(Enter 3)")
    #Difficulty input error checking
    while a==True:
        try:
            diff= int(input("Diffuculty:"))
            #Ensures the input is within 0 and 3
            if (diff>=0 and diff<=3)==False:
                #Impossible so it goes to the except condition and loops (Same function as break)
                10/0
            a=False
        except:
            print ("Please enter a valid input.")
    correctAns = False
    #Converts the difficulty input into a useful tries var for a for loop.
    tries=0
    if diff==1:
        tries=14
    elif diff==2:
        tries=9
    elif diff==3:
        tries=4
    #Error checking for guessing input.
    while b==True:
        try:
            guess= int(input("Guess:"))
            b=False
        except:
            print("Please enter a valid input.")
    #Tells user if input is too low or too high
    for i in range (tries):
        if guess==num:
            correctAns==True
            print("You Win! It took you ",(i+1),"tries.")
            break
        elif guess>num:
            print("Too high.")
            print("You have", tries-i, "attempts left.")
            guess= int(input("Guess:"))
        else:
            print("Too low.")
            print("You have", tries-i, "attempts left.")
            guess= int(input("Guess:"))
    if correctAns == False:
        print("You Lose! You failed to guess correctly within your", tries+1,"guesses.")
        print("The correct guess was ", num,".", sep="")
    #Error checking for playing again input.
    c=True
    while c:
        try:
            playAgain=int(input("Do you want to play again?/n Enter 1 for Yes OR 2 for No. \n Play again:"))
            if (playAgain>=0 and playAgain<=2)==False:
                10/0
            c=False
        except:
            print("Please enter a valid input.")
            c=False
    #If the user enetered 2 it exits the play again loop
    if playAgain==2:
        play=False
print("Thank you for playing!")
        
 

        
