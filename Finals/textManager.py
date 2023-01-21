import os
import time
import textwrap
import shutil
import msvcrt

class TextManager:

    def __init__(self, roomNum, textNum):
        self.roomNum = roomNum
        self.textNum = textNum

    def narration(self):
        """For narrative paragraphs"""
        self.displayText()
        self.pressEnter()

    def pressEnter(self):
        """Press enter for confirmation, then clears terminal"""
        input("\nPress ENTER to continue...")
        self.clear()
    
    def clear(self):
        """Clears the terminal"""
        os.system('cls||clear')

    def italicize(self, dialogue):
        """Italicizes strings for player dialogue"""
        return f"\x1B[3m{dialogue}\x1B[0m"
    
    def displayText(self):
        """Makes strings fit in terminal and is called for printing"""
        self.displayRoom()
        width = shutil.get_terminal_size().columns
        filledText = textwrap.fill(self.textLibrary(), width=width)
        lines = filledText.split("\n")
        for line in lines:
            for char in line:
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key == b' ':
                        self.clear()
                        self.displayRoom()
                        print(filledText)
                        return
                print(char, end = "", flush=True)
                time.sleep(0.01)
            print()

    def displayRoom(self):
        """Displays the room and its title"""
        if self.roomNum == 1:
            print("1: A Soaked Start\n")
        elif self.roomNum == 2:
            print("2: Grand Sarcophagus Hall\n")
        elif self.roomNum == 3:
            print("3: Treasure Trove\n")
        elif self.roomNum == 4:
            print("4: The Mummy's Crypt\n")
        elif self.roomNum == 5:
            print("5: Shrine of the Gauntlet\n")
        elif self.roomNum == 6:
            print("Epilogue\n")

    def textLibrary(self): 
        """Lists long strings used in the program"""
        stringList = [
        # [0] Introduction
        "You are Altair, a rookie adventurer who started adventuring in search of fame, glory, and treasure. " 
        "Despite being a novice, you are commissioned to find an ancient artifact called \"the Gauntlet of Nez'Uk\" inside the pyramid of the Yelling Desert. " 
        "You prepare yourself for the journey, eager to prove to yourself that you have what it takes to become one of the greatest adventurers in the world… ",
        
        # [1] Introduction 2
        "You arrive inside the pyramid, engulfed in dust and sand from your trek across the desert. " 
        "Your vision impaired by the particles in the air, you move cautiously through the corridors. " 
        "Suddenly, you hear a tick behind you, and before you can react, your feet lose contact with the ground as you fall into a trap. " 
        "Before you even catch your breath, you find yourself submerged under water. ",
        
        # [2] Room 1 Paragraph 1
        "After a while, you finally reach solid ground and you heave a sigh of relief. " 
        "As you take a little rest, you can't help but think about the water you just escaped from. " 
        + self.italicize("\"If only I had known I would be swimming in water,\"") + " you think to yourself. " 
        + self.italicize("\"I would have made my equipment waterproof!\" ") +
        "You check your gear to see if you can still salvage some of it. Nothing. Everything is covered in murky water, including yourself. " 
        "You shake your head and try to focus on finding the treasure, rather than dwelling on your misfortune. ",

        # [3] Room 1 Choice Dialogue
        "As you survey the room, your eyes fall upon a pile of discarded items on the floor and a door that leads to a pitch-black chamber in the other. " 
        "Where would you like to look?",

        # [4] Room 1 Option 1 - Doorway
        "You barely make out a figure in the center of the room, its silhouette barely visible in the shadows… "
        + self.italicize("\"It's too dark there. I'd better find a light source first.\""),

        # [5] Room 1 Option 2 - Discarded Items
        "You decide to search through the discarded items, and you find a collection of materials that can be used to create a makeshift torch. "
        "With a little bit of creativity, you manage to put together a rudimentary light source that will help you find your way through the dark corridors of the pyramid… ",

        # [6] Room 1 Option 2 - Discarded Items (w/ torch)
        "You have already salvaged all you can get from the pile. Time to move on. ",

        # _________________________________________________________
        # [7] Room 2 Choice Dialogue 
        "As you make your way through the doorway and into the previously pitch-black room, your torch casts a warm glow that illuminates your surroundings. "
        "You are greeted by a grand hall, its walls adorned with intricate carvings and ancient symbols. "
        "In the center of the room stands a large sarcophagus, its lid adorned with hieroglyphics. "
        "Where would you like to look?",

        # [8] Room 2 Option 1 - Door
        "A door with no handles nor seams. "
        + self.italicize("\"There seems to be no way to open this door for now.\""),

        # [9] Room 2 Option 2 - Sarcophagus 
        "You open the ancient coffin, expecting vast amounts of treasures. "
        + self.italicize("\"Empty… wait, what are these symbols? An eye, a scarab, and some kind of bird?\""),

        # [10] Room 2 Paragraph 2 
        "Suddenly, you hear mechanisms whirring. " 
        "You look upwards to find spikes covering the entirety of the ceiling, slowly but surely descending. "
        + self.italicize("\"Oh no… I've gotta get out of here.\""),

        # [11] Room 2 Choice Dialogue (after spikes)
        "Where would you like to go?",
         
        # [12] Room 2 Option 1 - Door (after spikes)
        "As you examine the door more closely, you realize that the mechanisms have changed since you last saw it. "
        "Attached to the door is a coffin-shaped device with five buttons: one in each of the directions of a compass, and one in the center. "
        + self.italicize("\"Looks like I have to press the right button to open this door. But which one is it?\""),

        # [13] Room 2 Option 2 - Sarcophagus (after spikes)
        "An empty coffin in the center of the hall…",

        # [14] Room 2 Option 3 - Return to Room
        "Feeling unsure of what to do next, you decide to take a look around the room once more.",

        # [15] Room 2 Puzzle (Center Button)
        "The door retracts to the ground. "
        + self.italicize("\"Yes!\"") + " you exclaim as you run through the doorway. "
        "Upon reaching the other side, the door behind you closes.",

        # [16] Room 2 Puzzle (NWES Button)
        "BANG! The spikes have lowered. "
        + self.italicize("\"I don't have much time. I've gotta get this right. ")
        + self.italicize("Maybe it has something to do with the sarcophagus?\""),

        # [17] Room 2 Puzzle (third NWES button)
        "The spikes rapidly fall upon you. Crushing both your bones and your dreams into pieces.",

        # _________________________________________________________
        # [18] Room 3 Paragraph 1 
        "After looking around the room, you realize that this must be a treasure room of some sort. "
        "However, you don't see anything that looks like the gauntlet. "
        "Maybe it's deeper inside.",

        # [19] Room 3 Option 1 - Doorway (before dead adventurer) 
        "The door has no knobs but only a claw shaped dent. "
        "Maybe there is something I can use in this room?",

        # [20] Room 3 Option 2 - Treasures
        "There are wall paintings that you can barely make anything out of. "
        "An eye blinking, an upside down scarab, and a flying bird? "
        + self.italicize("\"Huh.\" ") +
        "Other than that, there are huge vases, clothing, jewelry, and something else. "
        + self.italicize("\"Is that blood?\""),

        # [21] Room 3 Option 3 - Blood
        "You follow the trail to find a desecrated corpse. "
        "They must also be an adventurer. "
        "The first thought that comes to your mind is that you might share a similar fate. "
        "After quickly brushing it off and pulling yourself together, you see something shiny on his body.",

        # [22] Room 3 Option 4 - Claw + crumpled note
        "You find a claw and a crumpled note. The crumpled note reads \"Flight leads to freedom.\" "
        "You wonder to yourself what that might mean. "
        "You decided to not think about it too much unless you want to end up dead on the ground like them.",

        # [23] Room 3 - Claw in inventory
        "The claw seems to be the key, lets try it out.",

        # [24] Room 3 Option 5 - Insert claw
        "You insert the claw into the door and you hear gears shifting and the walls shaking. "
        "The door opens.",

        # _________________________________________________________
        # [25] Room 4 Paragraph 1
        "As you step inside the room, you feel your foot lower from the actual ground level, you hear a loud thud and see an hourglass with sand already falling. "
        "You wonder what the hour glass is for, but as you look around the room, you see a mummy that is trapped behind bars.",

        # [26] Room 4 Paragraph 2
        "The bars seem to be lowering?! The mummy is desperately trying to claw its way through it. "
        "You panic for a quick second but realize it doesn't help you in this kind of situation.",

        # [27] Room 4 Option 1 - Door
        "You quickly head to the door to see what it needs to be unlocked. "
        "It's a combination lock and it needs three numbers to be unlocked.",

        # [28] Room 4 - Question
        "Where would you like to search? ", # Placeholder

        # [29] Room 4 Option 2 - Rocks
        "You lift up rocks, hoping it may give you a hint on what numbers the lock contains. "
        "Luckily, one of the rocks you lifted has a number carved under it. 'Three'",

        # [30] Room 4 Option 3 - Mummy
        "You were frightened, but you went near the mummy to inspect its surroundings. "
        "You see from the distance, a number that is written on the floor from where the mummy is standing. "
        "Good thing the mummy moves its feet constantly so you easily see the number, which is 'nine'",

        # [31] Room 4 - No clue in area
        "It seems there is nothing here. " # placeholder
        "I better check somewhere else.",

        # [32] Room 4 - After finding clue on Mummy + rocks
        "After looking around, you could not find the final number. "
        "As you are about to give up, you see a vertical scratched in beside the door. "
        + self.italicize("\"This has to be one.\" ") +
        "So obvious, you're just not smart enough for you to figure that out sooner. "
        "You also notice the cage is lower than before. "
        + self.italicize("\"I better get out of here before the mummy escapes\" ")
        + self.italicize("\"Time to put the code in the door.\""),

        # [33] Room 4 - Already went to this area
        "I've been in this area, I guess I should look somewhere else. "
        "The cage seems like it's gotten lower",

        # [34] Room 4 - Try again (code)
        "Wrong answer! Would you like to input the code again?", # placeholder

        # _________________________________________________________
        # [35] Treasure Room - Paragraph 1 
        "You finally got out of that room after trying several combinations. "
	    "You saw the \"the Gauntlet of Nez'Uk\" lying on its own shrine. "
        "It glows brightly and is made from solid gold. "
        "The light reflects beautifully on the large gem in the middle of it. "
        + self.italicize ("\"Now that is what you call treasure.\" ") +
        "You start walking slowly towards it. "
        "After a few steps, lies before you the treasure! "
        "All you have to do is grab it.",

        # [36] Treasure Room - Paragraph 2 
        "You laid your hands on it and slowly lifted it up from its shrine. "
        "As you admire how beautiful it is, you feel the ground lightly moving. "
        "As it quickly got stronger, that's when it hit you that the place was about to collapse.",
        
        # [37] Treasure Room - Choice 
        "You start sprinting, dodging the falling rocks, to look for an exit, then you encounter three doors. "
        "Each has a symbol that is different from one another. "
        "The first door has an eye. "
        "The second door has a scarab. "
        "And finally, the last door has a bird carved on it. "
        "(Warning! Pick your choice carefully. This can affect the outcome of the game.)",

        # [38] Treasure Room Option 1 - Eye door
        "You open the door with the eye. "
        "When you enter, the door behind you closes and you realize that it is a dark empty room and that there is nowhere to run. "
        + self.italicize("\"This can't be!\"") + " you say, "
        + self.italicize("\"I'm stuck!\" ") +
        "There must be something you have missed because who could've seen this coming. "
        "The pyramid collapses with you stuck in it. "
        "The last thing you see is darkness.",

        # [39] Treasure Room Option 2 - Scarab door
        "You run inside the room and the door behind you closes. "
        "While running you suddenly realize that the room is lit up by candles. "
        "You scan the room and see embalming tools, wraps of linen, and a sarcophagus. "
        "Desperate to get out, you rummage around the room to see what you can do, but then the sarcophagus opens. "
        "A mummy runs towards you and grabs you by your throat and you pass out in shock. "
        "When you open your eyes, the rumbling has stopped and you seem to be immobilized and in a tight place. "
        "You came to the horrifying realization that you are in the sarcophagus and you are going to be there… for a while. ",

        # [40] Treasure Room - Option 3 - Bird door
        "The symbols on the door seem to have appeared before in the previous rooms. "
        "The bird stands out to you the most since it is the one that has appeared most and you've read that it leads to freedom. "
        "Who knew that the random symbols you saw will help you in this kind of situation?",

        # _________________________________________________________
        # [41] Epilogue Paragraph 1 
        "Since you have a strong photographic memory, you figured out the hints that were displayed on the door and safely made it to the exit. "
        "You safely escape the place with the treasure secured with you. "
        "As you were heading home, you thought about your journey so far, and what lies ahead. "
        "You realized that perhaps, adventuring is not for you, and that you can make a fortune with the treasure you worked hard to acquire.",

        # [42] Epilogue Paragraph 2
        self.italicize("\"Hmm.\"") + " you thought to yourself, "
        + self.italicize("\"Although I was paid to do this job, the money they're paying me is not even comparable to what this treasure is worth! ") 
        + self.italicize("Maybe I'd buy a beach house and retire. Yes, I like the sound of that.\" ") +
        "And so that is where your story ends. " 
        "And you live happily ever after!",

        # [43] Game Over
        "Do you want to try again?",

        # [44] Thanks 
        "Thank you for playing! :)"
        ]
        return stringList[self.textNum]
