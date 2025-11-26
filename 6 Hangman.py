import random
stages = ["""
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / \ 
 |
_|___
""", """
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / 
 |
_|___
""", """
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |       
 |
_|___
""", """
  _______
 |/      |
 |      (_)
 |      \|
 |       |
 |      
 |
_|___
""", """
  _______
 |/      |
 |      (_)
 |       |
 |       |
 |      
 |
_|___
""", """
  _______
 |/      |
 |      (_)
 |       
 |       
 |     
 |
_|___
""", """
  _______
 |/      |
 |      
 |       
 |       
 |     
 |
_|___
"""]

word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)
#print(chosen_word)

placeholder = ""

print(stages[lives])

for i in range(len(chosen_word)):
    placeholder += "-"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Please guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "-"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"It was {chosen_word}. You lose.")

    if "-" not in display:
        game_over = True
        print("You win.")
    
    print(stages[lives])
