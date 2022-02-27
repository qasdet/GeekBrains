DICT_NUM = {

    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четире",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",

}


def num_translate(num_word):
    """ convert one to один...nine to девять """
    # return DICT_NUM.get(num_word)
    print(DICT_NUM.get(num_word))


def num_translate_adv(num_word):
    """ convert one to один...nine to девять with firt char capitalize """
    to_key = DICT_NUM.get(num_word.lower())

    if to_key:
        return to_key.capitalize() if num_word[0].isupper() else to_key

    return None



num_translate("one")
num_translate_adv("two")