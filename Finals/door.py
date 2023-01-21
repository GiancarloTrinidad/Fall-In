from textManager import *

class Door:

    def __init__(self, doorNumber, description, doorKey):
        self.name = "Doorway"
        self.doorNumber = doorNumber
        self.description = description
        self.doorKey = doorKey

    def updateDoorKey(self, value):
        """Updates the door key"""
        self.doorKey = value

    def attemptEscape(self):
        """Returns the boolean value of the door key"""
        if self.doorKey:
            return True
        else:
            TextManager(self.doorNumber, self.description).narration()
            return False