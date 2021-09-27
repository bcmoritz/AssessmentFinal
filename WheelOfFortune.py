import random
from random import randrange
import sys
import time

## Initialize Player Status
P1 = {'Name': None, 'Bank': 0, 'Round Bank': 0, 'SpinAgain': 0}
P2 = {'Name': None, 'Bank': 0, 'Round Bank': 0, 'SpinAgain': 0}
P3 = {'Name': None, 'Bank': 0, 'Round Bank': 0, 'SpinAgain': 0}

##Prompt Player Names
P1['Name'] = input('Player 1 Name: ')
P2['Name'] = input('Player 2 Name: ')
P3['Name'] = input('Player 3 Name: ')


## Initialize vowels
vowels = 'AEIOU'
Consonants = 'BCDFGHJKLMNPQRSTVWYXZ'

## Initialize Round variables
RoundNumber = 1
RandomNum = 0
RoundWord = ''
RoundCategory = ''
RoundGuess = ''
Solved = False

CurrentPlayer = P1

## Initialize the wheel
segments = []
segments.append('LOSE TURN')
segments.append('BANKRUPT')
for i in range(1,22):
    segments.append(randrange(2, 18)*50)

##Initialize Categories and Words
words = ['PURPLE' , 'BRIAN', 'R L STINE', 'LISTENER', 'RESTLESS']
categories = ['THINGS THAT RHYME WITH URPLE', 'COOL FIRST NAMES', 'FAMOUS CHILDRENS AUTHORS', 'TYPE OF PERSON', 'STATE OF BEING']

## Generates random word and corresponding phrase from a list of possible ones and deletes so it will not be used again
def GetWordPhrase():
    global words
    global categories
    global RoundGuess
    global RoundWord
    global RoundCategory
    global randomNum
    WordFinal = ''
    randomNum = randrange(len(words))
    WordFinal = words[randomNum]
    print(WordFinal)
    while len(RoundGuess) < (len(WordFinal)):
        for i in range(0, len(WordFinal)):
            if WordFinal[i].isalpha(): 
                RoundGuess = RoundGuess + '_'
            else:
                RoundGuess = RoundGuess + ' '
    RoundWord = words[randomNum]
    RoundCategory = categories[randomNum]
    words.remove(words[randomNum])
    categories.remove(categories[randomNum])

## Player wins round
def Win():
    global RoundNumber
    global CurrentPlayer
    global Solved
    global RoundWord
    global RoundCategory
    global RoundGuess
    CurrentPlayer['Bank'] = CurrentPlayer['Bank'] + CurrentPlayer['Round Bank']
    print('Congratulations player' , CurrentPlayer['Name'] , '.\n The current totals are:\n Player 1:' , P1['Bank'] , '\n Player 2:' , P2['Bank'] , '\n Player 3:' , P3['Bank'])
    P1['Round Bank'] = 0
    P2['Round Bank'] = 0
    P3['Round Bank'] = 0
    Solved = True
    RoundNumber += 1
    RoundWord = ''
    RoundCategory = ''
    RoundGuess = ''

    
## Changed the current player
def ChangePlayer():
    global CurrentPlayer
    if CurrentPlayer == P1:
        CurrentPlayer = P2
    elif CurrentPlayer == P2:
        CurrentPlayer = P3
    else:
        CurrentPlayer = P1

## Spin the wheel
def SpinWheel():
    global random
    global segments
    print('.....')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('.')
    time.sleep(1)
    Spin = random.randint(0,23)
    print('You spun ' , segments[Spin]) , '\n'
    return segments[Spin]

## Player Loses Turn
def LoseTurn():
    print('Sorry player' , CurrentPlayer['Name'] , 'your turn is over.')
    ChangePlayer()

## Bankrupts a player and ends their turn
def Bankrupt():
    CurrentPlayer['Round Bank'] = 0
    print("OH NO BANKRUPT")
    LoseTurn()

