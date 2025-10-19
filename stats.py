def count_words(text):
    return len(text.split())


def character_count(text):
    char_dict = {}
    char_list = text.lower()
    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def sort_on(items):
    return items["num"]


from collections import defaultdict

def sorted_dict(char_dict):
    proper_dict = []
    for char, num in char_dict.items():
        proper_dict.append({"char":char, "num":num})
    proper_dict.sort(reverse=True, key=sort_on)
    return proper_dict