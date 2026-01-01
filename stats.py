def word_count(book_text: str) -> int:
    words = book_text.split()
    return len(words)


def letter_count(book_text: str) -> dict:
    letter_count = {}
    letters = book_text.lower()
    for character in letters:
        if character in letter_count:
            letter_count[character] += 1
        else:
            letter_count[character] = 1

    return letter_count


def sort_dictionary(letters: dict) -> list:
    # return as e: num
    # return greatest count -> least count
    # use isalpha()
    letter_list = []
    for letters["character"] in letters:
        letter_list.append(
            letters["character"].sort(reverse=True, key=letters["character"].islapha())
            # key=lambda letter: letter["character"]
        )
    print(letter_list)
