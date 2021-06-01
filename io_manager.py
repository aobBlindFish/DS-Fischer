import TextContent.res_prewritten as res


# what msg relates to what prompt
def answer(text, user_id=2):
    output = "No answer."
    for prompt in res.response_list:
        if prompt.relate(text):
            output = prompt.answer(int(user_id))

    return output
