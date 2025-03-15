import random

file=open("words.txt","r")
data= file.readline()
words=data.split()
word = random.choice(words)
word=word.upper()

total_chances = 7
guessed_word = "-" * len(word)

while total_chances != 0:
    print(guessed_word)
    letter = input("Guess the letter: ").upper()

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
        print(guessed_word)

        if guessed_word == word:
            print("Congratulations, you won!!!")
            break
    else:
        total_chances -= 1    
        print("Incorrect guess") 
        print(f"Remaining chances: {total_chances}")

# Fixed indentation here
if guessed_word != word
    print("Game over")
    print("You Lose")
    print("All your chances are exhausted")
    print(f"The correct word was {word}")
