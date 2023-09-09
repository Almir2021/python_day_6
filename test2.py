# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

lenght_of_word = len(chosen_word)
chosen_list = list(chosen_word)
for l in range(lenght_of_word):
    print("_ ", end="")
print()
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
for i in range(lenght_of_word):
    guess = str(input("Take a guess"))
    guess = guess.lower()
    print(guess)
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for l in range(lenght_of_word):
        # print(chosen_list[l])
        if guess == chosen_list[l]:
            print("Right")
        else:
            print("Wrong")
