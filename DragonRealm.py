# Written by Jarod L. Cunningham
# Python
# Imports and Character Class

import random
import time
import pickle

def display_intro():
    print('''Welcome to NeverDie, a mystical land of dragons and adventure. Here, your courage and wit will be tested as you seek the legendary treasure of the dragons.
          Before you stand two ancient caves: one adorned with mystical runes, suggesting wisdom and magic within; the other surrounded by ominous bones, signaling danger.
          Will you uncover the secrets of NeverDie and claim the dragons' treasure, or will you fall to the perils that lurk in the shadows? The choice is yours.''')

class Character:
    def __init__(self, name, char_class, strength, intelligence, agility, max_health=100):
        self.name = name
        self.char_class = char_class
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        self.max_health = max_health
        self.current_health = max_health
        self.inventory = ["torch", "sword", "potion", "map"]


    def __str__(self):
        return f"{self.name}, the {self.char_class} - Strength: {self.strength}, Intelligence: {self.intelligence}, Agility: {self.agility}, Health: {self.current_health}/{self.max_health}"

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        print(f"{self.name} takes {damage} damage! Current health: {self.current_health}/{self.max_health}")

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print(f"{self.name} heals for {amount}! Current health: {self.current_health}/{self.max_health}")

# Character creation
def create_character():
    print("Character Creation")
    name = input("Enter your character's name: ")
    char_class = choose_class()
    strength, intelligence, agility = distribute_attributes()
    return Character(name, char_class, strength, intelligence, agility, max_health=100)

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
    print("Distribute your attribute points (total: 15): ")
    for attribute in attributes:
        points = -1
        while points < 0 or points > total_points:
            points = int(input(f"Enter points for {attribute} (0-15): "))
            if points > total_points:
                print(f"Not enough points. You have {total_points} points left.")
        attributes[attribute] = points
        total_points -= points
    return attributes["Strength"], attributes["Intelligence"], attributes["Agility"]

# Game Mechanics (Cave Choice and Dragon Encounter)
def encounter(character):
    while True:
        print("What would you like to do?")
        print("1. Move forward")
        print("2. Check your inventory")
        print("3. Consult your map")
        print("4. Exit game")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("You cautiously move forward into the darkness...")
            # Here you can add more specific game logic for moving forward
            break  # Break the loop to proceed to next part of the game

        elif choice == "2":
            print("You check your inventory.")
            for item in character.inventory:
                print(item)
            # Additional logic for inventory management can be added here

        elif choice == "3":
            if "map" in character.inventory:
                print("You consult your map and see that you are currently in the middle of a cave.")
            else:
                print("You don't have a map to consult.")
            # Include more details about the player's location or objectives

        elif choice == "4":
            print("Thanks for playing! Exiting game...")
            exit(0)  # Exits the game

        else:
            print("Invalid input. Please try again.")


def choose_cave():
    cave = ''
    while cave not in ['1', '2']:
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def check_cave(chosen_cave, character):
    print('You start to approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    

    friendly_cave = random.randint(1, 2)
    if chosen_cave == str(friendly_cave):
        print('The friendly dragon greets you warmly and gives you a large chunk of the treasure!')
    else:
        print('A large dragon jumps out in front of you! He opens his jaws and...')
        time.sleep(2)
        dragon_damage = random.randint(1, 30)
        character.take_damage(dragon_damage)
        if character.current_health <= 0:
            print(f"{character.name} has been defeated by the dragon!")
            return False  # Indicates the character has been defeated
        else:
            print('The dragon raises his right wing in defense of the intruders, reveiling a small door way.You rush past the aggitated dragon toward the doorway, you barely surviving the encounter! ')
            #character.heal(10)
        # Small health boost after surviving
        return True  # Indicates the character survived
  
# More Encounters   
def encounter3(character):
    print("After surviving the dragon, you venture deeper into the cave...")
# Placeholder for additional encounters or decision points
    choice = input("Do you wish to continue deeper into the cave or head back? (continue/back): ")
    if choice.lower() == "continue":
        print("You bravely move deeper into the cave...")
# Additional encounters or events here
    else:
        print("You decide to head back, taking the safe route...")

    
# Save and Load Game Functions      
def save_game(character, filename='savegame.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(character, f)
    print("Game saved successfully!")

def load_game(filename='savegame.pkl'):
    try:
        with open(filename, 'rb') as f:
            character = pickle.load(f)
        print("Game loaded successfully!")
        return character
    except FileNotFoundError:
        print("No saved game found.")
        return None

# Main Function
def main():
    print("Welcome to Dragon's Realm!")
    choice = input("Do you want to load a saved game? (yes/no): ")
    if choice.lower() in ['yes', 'y']:
        player_character = load_game()
        if not player_character:
            player_character = create_character()
    else:
        player_character = create_character()
    print(player_character)
    play_again = 'yes'
    while play_again.lower() in ['yes', 'y']:
        display_intro()
        encounter(player_character)
        cave_number = choose_cave()
        survived = check_cave(cave_number, player_character)
        if not survived:
            print('Congradulations on finding the Treasure! Would you like to try again? (yes/no)')
            play_again = input()
            if play_again.lower() in ['yes', 'y']:
                player_character = create_character()  # Create a new character
            continue

        encounter3(player_character)

        save_choice = input("Do you want to save your game? (yes/no): ")
        if save_choice.lower() in ['yes', 'y']:
            save_game(player_character)

        print('Do you want to play again? (yes or no)')
        play_again = input()

if __name__ == "__main__":
    main()
