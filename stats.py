
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(words):
    letters = words.lower()
    char_count = {}
    for letter in letters:
        if letter in char_count and letter.isalpha():
            char_count[letter] += 1
        elif letter not in char_count and letter.isalpha():
            char_count[letter] = 1
    return char_count

def sort_dict(dict):
    return dict["num"]