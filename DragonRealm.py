#Created By Jarod L. Cunningham 8-7-2023
#This is a game called Dragon's Realm. It is written in the python language.
import random
import time

def displayIntro():
    print('''Your are in a land full of Dragons called NeverDie! Some  dragons are friendly while others are very malicious. In the Land of NeverDie,
           it is imperitive that you adhere to your goal to never die. Standing on the dry soil, before you stands two caves and you hear a loud snarl coming from one of the caves.
           In one of the caves is a friendly dragon wating for you, who will share his treasure with you. While the other cave has a hungry and greedy dragon that will eat you on sight.''')
    

def chooseCave():
    cave=''
    while cave!= '1'  and cave !="2":
        print('Which cave will you go into? (1 or 2)')
        cave=input()

    return cave

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

playagain='yes'
while playagain == 'yes' or playagain == 'y':
    displayIntro()
    caveNumber=chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? Yes or no?')
    playagain=input()
