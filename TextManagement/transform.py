import random
import sys
import TextManagement.StringPreset as StrP


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

    # intensity: int/float in range(0, 100)
    # basic case
    if intensity == 0:
        return text

    if intensity < 0:
        intensity = 0
    elif intensity > 100:
        intensity = 100

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

    # intensity: int/float in range(0, 100)
    # basic case
    if intensity == 0:
        return text

    if intensity < 0:
        intensity = 0
    elif intensity > 100:
        intensity = 100

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


def typo(text, intensity):
    if intensity == 0:
        return text

    sentence_chars = [
        ".",
        "!",
        "?",
        ",",
        ";",
        ":",
        "-",
        "_",
        "'",
        '"',
        "*",
        "~",
        "+",
        "#",
    ]
    try:
        text = str(text)
        intensity = float(intensity)
    except ValueError or UnicodeDecodeError:
        return text

    # intensity in range(0, 100)
    if intensity < 0:
        intensity = 0
    elif intensity > 100:
        intensity = 100

    words = text.split(" ")
    output = ""
    for word in words:
        if rng(intensity):
            new_word = ""
            for letter in word:
                if rng(intensity * 0.3) and letter not in sentence_chars:
                    # capitalize
                    if rng(50):
                        letter = letter.upper()
                    else:
                        letter = letter.lower()
                if rng(95) or letter in sentence_chars:  # omission
                    new_word = new_word + letter
            output = output + new_word + " "
        else:
            output = output + word + " "

    return StrP.str_trim(output, -1)


def filler(text, filler_words, intensity=50, word_mode=True):
    # fills in a random assortment of words after random words or sentences

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

    # intensity: int/float in range(0, 100)
    if type(intensity) not in [int, float]:
        sys.exit("Error in filler(): Intensity needs to be a number.")
    if intensity < 0:
        intensity = 0
    elif intensity > 100:
        intensity = 100

    # basic case
    if filler_words == [] or intensity == 0:
        return text

    # normal case
    if not word_mode:
        text = " " + text

    if word_mode:
        splitter = " "
    else:
        splitter = "."

    str_split = text.split(splitter)

    output = ""

    for i in str_split:
        for filler_word in filler_words:
            if rng(intensity):
                if word_mode:
                    i = i + " " + filler_word
                else:
                    i = " " + filler_word + i
        output = output + i + splitter

    if output[:1] == " ":
        output = StrP.str_trim(output, 1)

    return output


# Function Definition
def transform(text, user_id, intensity=50):
    intensity = intensity * 0.02

    if user_id == 0:
        text = capital(text, 5 * intensity)
        text = repetition(text, ["."], 0.1 * intensity)
        text = typo(text, 5 * intensity)

    elif user_id == 1:
        text = decapital(text, 20 * intensity)
        text = repetition(text, ["."], 0.3 * intensity)
        text = typo(text, 5 * intensity)

    elif user_id == 2:
        text = decapital(text, 30 * intensity)
        text = repetition(text, ["?"], 0.3 * intensity)
        text = repetition(text, ["."], 0.1 * intensity)
        text = typo(text, 10 * intensity)
        text = filler(text, ["halt", "so"], 5 * intensity, True)
        text = filler(text, ["Also"], 5 * intensity, False)

    elif user_id == 3:
        text = decapital(text, 20 * intensity)
        text = repetition(text, [","], 0.8 * intensity)
        text = repetition(text, ["."], 0.3 * intensity)
        text = typo(text, 5 * intensity)
        text = filler(text, ["Ja"], 20 * intensity, False)

    elif user_id == 4:
        text = decapital(text, 5 * intensity)
        text = repetition(text, ["."], 0.3 * intensity)
        text = filler(text, ["halt", "so"], 5 * intensity, True)

    elif user_id == 5:
        text = repetition(text, ["."], 0.3 * intensity)
        text = typo(text, 5 * intensity)

    elif user_id == 6:
        text = decapital(text, 30 * intensity)
        text = repetition(text, ["."], 0.3 * intensity)
        text = typo(text, 5 * intensity)

    elif user_id == 7:
        text = decapital(text, 20 * intensity)
        text = repetition(text, [","], 0.6 * intensity)
        text = repetition(text, ["."], 0.3 * intensity)
        text = repetition(text, ["?"], 1.3 * intensity)
        text = typo(text, 5 * intensity)
        text = filler(text, ["so"], 5 * intensity, True)

    elif user_id == 8:
        text = decapital(text, 5 * intensity)
        text = repetition(text, [","], 0.6 * intensity)
        text = repetition(text, ["."], 0.3 * intensity)
        text = typo(text, 5 * intensity)

    elif user_id == 9:
        text = decapital(text, 80 * intensity)
        text = capital(text, 5 * intensity)
        text = repetition(text, ["."], 0.3 * intensity)
        text = typo(text, 20 * intensity)
        text = filler(text, ["halt"], 3 * intensity, True)

    elif user_id == 10:
        text = capital(text, 5 * intensity)
        text = repetition(text, ["."], 0.3 * intensity)
        text = repetition(text, [","], 0.8 * intensity)

    return text
