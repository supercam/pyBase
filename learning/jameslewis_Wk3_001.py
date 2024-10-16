"""
.Synopsis
    Mastermind Game creation
.Description
    1. Get user input
    2. validate user input
    3. produce output for white/red pegs
    3a. white-peg: color is correct but wrong location (mark with W character)
    3b. red-ped: color/location is correct (mark with R character)
    3c. No peg: a color is not used (use underscore)
    3d. No color can be repeated
    4. Create Loop for game with win/lose condition
    5. Loss condition player fails to guess within 5 tries
    6. win condition player guesses within 5 tries
    7. Add option to quit game
    8. Add option to restart game upon win/loss
    
.Author
    James Lewis
.Date
    09/16/2024
"""

legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']

def generate_color_sequence():
    import random
    random.seed()

    sequence = random.sample(range(len(legal_colors)), 4)
    return [legal_colors[i] for i in sequence]

colors = generate_color_sequence()


### You Code Here

#Declare variables to be modified
#usrInput = input("You have an opportunity to guess: ")
pegClr = ['W', 'R', '_']
redPeg = "R"
winCon = False
loseCon = False
ruleInfoOpen = True
ruleExitMsg = "press enter to go back to the game\n"
noEntryMsg = "Not a valid entry\n"
question = "\nplease enter your guess with no spaces between colors.  colors cannot be repeated. "
infoMsg = ["you win, no prize.",
           "You get nothing, you lose, good day sir.",
           "ending game.  thanks for playing.",
           "play again? Yes to restart, No to exit"]

usrInput = ""
usrGuess = []
exitList = ['quit', 'q', 'exit']
guesses = 5


#Create Loop for game with win/lose condition
while usrInput not in exitList or winCon == True:
    #Get user input so user can guess colors
    usrInput = input(f"{question.capitalize()}")

    #exit game if "quit" entered to quit game
    if usrInput.lower() in exitList:
        print(f"\n{infoMsg[2].title()}")
        break

    #check if length greater than 4 but also check if player entered anything only want to get answer of 4
    if len(usrInput) != 4 or usrInput.upper() == "" or usrInput.isalpha() == False:
        print(noEntryMsg)
    else:
        #validate user input for confirmation to compare to guessCon
        print(f"Guess1: {usrInput.upper()}")
        print(colors)


    #rules section of game so player understands the rules.
    if usrInput.lower() == "rules":
        ruleInfoOpen = True
        while ruleInfoOpen == True:
            print("These are the rules: "
                  "\n\tThe user guesses VOGY (violet, orange, green, yellow) "
                  "The computer would output “_WR_ “ (underscore, white, red, underscore). This is because violet is not "
                  "present, orange is, but it’s not in position 2, green is, and in position 3, and then yellow is not present. "
                  "The user then guesses BRGO (blue, red, green, orange) "
                  "The computer would output WWRR (so, first two are right colors, wrong spots, final two are correct) "
                  "Hopefully after this, the user would realize that the correct guess is now RBGO and would guess that. "
                  "The computer will output “You win!” and end. \n")
            usrInput = input(ruleExitMsg)
            if usrInput.lower() == "":
                ruleInfoOpen = False
                break
            else:
                print(noEntryMsg)


#produce output for white/red pegs



#red-peg: color/location is correct (mark with R character)


#No peg: a color is not used (use underscore)

#No color can be repeated

#Loss condition player fails to guess within 5 tries
    if guesses <= 0:
        loseCon = True
        if loseCon == True:
            print(f"\n{infoMsg[1]}")
            break



    if len(usrInput) == 4 and usrInput.isalpha() == True:
        #white-peg: color is correct but wrong location (mark with W character)
        for index in usrInput:
            if usrInput.count(index) > 1:
                print(noEntryMsg)
                continue
            if index[0] in colors:
                usrGuess += pegClr[0]
                #print("true")
            else:
                usrGuess += pegClr[2]
                #print("false")
            for guess in usrGuess:
                print(guess, end="")
                del usrGuess[:]



#win condition player guesses within 5 tries        
        #if usrInput[0].upper() == colors[0] and usrInput[1].upper() == colors[1] and usrInput[2].upper() == colors[2] and usrInput[3].upper() == colors[3]:
        #    winCon = True
        #if usrInput[0].upper() != colors[0] or usrInput[1].upper() != colors[1] or usrInput[2].upper() != colors[2] or usrInput[3].upper() != colors[3]:
            #guesses -= 1
            
        if winCon == True and guesses >= 0:
            print(f"\n{infoMsg[0]}")
            break


