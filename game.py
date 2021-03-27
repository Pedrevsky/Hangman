import random
import database
from printing_service import draw_hangman


new_words = database.words


def guessing():
    tries = 6
    incorrect_guesses = []
    category_words = []
    category = input("Write a category you want to play: ")
    for element in database.words:
        if element[0] == category:
            category_words.append(element[1])
    if len(category_words) == 0:
        print("You have no words in this category")
        print("\n\n\n")
    else:
        word = random.choice(category_words)
        undercover_list = []

        for element in word:
            if element == " ":
                undercover_list.append(" ")
            else:
                undercover_list.append("_")

        undercover = "".join(undercover_list)
        print(undercover)
        guess = input("Write a letter: ")
        while guess != "EXIT" and tries > 1:
            i = 0
            if guess not in word:
                incorrect_guesses.append(guess.lower())
                incorrect_guesses = list(set(incorrect_guesses))
                tries -= 1
                print(f"Your guess {guess} was incorrect")
                print(f"You have {tries} tries left")
                draw_hangman(tries)
                _incorrect_guesses = " ,".join(incorrect_guesses)
                print(f"Your incorrect guesses: {_incorrect_guesses}\n")
                print(undercover)
                guess = input("Write a letter: ")
            else:
                for element in word:
                    if element.lower() == guess.lower():
                        undercover_list[i] = element
                    i += 1
                undercover = "".join(undercover_list)
                print(undercover)
                if word != undercover:
                    guess = input("Write a letter: ")
                else:
                    print(f"Congratulations! You guessed correctly {word}")
                    break
        else:
            print("You lost")
            draw_hangman(0)
            print(f"Your word was {word}")


def game():
    if len(database.words) == 0:
        print("List of words is empty")
    else:
        name = input("Hi, write your name: ")
        decision = input(f"{name} do you want to start a game? Press 'y' if yes and other key if no: ")
        while decision == "y":
            guessing()
            decision = input(f"{name} do you want to start another game? Press 'y' if yes and other key if no: ")
