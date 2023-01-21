from gameObject import *
from door import *
from textManager import *
from userChoices import *
from asciiArt import *

class EscapeRoom:
    
    def __init__(self):
        self.roomNum = 1
        self.alive = True
        
# __________________________________________________________________________________

    def start(self):
        # Game Introduction
        intro1 = TextManager(0, 0)
        intro2 = TextManager(0, 1)
        titleArt = AsciiArt(0)
        pyramidArt = AsciiArt(1)

        print("(Press SPACE to skip text animations)\n\n")
        intro1.displayText()
        titleArt.display()
        intro1.pressEnter()
        pyramidArt.display()
        intro2.narration()
        self.firstRoom()

# __________________________________________________________________________________

    def firstRoom(self):
        haveTorch = False
        firstDoor = Door(self.roomNum, 4, haveTorch)
        discardedItems = GameObject("Discarded Items", self.roomNum, 5, 6)
        choice1 = UserChoices(self.roomNum, 3, [firstDoor.name, discardedItems.name])

        paragraph1 = TextManager(self.roomNum, 2)
        torchArt = AsciiArt(9)

        paragraph1.narration()
        
        while self.roomNum == 1:
            userChoice = choice1.getUserChoice()
            # Checks if the player has the torch to proceed to the next room
            if userChoice == 0 and firstDoor.attemptEscape():
                self.roomNum += 1
                self.secondRoom()
            # If torch is already acquired
            elif userChoice == 1 and haveTorch:
                discardedItems.itemInInventory()
            # Acquiring the torch
            elif userChoice == 1:
                torchArt.display()
                discardedItems.displayInfo()
                haveTorch = True
                firstDoor.updateDoorKey(haveTorch)

# __________________________________________________________________________________

    def secondRoom(self):
        self.spikesActive = False
        self.buttonTries = 2
        centerButton = False

        secondDoor = Door(self.roomNum, 8, centerButton)
        sarcophagus = GameObject("Sarcophagus", self.roomNum, 9, 13)
        choice1 = UserChoices(self.roomNum, 7, [secondDoor.name, sarcophagus.name])
        choice2 = UserChoices(self.roomNum, 11, [secondDoor.name, sarcophagus.name])   
        buttons = UserChoices(self.roomNum, 12, ['North', 'West', 'Center', 'East', 'South', "Return to Room"])

        spikesShown = TextManager(self.roomNum, 10)
        backToRoom = TextManager(self.roomNum, 14)
        correctButton = TextManager(self.roomNum, 15)
        wrongButton = TextManager(self.roomNum, 16)
        spikesFell = TextManager(self.roomNum, 17)
        sarcophagusArt = AsciiArt(7)
        
        # When player is looking around the room
        def lookAround():
            while self.roomNum == 2:
                # Shows different dialogue and options if spikes are activated or not
                if self.spikesActive:
                    userChoice = choice2.getUserChoice()
                    if userChoice == 0:
                        pressButton()
                    else:
                        sarcophagus.itemInInventory()
                else:
                    userChoice = choice1.getUserChoice()
                    if userChoice == 0:
                        secondDoor.attemptEscape()
                    # Activates the "spikes"
                    else:
                        sarcophagusArt.display()
                        sarcophagus.displayInfo()
                        spikesShown.narration()
                        self.spikesActive = True

        # Responsible for any button related choice
        def pressButton():
            while self.alive:
                buttonPressed = buttons.getUserChoice()
                # If player decides to look around the room
                if buttonPressed == 5:
                    backToRoom.narration()
                    lookAround()
                # Spoilers: Correct button pressed
                elif buttonPressed == 2:
                    correctButton.narration()
                    self.roomNum += 1
                    self.thirdRoom()
                # Wrong button
                else:
                    if self.buttonTries == 0:
                        self.alive = False
                        spikesFell.narration()
                        self.gameOver(self.roomNum)
                    self.buttonTries -= 1
                    wrongButton.narration()

        lookAround()
        
# __________________________________________________________________________________

    def thirdRoom(self):
        foundClaw = False

        thirdDoor = Door(self.roomNum, 19, foundClaw)
        treasures = GameObject("Treasures", self.roomNum, 20, 23)
        choice = UserChoices(self.roomNum, 11, [thirdDoor.name, treasures.name])
        
        paragraph1 = TextManager(self.roomNum, 18)
        followBlood = TextManager(self.roomNum, 21)
        claw = TextManager(self.roomNum, 22)
        doorOpens = TextManager(self.roomNum, 24)
        deadManArt = AsciiArt(8)

        paragraph1.narration()

        while self.roomNum == 3:
            userChoice = choice.getUserChoice()
            # Checks if the player already has the key (claw)
            if userChoice == 0 and thirdDoor.attemptEscape():
                doorOpens.narration()
                self.roomNum += 1
                self.fourthRoom()
            # If claw is found but player decides to go back to the same spot
            elif userChoice == 1 and foundClaw == True:
                treasures.itemInInventory()
            # Acquiring the claw
            elif userChoice == 1:
                treasures.displayInfo()
                followBlood.displayText()
                deadManArt.display()
                followBlood.pressEnter()
                claw.narration()
                foundClaw = True
                thirdDoor.updateDoorKey(foundClaw)
                
