def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words
from stats import get_num_char
from stats import get_char_report_data
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_contents = get_book_text(sys.argv[1])
        num_words = get_num_words(book_contents)
        num_char = get_num_char(book_contents)
        count_dict = get_char_report_data(num_char)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in count_dict:
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")

main()

