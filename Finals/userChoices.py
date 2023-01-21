from textManager import *

class UserChoices:

    def __init__(self, roomNum, question, choices):
        self.roomNum = roomNum
        self.question = question            # Question number in textManager
        self.choices = choices              # Choices the player can make (list)
        
    def getUserChoice(self):
        """Prints the question and returns the user's choice."""
        question = TextManager(self.roomNum, self.question)
        question.displayText()
        choiceMade = False

        while choiceMade == False:
            for i, choice in enumerate(self.choices):
                print(f"{i+1}) {choice}")
            userInput = input("\n")
            try:
                choiceIndex = int(userInput) - 1
                if 0 <= choiceIndex < len(self.choices):
                    choiceMade = True
                    question.clear()
                    return choiceIndex
                else:
                    question.clear()
                    print("Invalid choice. Try again.")
            except ValueError:
                question.clear()
                print("Invalid input. Please enter a number.")