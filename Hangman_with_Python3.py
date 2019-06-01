####Python Hangman Game####
####Python Hangman with words for Python 3####

import random
import os

#For window screen
os.system('mode con: cols=100 lines=50')

#Create User Interface
intro = '''
    ______
    |
    |                       Guessed: %s
    |
    |                       Word #: %s
    |                       Score:	%d
____|_____                  High Score: %d
|        |___
|__________|

Word: %s
Guess: %s
'''
Hangman1 = '''
    ______
    |	 |	
    |	 O					Guessed: %s
    |
    |						Word #:	%s
    |						Score:	%d
____|____ 					High Score: %d
|       |___
|__________|

Word: %s
Guess: %s
'''
Hangman2 = '''
    ______
    |	 |	
    |	 O					Guessed: %s
    |	 |
    |						Word #:	%s
    |						Score:	%d
____|____ 					High Score: %d
|       |___
|__________|

Word: %s
Guess: %s
'''
Hangman3 = '''
    ______
    |	 |	
    |	 O					Guessed: %s
    |	/|
    |						Word #:	%s
    |						Score:	%d
____|____ 					High Score: %d
|       |___
|__________|

Word: %s
Guess: %s
'''
Hangman4 = '''
    ______
    |	 |	
    |	 O					Guessed: %s
    |	/|\								
    |						Word #:	%s
    |						Score:	%d
____|____ 					High Score: %d
|       |___
|__________|

Word: %s
Guess: %s
'''
Hangman5 = '''
    ______
    |	 |	
    |	 O					Guessed: %s
    |	/|\								
    |    |					Word #:	%s
    |						Score:	%d
____|____ 					High Score: %d
|       |___
|__________|

Word: %s
Guess: %s
'''
Hangman6 = '''
    ______
    |	 |	
    |	 O					Guessed: %s
    |	/|\								
    |    |					Word #:	%s
    |   /					Score:	%d
____|____ 					High Score: %d
|       |___
|__________|

Word: %s
Guess: %s
'''
Hangman7 = '''
    ______
    |	 |	
    |	 O					Guessed: %s
    |	/|\								
    |    |					Word #:	%s
    |   / \					Score:	%d
____|____ 					High Score: %d
|       |___
|__________|

Word: %s
Guess: %s
'''


#Start Game
print("--------------------------------")
print("Welcome to Hangman")
print("--------------------------------")
print("Python Hangman with words for Python 3")
print("--------------------------------")

Score = 0
TOP = 0
HighScore = 0
streak = False
while True:
	#Score
	if streak == False:
		HighScore = 0
	if HighScore >= TOP:
		TOP = HighScore
	WrongTry = 0
	MaxGuesses = 7
	Found = False
	UsedLetters =[]
	L = ["float", "str", "list", "set", "int", "tuple", "bool"]
	#Lists
	FloatList = ['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
	StrList = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
	ListList = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
	SetList = ['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
	IntList = ['bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
	TupleList = ['count', 'index']
	BoolList = ['bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


	#Choice List
	HideList = random.choice(L)
	#Choice Word
	if HideList == "float":
		HideWord = random.choice(FloatList)
	elif HideList == "str":
		HideWord = random.choice(StrList)
	elif HideList == "list":
		HideWord = random.choice(ListList)
	elif HideList == "set":
		HideWord = random.choice(SetList)
	elif HideList == "int":
		HideWord = random.choice(IntList)
	elif HideList == "tuple":
		HideWord = random.choice(TupleList)
	elif HideList == "bool":
		HideWord = random.choice(BoolList)
	Word = HideList

	#All Capital
	HideWord = HideWord.upper()
	#Break word to list
	WordList = list(HideWord)
	#Create empty list
	FindList = []
	LenWord = len(HideWord)
	
	#List
	for i in WordList:
		FindList.append("_")
	print(intro % (" ", 0, Score, TOP, FindList, " "))
	
	while not Found and WrongTry<MaxGuesses:

		GuessLetter = input("Give me a letter! ")
		GuessLetter = GuessLetter.upper()
		
		#Check letter
		GuessLetterIsOK = False
		
		while GuessLetterIsOK == False:
			if len(GuessLetter)!=1:
				GuessLetter=input('Wrong! Give me a letter! ')
				GuessLetter = GuessLetter.upper()
			elif GuessLetter in UsedLetters:
				GuessLetter=input('Same letter! Give me a another letter! ')
				GuessLetter = GuessLetter.upper()
			elif GuessLetter.isdigit() == True:
				GuessLetter=input('Not number! Give me a letter! ')
				GuessLetter = GuessLetter.upper()
			elif not GuessLetter.isalpha():
				GuessLetter=input('Only ENGLISH letters are allowed: ')
				GuessLetter = GuessLetter.upper()
			else:
				GuessLetterIsOK = True
		
		#Check if the letter is in the List
		if GuessLetter not in WordList:
			WrongTry = WrongTry + 1
			
			#Correct
			if WrongTry==1 :
				print(Hangman1 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==2 :
				print(Hangman2 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==3 :
				print(Hangman3 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==4 :
				print(Hangman4 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==5 :
				print(Hangman5 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==6 :
				print(Hangman6 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==7:
				print(Hangman7 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))
				print("You lost! The word was %s from the list %s" % (HideWord, HideList) ) 
				another = input("Another one? Y or N: ")
				if (another == "Y") or (another == "y"):
					os.system('cls')
					break
				else:
					exit()
				streak = False
				Score = 0

		#Check if the letter is in List
		elif GuessLetter in WordList:
			for i in range (0,LenWord):
				if(WordList[i]==GuessLetter):
					FindList[i] = GuessLetter

			#Wrong tries
			if WrongTry==0 :
				print(intro % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))
			if WrongTry==1 :
				print(Hangman1 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==2 :
				print(Hangman2 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==3 :
				print(Hangman3 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==4 :
				print(Hangman4 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==5 :
				print(Hangman5 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==6 :
				print(Hangman6 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))	
			if WrongTry==7:
				print(Hangman7 % (UsedLetters, Word, Score, TOP, FindList, GuessLetter))
		
		#Create list with used Letters
		UsedLetters.append(GuessLetter)
		UsedLetters.sort()
		
		#Win
		if WordList == FindList:
			print("You win! The word was %s from the list %s" % (HideWord, HideList) ) 
			Score = Score + 1
			HighScore = HighScore + 1
			streak = True
			Found = True
