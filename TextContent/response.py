import random


# Class Definition
class Response:
    def __init__(self, prompt_list, answer_list):
        # prompt_list -> str []
        # answer_list -> str [][]
        self.prompt_list = prompt_list
        self.answer_list = answer_list

    def answer(self, user_id):
        rand_int = random.randint(0, len(self.answer_list[user_id]) - 1)
        return self.answer_list[user_id][rand_int]

    def relate(self, text):
        output = False
        for prompt in self.prompt_list:
            if prompt.lower() == text.lower():
                output = True

        return output


# Responses

greeting_1 = Response(["Hallo", "Hi"],
                      [["Hallo 1a", "Hallo 1b"], ["Hallo 2"], ["Hallo 3", "Hallo 3ab", "Hallo 3f"], ["Hallo 4"],
                       ["Hallo 5"], ["Hallo 6"], ["Hallo 7"], ["Hallo 8"],
                       ["Hallo 9"], ["Hallo 10"], ["Hallo 11"]])

greeting_2 = Response(
    ["Yo", "Ye"], [["Yo 1"], ["Yo 2"], ["Yo 3"], ["Yo 4"], ["Yo 5"], ["Yo 6"],
                   ["Yo 7"], ["Yo 8"], ["Yo 9"], ["Yo 10"], ["Yo 11"]])

# List of responses
response_list = [greeting_1, greeting_2]