# __________________________________________________________________________________

    def fourthRoom(self):
        self.rock, self.mummy = False, False
        self.code = "193"
        self.mummyCage = 6
        
        fourthDoor = Door(self.roomNum, 27, self.code)
        rock = GameObject("Rocks", self.roomNum, 29, 33)
        mummy = GameObject("Mummy", self.roomNum, 30, 33)
        choice1 = UserChoices(self.roomNum, 28, [rock.name, "Old vase", "Basket", mummy.name, fourthDoor.name])
        choice2 = UserChoices(self.roomNum, 28, [fourthDoor.name])                   # Encountering door
        choice3 = UserChoices(self.roomNum, 28, ["Input Code", "Explore room"])    # Infront of the door
        tryAgain = UserChoices(self.roomNum, 34, ["Yes", "No"])
        
        paragraph1 = TextManager(self.roomNum, 25)
        barsLowering = TextManager(self.roomNum, 26)
        combinationLock = TextManager(self.roomNum, 27)
        mummyArt = AsciiArt(6)

        paragraph1.displayText()
        mummyArt.display()
        paragraph1.pressEnter()
        barsLowering.narration()
        choice2.getUserChoice()            
        combinationLock.narration()
        
        userChoice = choice3.getUserChoice()

        def searchRoom():
        # For searching around the room
            lastNumber = TextManager(self.roomNum, 32)
            nothingHere = TextManager(self.roomNum, 31)
            areaChoice = choice1.getUserChoice()
            # if player decides to go back in the same area
            if (areaChoice == 0 and self.rock) or (areaChoice == 3 and self.mummy):
                rock.itemInInventory()
                self.mummyCage -= 1
                print(f"Actions left before the mummy escapes: {self.mummyCage}")
                searchRoom()
            # Finding one of the clues
            elif areaChoice == 3:
                mummy.displayInfo()
                self.mummy = True
                searchRoom()
            elif areaChoice == 0:
                rock.displayInfo()
                self.rock = True
                searchRoom()
            # Will only trigger if self.rock and self.mummy are True and player chooses 5 (- 1)
            elif self.rock and self.mummy and (areaChoice == 4):
                lastNumber.narration()
                self.mummyCage -= 1
                print(f"Actions left before the mummy escapes: {self.mummyCage}")
                inputCode()
            # player chooses 5 (- 1), the doorway, prompts them to input the code
            elif areaChoice == 4:
                inputCode()
            # If there is nothing in the area
            else:
                nothingHere.narration()
                self.mummyCage -= 1
        
        def inputCode():
        # Loops until player inputs the correct code, or until the mummy escapes, or until they exit the code input
            while self.mummyCage != 0:
                # Player can progress if they input the correct code (193)
                if input("Input the code: ") == self.code:
                    self.roomNum += 1
                    self.treasureRoom()
                # If player didn't get the correct code, mummy's cage lowers
                elif tryAgain.getUserChoice() == 0:        
                    self.mummyCage -= 1
                    print(f"Actions left before the mummy escapes: {self.mummyCage}")
                    inputCode()
                else:
                    break

        while self.alive:
            # Loop will break when player dies
            if self.mummyCage == 0:
                break
            # For inputting the code in the door
            elif userChoice == 0:
                print(f"Actions left before the mummy escapes: {self.mummyCage}")
                inputCode()
            # Searching around the room
            else:
                print(f"Actions left before the mummy escapes: {self.mummyCage}")
                searchRoom()
        self.gameOver(self.roomNum)
        
# __________________________________________________________________________________

    def treasureRoom(self):
        choice = UserChoices(self.roomNum, 37, ["Eye", "Scarab", "Bird"])
        paragraph1 = TextManager(self.roomNum, 35)
        treasureAcquired = TextManager(self.roomNum, 36)
        gauntletArt = AsciiArt(2)
        doorArt = AsciiArt(3)

        paragraph1.clear()
        gauntletArt.display()
        paragraph1.narration()
        treasureAcquired.narration()
        doorArt.display()
        # There are three doors, but can only choose one. Each door with different ending
        doorChoice = choice.getUserChoice()
        self.roomNum += 1
        self.epilogue(doorChoice)

# __________________________________________________________________________________

    def epilogue(self, doorChosen):
        eyeEnding = TextManager(self.roomNum, 38)
        scarabEnding = TextManager(self.roomNum, 39)
        birdEnding = TextManager(5, 40)
        epilogue1 = TextManager(self.roomNum, 41)
        epilogue2 = TextManager(self.roomNum, 42)
        thanks = TextManager(0, 44)
        theEndArt = AsciiArt(4)

        # Each door the player chooses has its own ending
        if doorChosen == 0:
            eyeEnding.narration()
        elif doorChosen == 1:
            scarabEnding.narration()
        elif doorChosen == 2:
            birdEnding.narration()
            epilogue1.narration()
            epilogue2.narration()

        theEndArt.display()
        thanks.displayText()
        input("\nPress ENTER to exit...")
        exit()

# __________________________________________________________________________________

    def gameOver(self, roomNum):
        # Will trigger if the user dies
        restart = UserChoices(0, 43, ["Yes", "No"])
        thanks = TextManager(0, 44)
        gameOverArt = AsciiArt(5)
        
        thanks.clear()
        gameOverArt.display()

        # Asks the player if they want to play the game again
        if restart.getUserChoice() == 0:
            self.alive = True
            if roomNum == 2:
                self.secondRoom()
            elif roomNum == 4:
                self.fourthRoom()
        else:
            self.epilogue(3)
