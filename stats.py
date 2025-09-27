def get_num_words(text):
    """Returns the number of times a word appears in the text."""
    return len(text.split())


def character_count(text):
    """Returns the number of times a character appears in the text as a dictonary. Including symbols and spaces.
    Example: {'a': 10, 'b': 5, ...}
    """
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(items):
    return items["num"]


def sorted_character_count(char_dict):
    """Takes a dictionary of characters and their counts and returns a sorted list of dictionaries."""
    listed_characters = []
    for item in char_dict:
        listed_characters.append({"char": item, "num": char_dict[item]})
    listed_characters.sort(reverse=True, key=sort_on)
    return listed_characters
