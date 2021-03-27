import database
import game
import printing_service


def prompt_add_word():
    choice = "y"
    while choice == "y":
        category = input("Category for which you want to add word: ")
        word = input(f"Word you want to add to {category}: ")
        database.add_word(category, word)
        choice = input("Do you want to add next world? Type 'y' if yes, type anything else if no: ")


def prompt_remove_word():
    choice = "y"
    while choice == "y":
        word = input("Write a word you want to delete: ")
        database.remove_word(word)
        choice = input("Do you want to add next world? Type 'y' if yes, type anything else if no: ")


USER_CHOICE = """
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
    choice = input(USER_CHOICE).lower()
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
            game.game()
        elif choice == "334":
            print(database.get_all_words())
        else:
            print("Unknown choice, please try again")
        choice = input(USER_CHOICE).lower()


menu()
