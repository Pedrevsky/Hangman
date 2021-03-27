import database

# words = database.get_all_words()


def print_all_categories():
    categories = []
    for element in database.words:
        categories.append(element[0])

    categories = list(set(categories))
    if len(categories) == 0:
        print("You don't have any categories")
    else:
        _categories = ", ".join(categories)
        print("All categories you can pick are below:\n")
        print(_categories)
        print("\n\n")


def info():
    print("Project 'Hangman' is made by Wojciech Jasiewicz")


def instructions():
    _instruction = """
    1. Pick a category and play
    2. If there is no words in category you will be informed and pushed to the main menu
    3. You can add words to the new categories or to the categories that already exist
    4. You can check categories by typing 'c' in main menu (words won't be shown)
    5. In game you have 6 lives
    6. One miss is one life down
    7. You can resign a game by typing 'EXIT', you will return to main menu
    """

    print(_instruction)


def draw_hangman(tries):
    if tries == 5:
        hangman = """
            
            |
            |
            |
            |
        ____|____
        """
    elif tries == 4:
        hangman = """
            _______
            |     
            |     
            |     
            |
            |
        ____|____
        """
    elif tries == 3:
        hangman = """
            _______
            |     |
            |     O
            |     
            |     
            |
        ____|____
        """
    elif tries == 2:
        hangman = """
            _______
            |     |
            |     O
            |     |
            |     |
            |     
        ____|____
        """
    elif tries == 1:
        hangman = """
            _______
            |     |
            |     O
            |    -|-
            |     |
            |     
        ____|____
        """
    elif tries == 0:
        hangman = """
            _______
            |     |
            |     O
            |    -|-
            |     |
            |     /\\
        ____|____
        """
    else:
        hangman = "Hangman not found"
    print(hangman)
