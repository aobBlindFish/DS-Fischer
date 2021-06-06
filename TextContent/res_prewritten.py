import random
import TextContent.transform as rt


# Function Definition
def text_comp(a, b):
    # alter a and b here
    # return
    return a.lower() == b.lower()


# Class Definition
class Response:
    def __init__(self, prompt_list, standart_res, answer_list):
        # prompt_list -> str []
        # standart_res -> str []
        # answer_list -> str [][]
        self.prompt_list = prompt_list
        self.standart_res = standart_res
        self.answer_list = answer_list

    def answer(self, user_id):
        special_res_chance = 50
        vocab_chance = 70
        if rt.rng(special_res_chance):
            # Special Response
            answer = self.answer_list[user_id]
            if answer == None:
                answer = random.choice(self.standart_res)
                answer = rt.transform(answer, user_id)
            else:
                answer = random.choice(answer)
        else:
            # Altered Standart Response
            answer = random.choice(self.standart_res)
            # Insert Vocab here
            answer = rt.transform(answer, user_id)

        return answer

    def relate(self, text):
        output = False
        for prompt in self.prompt_list:
            if text_comp(prompt, text):
                output = True

        return output


# Responses
thanks_1 = Response(
    ["Für dich", "Bitte", "Bitteschön"],
    ["Dankeschön.", "Danke.", "Danke dir!"],
    [["ty"], None, ["thx"], None, None, ["thx"], None, None, None, None, None])

greeting_1 = Response(
    ["Hallo", "Hi"], ["Hallo."],
    [["Hi", "Guten Tag", "Hey", "Yo"], None, ["Hi", "Hey"], ["Hi", "Hey"],
     None, ["Hi", "Hey"], ["Hi", "Hey"], None, None, ["Moinmoin"], None])

disorientation_2 = Response(
    ["lost"], ["Ich weiß nicht.", "Ich habe keine Ahnung."],
    [["idk", "wth", "what", "wdym"], None, ["hä", "dafuq"], None, ["hä"],
     ["ka", "hä"], None, None, None, None, None])

# List of responses
response_list = [greeting_1, thanks_1]
