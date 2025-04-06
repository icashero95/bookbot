import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_count(text)
    char_list = []
    for char, count in char_dict.items():
        new_dict = {"name": char, "num": count}
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_dict)
    print(f"=== Here's a report of {book_path} ===")
    print(f"{num_words} words were found in the document.")
    for i in char_list:
        print(f"The '{i['name']}' character was found {i['num']} times")
    print("=== End of report ===")

def sort_dict(dict):
    return dict["num"]

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





main()