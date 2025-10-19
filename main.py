import sys
from stats import count_words, character_count, sorted_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_count = character_count(text)
    print("--------- Character Count -------")
    list_dict = sorted_dict(char_count)
    for item in list_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    return


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()