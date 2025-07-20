# problem-14 ---> make a Guessing game --->
import random
gameTime = int(input('How Time you wanna run this game : '))

i =0 
countWorng =[]
countRight =[]
while i <=gameTime :
    guessNumb = int(input('Enter your Guess Number 1 to 5  : '))
    randNumb = random.randint(1,5)
    if guessNumb ==randNumb:
        print('Guess is right')
        countRight.append(guessNumb)
    else:
        print(f'Worng Guess the right numb is {i} ')
        countWorng.append(guessNumb)
        
    i =i+1
print(f"Worng {len(countWorng) } times --> {countWorng}\n Right {len(countRight) } times --> {countRight}")