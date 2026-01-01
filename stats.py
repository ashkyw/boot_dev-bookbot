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


def sorted_letters(letters: dict):
    letters_list = list(letters.items())
    dict_list = []
    for tuples in letters_list:
        if tuples[0].isalpha():
            dict_list.append({"item": tuples[0], "num": tuples[1]})

    sort_list = sorted(dict_list, key=lambda x: x["num"], reverse=True)
    for item in sort_list:
        print(f"{item['item']}: {item['num']}")
