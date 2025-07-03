from stats import get_word_count, get_word_freq, final_op
import sys

def get_book_text(filepath):
    with open(file=filepath) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    PATH=sys.argv[1]
    content = get_book_text(PATH)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {PATH}")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(content)} total words")
    print("--------- Character Count -------")
    list = final_op(content)
    for item in list:
        print(f"{item['char']}: {item['num']}")

main()