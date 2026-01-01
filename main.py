import sys

from stats import letter_count, sorted_letters, word_count


def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = word_count(book_text)
    total_letters = letter_count(book_text)

    print(
        " ============ BOOKBOT ============\n",
        "Analyzing book found at books/frankenstein.txt...\n",
        "----------- Word Count ----------\n",
        f"Found {num_words} total words\n",
        "--------- Character Count -------",
    )
    sorted_letters(total_letters)
    print(
        " ============= END ===============",
    )


main()
