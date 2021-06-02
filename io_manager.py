import TextContent.res_prewritten as res_pre
import TextContent.res_basic as res_basic


# what msg relates to what prompt
def answer(text, user_id):
    output = "No answer."
    # Check for basic answers
    for prompt in res_basic.response_list:
        if prompt.relate(text):
            output = prompt.answer(int(user_id))

    # Check for prewritten answers
    for prompt in res_pre.response_list:
        if prompt.relate(text):
            output = prompt.answer(int(user_id))

    return output
