def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_char_counts(book_text):
    book_text_lower = book_text.lower()
    char_counts = {}

    for char in book_text_lower:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_on(items):
    return items["num"]

def sort_char_counts(char_counts):
    list_of_dicts = []

    for k, v in char_counts.items():
        if k.isalpha():
            new_dict = {"char":k, "num":v}
            list_of_dicts.append(new_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts