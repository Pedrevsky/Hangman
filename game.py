import random
import database
from printing_service import draw_hangman


def check_all_words(checklist):
    return len(checklist) != 0


def make_undercover(word):
    undercover_list = []
    for element in word:
        if element == " ":
            undercover_list.append(" ")
        else:
            undercover_list.append("_")
    return "".join(undercover_list)


def get_single_category(category):
    return [element[1] for element in database.words if element[0] == category]


def check_category(category_words):
    return len(category_words) != 0


def code_word(word, purpose):
    undercover_list = []
    for element in word:
        if element == " ":
            undercover_list.append(" ")
        elif element == "-":
            undercover_list.append("-")
        else:
            undercover_list.append("_")

    if purpose == "print":
        print("".join(undercover_list))
    else:
        return undercover_list


def guessing_letters(guess, word):
    undercover = "".join(code_word(word, "assignment"))
    undercover_list = code_word(word, "assignment")
    tries = 6
    incorrect_guesses = []
    while guess != "EXIT" and tries >= 0:
        i = 0
        if guess.lower() not in word:
            if guess.lower() not in incorrect_guesses:
                incorrect_guesses.append(guess.lower())
                incorrect_guesses = list(set(incorrect_guesses))
                tries -= 1
                print(f"Your guess {guess} was incorrect, you have {tries} tries left")
                draw_hangman(tries)
                _incorrect_guesses = ", ".join(incorrect_guesses)
                print(f"Your incorrect guesses: {_incorrect_guesses}\n")
                print(undercover)
                guess = input("Write a letter: ")
            else:
                print(f"You already have guessed incorrectly {guess.lower()}")
                print(undercover)
                guess = input("Write a letter: ")
        else:
            for element in word:
                if element.lower() == guess.lower():
                    undercover_list[i] = element
                i += 1
            undercover = "".join(undercover_list)
            if word != undercover:
                print(undercover)
                guess = input("Write a letter: ")

            else:
                print(f"Congratulations! You guessed correctly '{word}'")
                break
    else:
        print("You lost")
        draw_hangman(0)
        print(f"Your word was '{word}'")


def game():
    category = input("Category you would like to play: ")
    category_words = get_single_category(category)
    if check_category(category_words):
        word = random.choice(category_words)
        code_word(word, "print")
        guess = input("Write a letter: ")
        guessing_letters(guess, word)
    else:
        print(f"There is no words in category: {category}\n")


def start():
    if check_all_words(database.words):
        name = input("Hi, write your name: ")
        decision = input(f"{name} do you want to start a game? Press 'y' if yes and other key if no: ").lower()
        while decision == "y":
            game()
            decision = input(f"{name} do you want to start next game? Press 'y' if yes and other key if no: ").lower()
        else:
            print("Returning to the main menu")
    else:
        print("You don't have any words\n")
