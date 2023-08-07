# Created by Jarod Cunningham
# This is a Guess the Number Game.
import random

guessesTaken=0

print('Why Hello Stranger! What is your name?')
myName=input()

number=random.randint(1,20)
print('Huh, '+ myName +', That is a werid name. Well ' +myName+ ' I will give you 5 tries to predict a number that i am thinking of, it is bewteen 1 and 20.')

for guessesTaken in range(5):
    print('What is the number? Think carefully.') #Four Spaces im front of "print"
    guess=input()
    guess=int(guess)

    if guess < number:
        print('WRONG!!! Your guess is to low.') #Eight spaces infront of 'print'

    if guess > number:
        print('WRONG!!! Your guess is to high.')
    if guess==number:
          break
if guess == number:
    guessesTaken=str(guessesTaken + 1)
    print('Well crap, I guess that I owe you a Good Job,' + myName + '! You guessed my number in ' + guessesTaken + ' guesses! Your not such a bad guesser after all.')

if guess != number:
        number=str(number)
        print('Nope. Times Up! The Number I was thinking of was ' + number + ' You have done nothing but waste my time, and prove my point.')