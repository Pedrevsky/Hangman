words_file = "words.txt"


def create_word_file():
    with open(words_file, 'w'):
        pass  # creating file if there is no file


def get_all_words():
    with open(words_file, 'r') as file:
        return [line.strip().split(',') for line in file.readlines()]


def add_word(category, word):
    with open(words_file, 'a') as file:
        file.write(f'{category},{word}\n')


def _save_all_words(words):
    with open(words_file, 'w') as file:
        for word in words:
            file.write(f'{word[0]},{word[1]}\n')


def remove_word(delete):
    words = get_all_words()
    words = [word for word in words if word[1] != delete]
    _save_all_words(words)


words = get_all_words()
