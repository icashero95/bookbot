def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_char_count(text)
    print(f"=== Here's a report of {book_path} ===")
    print(f"{num_words} words were found in the document.")
    

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
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count





main()