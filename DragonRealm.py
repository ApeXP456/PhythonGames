#Created By Jarod L. Cunningham 8-7-2023
#This is a game called Dragon's Realm. It is written in the python language.
import random
import time
import pickle

def display_intro():
    print('''Welcome to NeverDie, a mystical land of dragons and adventure...''')  # Truncated for brevity

class Character:
    def __init__(self, name, char_class, strength, intelligence, agility, max_health=100):
        self.name = name
        self.char_class = char_class
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        self.max_health = max_health
        self.current_health = max_health

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
    print('A Large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(3)

    friendly_cave = random.randint(1, 2)
    if chosen_cave == str(friendly_cave):
        print('The friendly dragon greets you warmly and gives you a large chunk of the treasure!')
    else:
        print('Silence... The dragon has gobbled you down in one big bite!')

# Placeholder for future implementation
# def dragon_encounter():
# Placeholder for future implementation      
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
        cave_number = choose_cave()
        check_cave(cave_number, player_character)

        save_choice = input("Do you want to save your game? (yes/no): ")
        if save_choice.lower() in ['yes', 'y']:
            save_game(player_character)

        print('Do you want to play again? (yes or no)')
        play_again = input()

if __name__ == "__main__":
    main()
