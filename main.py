import sys

from stats import character_count, get_num_words, sorted_character_count


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def structure_report(book_path, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit

    book_path = sys.argv[1]  # books/frankenstein.txt
    book = get_book_text(book_path)
    wc = get_num_words(book)
    char_count = sorted_character_count(character_count(book))

    structure_report(book_path=book_path, word_count=wc, char_count=char_count)


main()
