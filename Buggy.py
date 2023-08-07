# Created BY Jarod L Cunningham
# This is a example of what a bug looks like in python language
import random
number1=random.randint(1,10)
number2=random.randint(1,10)
print('What is ' + str(number1) +' + '+ str(number2)+ '?')
answer =input()
if answer == number1 + number2:
    print('Correct')
else:
    print('Nope! The answer is ' + str(number1 + number2))