## Plays a single turn
def PlayTurn():
    global RoundNumber
    global RoundWord
    global RoundCategory
    global RoundGuess
    global Consonants
    global CurrentPlayer
    TurnChoice = 0
    ValidChoice = ''
    ConsonantMultiplier = 0
    print('\nCurrent Player:' , CurrentPlayer['Name'] , '\nCurrent Money' ,CurrentPlayer['Round Bank'])
    print('Current Category: ' , RoundCategory)
    print('Following is the word you will be guessing:' , RoundGuess) , '\nRound Number:', RoundNumber ,'\n'
    if RoundNumber == 3:
        if P1['Bank'] > CurrentPlayer['Bank']:
            CurrentPlayer = P1
        if P2['Bank'] > CurrentPlayer['Bank']:
            CurrentPlayer = P2
        if P3['Bank'] > CurrentPlayer['Bank']:
            CurrentPlayer = P3
        FirstConsonant = '1'
        SecondConsonant = '1'
        ThirdConsonant = '1'
        FirstVowel = '1'
        for i in range(len(RoundWord)):
            if RoundWord[i].upper() == 'R':
                RoundGuess = RoundGuess[:i] + 'R' + RoundGuess[i+1:]
            if RoundWord[i].upper() == 'S':
                RoundGuess = RoundGuess[:i] + 'S' + RoundGuess[i+1:]
            if RoundWord[i].upper() == 'T':
                RoundGuess = RoundGuess[:i] + 'T' + RoundGuess[i+1:]
            if RoundWord[i].upper() == 'L':
                RoundGuess = RoundGuess[:i] + 'L' + RoundGuess[i+1:]
            if RoundWord[i].upper() == 'N':
                RoundGuess = RoundGuess[:i] + 'N' + RoundGuess[i+1:]
            if RoundWord[i].upper() == 'E':
                RoundGuess = RoundGuess[:i] + 'E' + RoundGuess[i+1:]
        print('Well done Player', CurrentPlayer['Name'], '\n\nYou have made it to the final round')
        print('The FINAL ROUND category is' , RoundCategory, 'we have guessed R S T L N E for you.\nThe current phrase is', RoundGuess)    
        while FirstConsonant.upper() not in Consonants:
            FirstConsonant = input('Please enter your first consonant: ')
        while SecondConsonant.upper() not in Consonants:
            SecondConsonant = input('Please enter your second consonant: ')
        while ThirdConsonant.upper() not in Consonants:
            ThirdConsonant = input('Please enter your third consonant: ')
        while FirstVowel.upper() not in vowels:
            FirstVowel = input('Please enter your first vowel: ')
        for i in range(len(RoundWord)):
            if RoundWord[i] == FirstConsonant.upper():
                RoundGuess = RoundGuess[:i] + FirstConsonant.upper() + RoundGuess[i+1:]
            if RoundWord[i] == SecondConsonant.upper():
                RoundGuess = RoundGuess[:i] + SecondConsonant.upper() + RoundGuess[i+1:]
            if RoundWord[i] == ThirdConsonant.upper():
                RoundGuess = RoundGuess[:i] + ThirdConsonant.upper() + RoundGuess[i+1:]
            if RoundWord[i] == FirstVowel.upper():
                RoundGuess = RoundGuess[:i] + FirstVowel.upper() + RoundGuess[i+1:]
        print('\n\nThe final preview is' , RoundGuess)
        FinalGuess = input('\n\n\nPlease enter one final guess: ')
        if FinalGuess.upper() == RoundWord.upper():
            print('Well Done' , CurrentPlayer['Name'] , 'you have won', CurrentPlayer['Bank'])
        else:
            print('Sorry the correct answer is: ' , RoundWord , 'better luck next time.')
        RoundNumber += 1
        sys.exit()
        

    else:
        if RoundNumber == 3:
            exit
        ValidChoice = input('\nChoose and option.\n1. Solve the puzzle\n2. Buy a vowel\n3. Spin the wheel\n ')
        if (ValidChoice == str('1')):
            if input('Please guess the puzzle: ').upper() == RoundWord.upper():
                Win()
            else:
                LoseTurn()
        elif (ValidChoice == str('2')):
            VowelMultiplier = 0
            if(CurrentPlayer['Round Bank']) > 250:
                VowelGuess = input('What vowel would you like to buy: ').upper()
                CurrentPlayer['Round Bank'] = CurrentPlayer['Round Bank'] - 250
                if len(VowelGuess) != 1:
                    print('Sorry you should enter a single letter of the english language nexdrt time.')
                    LoseTurn()
                elif VowelGuess.upper() in vowels:
                    for i in range(len(RoundWord)):
                        if RoundGuess[i] == VowelGuess:
                            VowelGuess = ''
                        elif RoundWord[i] == VowelGuess:
                            RoundGuess = RoundGuess[:i] + VowelGuess + RoundGuess[i+1:]
                            VowelMultiplier += 1
                    if ConsonantMultiplier == 0:
                        print('Sorry that vowel was not a correct guess.')
                        LoseTurn()
                elif VowelGuess.upper() in Consonants:
                    print('Sorry you accidentally guessed a consonants')
                    LoseTurn()
                else:
                    exit                    
            else:
                print('Sorry not enough money.')
        elif (ValidChoice == str('3')):
            TurnSpin = SpinWheel()
            if TurnSpin == 'LOSE TURN':
                LoseTurn()
            elif TurnSpin == 'BANKRUPT':
                Bankrupt()
            else:
                ConsonantGuess = input('What consonant would you like to guess: ').upper()
                if len(ConsonantGuess) != 1:
                    print('Sorry you should enter a single letter of the english language net time.')
                    LoseTurn()
                elif ConsonantGuess.upper() in Consonants:
                    for i in range(len(RoundWord)):
                        if RoundGuess[i] == ConsonantGuess:
                            ConsonantGuess = ''
                        elif RoundWord[i] == ConsonantGuess:
                            RoundGuess = RoundGuess[:i] + ConsonantGuess + RoundGuess[i+1:]
                            ConsonantMultiplier += 1
                    CurrentPlayer['Round Bank'] = CurrentPlayer['Round Bank'] + (ConsonantMultiplier * TurnSpin)
                    if ConsonantMultiplier == 0:
                        print('Sorry that consonant was not a correct guess.')
                        LoseTurn()
                elif ConsonantGuess.upper() in vowels:
                    print('Sorry you accidentally guessed a vowel')
                    LoseTurn()
                else:
                    exit
        else:
            ValidChoice = input('Choose and option.\n1. Solve the puzzle\n2. Buy a vowel\n3. Spin the wheel\n ')

## Plays a round of Wheel Of Fortune until completion
def PlayRound():
    global Solved
    print('Round' , RoundNumber)
    while Solved != True:
        PlayTurn()  
    Solved = False

while RoundNumber < 4:
    RoundInfo = GetWordPhrase()
    PlayRound()