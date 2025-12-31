def word_count(book_text):
    words = book_text.split()
    return len(words)


def letter_count(book_text):
    letter_count = {}
    letters = book_text.lower()
    for character in letters:
        if character in letter_count:
            letter_count[character] += 1
        else:
            letter_count[character] = 1

    return letter_count


def sort_dictionary(total_letters):
    pass
