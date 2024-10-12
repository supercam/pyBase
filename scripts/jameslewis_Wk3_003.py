"""
.Synopsis
    Mastermind Game creation
.Description
    1a. Create Loop for game
    1b. Get user input
    2a. validate user input
    2b. length must be 4 characters
    2c. No spaces can be used
    2d. No color can be repeated
    2e. Colors must be within legal_colors
    3a. produce output for white/red pegs
    3b. white-peg: color is correct but wrong location (mark with W character)
    3c. red-ped: color/location is correct (mark with R character)
    3d. No peg: a color is not used (use underscore)
    4a. win/lose condition
    4b. Loss condition player fails to guess within 5 tries
    4c. win condition player guesses within 5 tries
    5. Add option to quit game
    
    
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


### Your Code Here

#Declare Variables
usrInput = ""
pegClr = ['W','R','_']
winCon = False
loseCon = False
ruleInfoOpen = True
infoMsgChk = True
clrLoc = ""
clrChk = ""
ruleExitMsg = "press enter to go back to the game\n"
noEntryMsg = "Not a valid entry\n"
question = "please enter your guess with no spaces between colors.  colors cannot be repeated. "
infoMsg = ["you win, no prize.",
           "You get nothing, you lose, good day sir.",
           "ending game.  thanks for playing.",
           "play again? Yes to restart, No to exit",
           "colors cannot be repeated, try again",
           "is not a valid color, try again",
           "possible colors are:"]
usrInput = ""
usrGuess = []
exitList = ['quit', 'q', 'exit']
guesses = 5
lglClrs = ""


#convert legal_colors to string
for i in legal_colors:
    lglClrs += i + ','


#1a. Create Loop for game to establish basic foundation
while usrInput not in exitList or winCon != True or loseCon != True:
    #1b. Get user input
    if infoMsgChk == True:
        print(f"{infoMsg[6].capitalize()} {lglClrs[:15]}")
    usrInput = input(f"\n{question.capitalize()}")


    #exit game if "quit" entered to quit game
    if usrInput.lower() in exitList:
        print(f"\n{infoMsg[2].capitalize()}")
        break

    #2. validate user input
    #2b. check if length greater than 4 but also check if player entered anything only want to get answer of 4
    #2c. no spaces can be used
    if len(usrInput) != 4 or usrInput.upper() == "" or usrInput.isalpha() == False:
        print(f"Guess1: {usrInput.upper()}")
        print(noEntryMsg)
        infoMsgChk = False

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

#2d. No color can be repeated also double check correct validation of input
    if len(usrInput) == 4 and usrInput.isalpha() == True:
        infoMsgChk = False
        lglClrChk = False
        print(f"Guess1: {usrInput.upper()}")

        for index in range(len(usrInput)):
            clrLoc = usrInput[index]
            clrChk = colors[index]

            #colors must not repeat
            if usrInput.count(clrLoc) > 1:
                print(f"\n{infoMsg[4].capitalize()}")
                break
            #2e. Colors must be within legal_colors
            elif clrLoc.upper() not in legal_colors:
                lglClrChk = True
                print(f"\n{clrLoc.upper()} {infoMsg[5]}")
                break

            #3a. product output for pegs
            #3c. white-peg: color is correct but wrong location (mark with W character)
            #initial use of getting index of lengh of range of usrinput to create two variables to compare indexes that are assumed to be the same length.
            elif clrLoc.upper() in colors and clrLoc.upper() == clrChk:
                print(pegClr[1], end="")
                #print("Right color/location") #used for debug
            #3b. red-peg: color/location is correct (mark with R character)
            elif clrLoc.upper() in colors and clrLoc.upper() != clrChk:
                print(pegClr[0], end="")
                #print("Right color/wrong location") #used for debug
            #3d. No peg: a color is not used (use underscore)
            elif clrLoc.upper() not in colors:
                print(pegClr[2], end="")

        #4a. win condition player guesses within 5 tries
        if usrInput[0].upper() == colors[0] and usrInput[1].upper() == colors[1] and usrInput[2].upper() == colors[2] and usrInput[3].upper() == colors[3]:
            winCon = True
        elif lglClrChk == True:
            continue
        else:
            guesses -= 1
        if winCon == True and guesses >= 1:
            print(f"\n{infoMsg[0].capitalize()}")
            break

        #4b. Loss condition player fails to guess within 5 tries
        if guesses <= 0 and winCon == False:
            loseCon = True
        if loseCon == True:
            print(f"\n{infoMsg[1].capitalize()}")
            break
 
