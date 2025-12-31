from stats import letter_count, word_count


def main():
    filepath = (
        "/home/kyle/Documents/bootdev_lessons/boot_dev-bookbot/books/frankenstein.txt"
    )
    book_text = get_book_text(filepath)
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")
    total_letters = letter_count(book_text)
    print(total_letters)


def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_contents = f.read()
        return file_contents


main()
