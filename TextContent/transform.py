import random
import sys


# Helper Function Definition
def rng(number):
    # number: int, float in range(0, 100)
    if type(number) not in [int, float]:
        sys.exit("Error in rng(): Number needs to be a number(bruh).")
    elif number < 0 or number > 100:
        sys.exit("Error in rng(): Number out of range.")

    # basic case
    if number == 100:
        return True
    elif number == 0:
        return False
    # normal case
    else:
        return random.randint(0, 100) < number


def decapital(text, intensity=50):
    # decapitalizes all letters in random words

    # text: str
    if type(text) != str:
        sys.exit("Error in decapital(): Text needs to be a String.")
    elif len(text) == 0:
        sys.exit("Error in decapital(): Text needs to have content.")

    # intensity: int in range(0, 100)
    # basic case
    if intensity == 0:
        return text

    # normal case
    str_split = text.split(" ")
    output = ""
    for word in str_split:
        if rng(intensity):
            word = word.lower()
        output = output + word + " "
    return output


def capital(text, intensity=50):
    # capitalizes the first letter in random words

    # text: str
    if type(text) != str:
        sys.exit("Error in capital(): Text needs to be a String.")
    elif len(text) == 0:
        sys.exit("Error in capital(): Text needs to have content.")

    # intensity: int in range(0, 100)
    # basic case
    if intensity == 0:
        return text

    # normal case
    str_split = text.split(" ")
    output = ""
    for word in str_split:
        if rng(intensity):
            i = 0
            new_word = ""
            for letter in word:
                if i == 0:
                    letter = letter.upper()
                new_word = new_word + letter
                i += 1
            word = new_word
        output = output + word + " "
    return output


def repetition(text, symbols, factor=1):
    # multiplies the amount of symbols of the specified type by the factor(on average)

    # text: str
    if type(text) != str:
        sys.exit("Error in repetition(): Text needs to be a String.")
    elif len(text) == 0:
        sys.exit("Error in repetition(): Text needs to have content.")

    # symbol: char []
    if type(symbols) != list:
        sys.exit("Error in repetition(): Symbols need to be in a list.")
    for symbol in symbols:
        try:
            str(symbol)
            if len(symbol) != 1:
                sys.exit(
                    "Error in repetition(): Symbols need to be single characters."
                )
        except UnicodeDecodeError:
            sys.exit("Error in repetition(): Symbols need to be writable.")

    # factor: int, float
    if type(factor) not in [int, float]:
        sys.exit("Error in repetition(): Factor needs to be a number.")
    factor = abs(factor)

    # basic case
    if symbols == [] or factor == 1:
        return text

    # adjust factor for rng()
    multiplier = 1
    while factor > 1:
        factor -= 1
        multiplier += 1

    output = ""
    for letter in text:
        if letter in symbols:
            # repetition with multiplier
            for i in range(multiplier - 1):
                output = output + letter
            # rng()
            if rng(100 * factor):
                output = output + letter
        else:
            output = output + letter

    return output


def filler(text, filler_words, intensity=50):
    # fills in a random assortment of words after random words

    # text: str
    if type(text) != str:
        sys.exit("Error in filler(): Text needs to be a String.")
    elif len(text) == 0:
        sys.exit("Error in filler(): Text needs to have content.")

    # filler_words: str []
    if type(filler_words) != list:
        sys.exit("Error in filler(): Filler words need to be in a list.")
    for filler_word in filler_words:
        try:
            str(filler_word)
            if len(filler_word) < 1:
                sys.exit(
                    "Error in filler(): Filler words need to be writable.")
        except UnicodeDecodeError:
            sys.exit("Error in filler(): Filler words need to be writable.")

    # intensity: int in range(0, 100)
    # basic case
    if filler_words == [] or intensity == 0:
        return text

    # normal case
    str_split = text.split(" ")
    output = ""
    for word in str_split:
        for filler_word in filler_words:
            if rng(intensity):
                word = word + " " + filler_word
        output = output + word + " "
    return output


# Function Definition
def transform(text, user_id):
    return text + " von " + str(user_id)
