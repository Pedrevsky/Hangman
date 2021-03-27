words = []


def get_all_words():
    return words


def add_word(category, word):
    words.append([category, word])


def remove_word(delete):
    global words
    words = [element for element in words if element[1] != delete]

