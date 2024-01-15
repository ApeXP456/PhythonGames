#Created By Jarod L. Cunningham 8-7-2023
#This is a game called Dragon's Realm. It is written in the python language.
import random
import time

def displayIntro():
    print('''Welcome to NeverDie, a mystical land of dragons and adventure. Here, your courage and wit will be tested as you seek the legendary treasure of the dragons.
           Before you stand two ancient caves: one adorned with mystical runes, suggesting wisdom and magic within; the other surrounded by ominous bones, signaling danger.
           Will you uncover the secrets of NeverDie and claim the dragons' treasure, or will you fall to the perils that lurk in the shadows? The choice is yours.''')
    # Add code for character customization here
    class Character:
    def __init__(self, name, char_class, strength, intelligence, agility):
        self.name = name
        self.char_class = char_class
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility

    def __str__(self):
        return f"{self.name}, the {self.char_class} - Strength: {self.strength}, Intelligence: {self.intelligence}, Agility: {self.agility}"


def create_character():
    print("Character Creation")
    name = input("Enter your character's name: ")
    char_class = choose_class()
    strength, intelligence, agility = distribute_attributes()

    return Character(name, char_class, strength, intelligence, agility)


def choose_class():
    classes = ["Warrior", "Mage", "Rogue"]
    print("Choose a class:")
    for i, char_class in enumerate(classes, 1):
        print(f"{i}. {char_class}")

    class_choice = 0
    while class_choice < 1 or class_choice > len(classes):
        class_choice = int(input("Enter the number of your class: "))

    return classes[class_choice - 1]


def distribute_attributes():
    total_points = 15
    attributes = {"Strength": 0, "Intelligence": 0, "Agility": 0}

    print("Distribute your attribute points (total: 15):")
    for attribute in attributes:
        points = -1
        while points < 0 or points > total_points:
            points = int(input(f"Enter points for {attribute} (0-15): "))
            if points > total_points:
                print(f"Not enough points. You have {total_points} points left.")

        attributes[attribute] = points
        total_points -= points

    return attributes["Strength"], attributes["Intelligence"], attributes["Agility"]

# Example usage
player_character = create_character()
print(player_character)

# Continue with existing functions...
def chooseCave():
    cave=''
    while cave!= '1'  and cave !="2":
        print('Which cave will you go into? (1 or 2)')
        cave=input()

    return cave
# New function for enhanced decision making
def dragonEncounter():
    # Code for interacting with dragons, making decisions, etc.
def checkCave(chosenCave):
    print('You start to approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A Large dragon was waiting in the cave. As you stand before him he opens his jaws open and...')
    print()
    time.sleep(3)

    friendlyCave=random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('The friendly Dragon greets you warmly and gives you a large chunck of the treasure!')
    else:
        print(' Silence... The Dragon has Gobbled you down in one big bite!')
# Implement save and load feature
def saveGame():
    # Code to save the game state

def loadGame():
    # Code to load a saved game state

# Main game loop
while playagain in ['yes', 'y']:
    # Include character customization at the start
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    # Additional gameplay elements
    dragonEncounter()
    # Option to save the game
    saveGame()

    print('Do you want to play again? Yes or no?')
    playagain = input()
