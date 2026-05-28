import random
words = ['apple','school','ice','books','pen']
secret_word = random.choice(words)
display = ["_"] * len(secret_word)
lives = 6
while lives > 0:
    print(display)
    letter = input("Enter your letter: ").lower()
    if letter in secret_word:
        print("Correct guess")
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                display[i] = letter
    else:
        print("Wrong guess")
        lives -= 1
    print("Remaining lives:", lives)
    if "_" not in display:
        print("Congratulations! You win")
        print("The word is:", secret_word)
        break
    if lives == 0:
        print("Game Over")
        print("The word was:", secret_word)
    