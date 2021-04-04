import random
import database
from printing_service import draw_hangman


def check_all_words(checklist):
    return len(checklist) != 0


def check_category(category_words):
    return len(category_words) != 0


def get_single_category(category):
    return [element[1] for element in database.words if element[0] == category]


def code_word(word):
    undercover_list = []
    for element in word:
        if element == " ":
            undercover_list.append(" ")
        elif element == "-":
            undercover_list.append("-")
        else:
            undercover_list.append("_")
    return undercover_list


def guess_decision(guess, tries):
    return guess != "EXIT" and tries > 1


def add_letter(guess, word, undercover_list):
    i = 0
    for element in word:
        if element.lower() == guess.lower():
            undercover_list[i] = element
        i += 1
    return undercover_list


def incorrect_guess_instruction(guess, undercover, tries, incorrect_guesses):
    if guess.lower() in incorrect_guesses:
        print(f"You already have guessed incorrectly {guess.lower()}")
        print(undercover)
        return False
    else:
        incorrect_guesses.append(guess.lower())
        incorrect_guesses = list(set(incorrect_guesses))
        print(f"Your guess {guess} was incorrect, you have {tries} tries left")
        draw_hangman(tries)
        _incorrect_guesses = ", ".join(incorrect_guesses)
        print(f"Your incorrect guesses: {_incorrect_guesses}\n")
        print(undercover)
        return True


def make_undercover(word, undercover_list):
    for element in word:
        if element == " ":
            undercover_list.append(" ")
        else:
            undercover_list.append("_")
    return "".join(undercover_list)


def check_if_correct_word(word, undercover):
    return word == undercover


def less_tries(tries):
    if incorrect_guess_instruction:
        tries -= 1
    return tries


def guessing_letters(guess, word):
    undercover_list = code_word(word)
    undercover = "".join(undercover_list)
    tries = 6
    incorrect_guesses = []
    while guess_decision(guess, tries):
        if guess in word:
            undercover_list = add_letter(guess, word, undercover_list)
            undercover = "".join(undercover_list)
            if check_if_correct_word(word, undercover):
                break
            else:
                print(undercover)
                guess = input("Write a letter: ")
        else:
            tries = less_tries(tries)
            incorrect_guess_instruction(guess, undercover, tries, incorrect_guesses)
            guess = input("Write a letter: ")
    if guess in word:
        undercover_list = add_letter(guess, word, undercover_list)
        undercover = "".join(undercover_list)
        while True:
            if guess not in word:
                break
            undercover_list = add_letter(guess, word, undercover_list)
            undercover = "".join(undercover_list)
            if check_if_correct_word(word, undercover):
                break
            else:
                print(undercover)
                guess = input("Write a letter: ")


    if check_if_correct_word(word, undercover):
        print(f"You guessed correctly {word}")
    else:
        print("You lost")
        draw_hangman(0)
        print(f"Your word was '{word}'")


def game():
    category = input("Category you would like to play: ")
    category_words = get_single_category(category)
    if check_category(category_words):
        word = random.choice(category_words)
        undercover_list = code_word(word)
        print("".join(undercover_list))
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
