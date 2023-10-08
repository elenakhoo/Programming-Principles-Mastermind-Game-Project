#Code will generate 4 random fruits from the given list
from random import choice
from collections import Counter

#To check user input of fruits in the correct place
def assess(check1, check2):
    statement1 = "Correct fruits in the correct place: " + str(check1)
    statement2 = "Correct fruits but in the wrong place: " + str(check2)

    return print(statement1 + "\n" + statement2 + "\n")

#Game title
print()
print("*************** A Master Mind Computer Game ***************\n")

#Explanation of rules to user
print("************************** RULES **************************\n")
print("- Fruit choices: apple, orange, banana and grape.")
print("- I'm thinking of 4 fruits. Guess what fruits are they?")
print("- Caution: There are repeated fruits!")
print("- Enter your answer one by one...")
print("- You will then be given hints when you answer.\n")
print("************************ Good Luck! ***********************")

#List of fruits given for code to choose at random
fruits = ["apple", "orange", "banana", "grape"]
play = "YES"
guessCount = 1     #It starts with 1 as it is 1 try can't start with 0 tries

#This step will repeat until user inputs no
while play == "YES":

    print()

    answer = []

    for i in range(4):
        answer.append(choice(fruits))   #To add random fruits into the list from the list given above

    #To display answer
    print(str(answer))

#To exit the loop
    win = False
    while True:
        validated = False
        while not validated:
            validated = True

#Creates a list to receive user input
            guess = []
            for i in range(0, 4):
                inputGuess = str(input("Insert your guess: "))
                guess.append(inputGuess.lower().strip())
                if len(guess) != 0:
                    print("Your answer: " + str(guess) + "\n")
                if guess[i] not in fruits:
                    print("Fruit do not exist. Please try again. \n")
                    validated = False    #To validate if answer is fruits if not user input not fruits will go back to line 47
                    break                #To break from line 52 to 59

#To provide count for correct and wrong places
        correctPlace = sum(1 for x, y in zip(answer, guess) if x == y)                  #(X= random list given, Y= user input) If random lists given and user input same it will add 1 counter
        wrongPlace = sum((Counter(answer) & Counter(guess)).values()) - correctPlace    #(Zip creates object)(Object stores data)

#If user input enters all correctly
        if correctPlace == 4:
            break
        else:
            guessCount += 1   #Add guesscount
            assess(correctPlace, wrongPlace)                 #To use function assess to print out statement 1 and 2 from line 7 and 8 based on user input

    print()

    print("You win! " + " The answer is " + str(answer))

#Shows user the total guesses they made
    print("Guess count: " + str(guessCount))

#Asks user if they would like to play again
    play = input("Would you like to play again? (Yes/No) ").upper()

#If user enters other answer besides yes or no it will ask the user again
    while play != "YES" and play != "NO":
        print("Please enter 'Yes' or 'No' only.")
        play= input("Would you like to play again? (Yes/No) ").upper()