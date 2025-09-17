import sys
from stats import count_words, count_chars, sort_count_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_Report(text):
    num_words = count_words(text)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {len(num_words)} total words")

    print("--------- Character Count -------")
    dic = count_chars(text)
    for c, val in sort_count_chars(dic).items():
        if c.isalpha():
            print(f"{c}: {val}")



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])

    print_Report(text)

main()