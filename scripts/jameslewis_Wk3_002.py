"""
.Synopsis
    Mastermind Game creation
.Description
    1. Get user input
    2. validate user input
    3. produce output for white/red pegs
    4. No color can be repeated
    5. No spaces can be used
    6. Length must be 4 characters
    7. Colors must be within legal_colors
    8a. white-peg: color is correct but wrong location (mark with W character)
    8b. red-ped: color/location is correct (mark with R character)
    8c. No peg: a color is not used (use underscore)
    9. Create Loop for game with win/lose condition
    10. Loss condition player fails to guess within 5 tries
    11. win condition player guesses within 5 tries
    12. Add option to quit game
    
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

#declare Variables
usrInput = ""
pegClr = ['W','R','_']


#1. Get user input
print(colors)
usrInput = input("Type 4 char ")

#2. validate user input
print(usrInput)


#4. No color can be repeated
for index in usrInput:
    if usrInput.count(index) > 1:
        print("repeat char")

#3. produce output for white/red pegs
print(pegClr[:3])


#5. No spaces can be used
if usrInput.isalpha() == False:
    print("no spaces")

#6. Length must be 4 characters
if len(usrInput) != 4:
    print("too many char")

#7. Colors must be within legal_colors
"""
for index in usrInput:
    if index.upper() not in legal_colors:
        print(f"{index.upper()} is not in a color that can be used")
"""


#8b. red-ped: color/location is correct (mark with R character)
#initial use of getting index of lengh of range of usrinput to create two variables to compare indexes that are assumed to be the same length.
for index in range(len(usrInput)):
    clrLoc = usrInput[index]
    clrChk = colors[index]

    if clrLoc.upper() in colors and clrLoc.upper() == clrChk:
        print(pegClr[0])
        #print("Right color/location") used for debug
    #8a. white-peg: color is correct but wrong location (mark with W character)
    if clrLoc.upper() in colors and clrLoc.upper() != clrChk:
        print(pegClr[1])
        #print("Right color/wrong location") used for debug


#8c. No peg: a color is not used (use underscore)
for index in usrInput:
    if index.upper() not in colors:
        print(pegClr[2])


#9. Create Loop for game with win/lose condition
"""
while usrInput != "exit":
    #exit game if "quit" entered to quit game
    if usrInput.lower() == "exit":
        print("exiting")
        break

"""

        
#10. Loss condition player fails to guess within 5 tries
"""
if guesses <= 0:
    loseCon = True
    if loseCon == True:
        print(f"\n{infoMsg[1]}")
        break
"""
        
#11. win condition player guesses within 5 tries
"""
if usrInput[0].upper() == colors[0] and usrInput[1].upper() == colors[1] and usrInput[2].upper() == colors[2] and usrInput[3].upper() == colors[3]:
    winCon = True
if usrInput[0].upper() != colors[0] or usrInput[1].upper() != colors[1] or usrInput[2].upper() != colors[2] or usrInput[3].upper() != colors[3]:
    guesses -= 1
            
if winCon == True and guesses >= 0:
    print("you win")
    break
"""
