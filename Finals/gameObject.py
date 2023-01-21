from textManager import *

class GameObject:

    def __init__(self, name, roomNum, description, inInventory):
        self.name = name
        self.roomNum = roomNum
        self.description = description
        self.inInventory = inInventory

    def displayInfo(self):
        """Displays object information"""
        TextManager(self.roomNum, self.description).narration()

    def itemInInventory(self):
        """Checks if the item is in the inventory"""
        TextManager(self.roomNum, self.inInventory).narration()