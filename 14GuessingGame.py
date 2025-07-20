# problem-14 ---> make a Guessing game --->
import random
gameTime = int(input('How Time you wanna run this game : '))

i =0 
while i <=gameTime :
    guessNumb = int(input('Enter your Guess Number 1 to 5  : '))
    randNumb = random.randint(1,5)
    if guessNumb ==randNumb:
        print('Guess is right')
    else:
        print(f'Worng Guess the right numb is {i} ')
    i =i+1