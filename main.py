import sys
from stats import get_num_words
from stats import get_char_counts
from stats import sort_on
from stats import sort_char_counts

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)
    sorted_char_counts = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for dict in sorted_char_counts:
        char = dict["char"]
        num = dict["num"]
        print(f"{char}: {num}")

def get_book_text(file_path):
    with open(file_path) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

main()