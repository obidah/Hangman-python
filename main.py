import random 
import os
import time
from body import *
from words import words

random_word = random.choice(words)
old_random_word = random_word

for i in range(len(random_word)-2):
    random_index = random.randrange(len(random_word)-2)
    random_word = random_word.replace(random_word[random_index], "*")

win = True
counter = 6
draw_range = -1
while True:
    print(f"You Have {counter} Chances Left", end = "\n\n")
    print(rope)
    if draw_range > -1:
        print(all_draws[draw_range])
    print("\n")
    print(random_word)
    if old_random_word == random_word:
        print("You Won!")
        time.sleep(1000)
        break
    if counter == 0:
        print("You Lose!")
        print(f"The Word Was {old_random_word}")
        time.sleep(1000)
        break
    old_random_word2 = random_word
    user_guess = str(input("Enter Your Guess: "))
    for e,j in enumerate(old_random_word):
        if j == user_guess and random_word[e] == "*":
            random_word = list(random_word)
            random_word[e] = user_guess
            random_word = "".join(random_word)
            break
    else:
        if old_random_word2 == random_word:
            counter -= 1
            draw_range += 1
    os.system("cls")
