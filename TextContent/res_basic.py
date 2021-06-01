import random


# Class Definition
class Response:
    def __init__(self, prompt_list, answer_list):
        # prompt_list -> str []
        # answer_list -> str []
        self.prompt_list = prompt_list
        self.answer_list = answer_list

    def relate(self, text):
        output = False
        for prompt in self.prompt_list:
            if prompt.lower() == text.lower():
                output = True

        return output


# Function Definition
def decapital(text, intensity=50):
    # decapitalizes all letters in random words

    # text: str
    # intensity: int in range(0, 100)
    str_split = text.split(" ")
    output = ""
    for word in str_split:
        rnd_float = random.randint(0, 100)
        if rnd_float >= 100 - intensity:
            word = word.lower()
        output = output + word + " "
    return output


def capital(text, intensity=50):
    # capitalizes the first letter in random words

    # text: str
    # intensity: int in range(0, 100)
    str_split = text.split(" ")
    output = ""
    for word in str_split:
        rnd_float = random.randint(0, 100)
        if rnd_float >= 100 - intensity:
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
