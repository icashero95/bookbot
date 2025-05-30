import sys
from stats import get_num_words, get_book_text, get_char_count, sort_dict

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
        print(f"{i['name']}: {i['num']}")
    print("=== End of report ===")


main()