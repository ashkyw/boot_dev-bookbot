from stats import letter_count, sorted_letters, word_count


def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as f:
        file_contents = f.read()
        return file_contents


def main():
    filepath = (
        "/home/kyle/Documents/bootdev_lessons/boot_dev-bookbot/books/frankenstein.txt"
    )
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
