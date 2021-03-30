import database
import printing_service
from game import start


def prompt_add_word():
    choice = "y"
    while choice == "y":
        category = input("Category for which you want to add word: ")
        word = input(f"Word you want to add to {category}: ")
        database.add_word(category, word)
        choice = input("Do you want to add next word? Type 'y' if yes, type anything else if no: ")


def prompt_remove_word():
    choice = "y"
    while choice == "y":
        word = input("Write a word you want to delete: ")
        database.remove_word(word)
        choice = input("Do you want to add next word? Type 'y' if yes, type anything else if no: ")


user_choice = """
Welcome to the hangman game!

-g) to see information about the game
-i) to view instructions
-a) to add a word 
-r) to remove word
-c) to check all categories
-p) to play
-q) to quit

What is your choice? Write here: """


def menu():
    #database.create_word_file()
    choice = input(user_choice).lower()
    while choice != "q":
        if choice == "g":
            printing_service.info()
        elif choice == "i":
            printing_service.instructions()
        elif choice == "a":
            prompt_add_word()
        elif choice == "r":
            prompt_remove_word()
        elif choice == "c":
            printing_service.print_all_categories()
        elif choice == "p":
            start()
        elif choice == "334":
            # This in undercover option to check for all elements
            print(database.get_all_words())
        else:
            print("Unknown choice, please try again")
        choice = input(user_choice).lower()


menu()
