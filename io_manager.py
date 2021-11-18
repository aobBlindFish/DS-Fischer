import TextManagement.transform as trend
import TextManagement.vocab as vocab
import TextManagement.StringPreset as StrP

IDs = [
    "Blind Fish#9878", "Dilara#1623"
]


# Transition Function
def transition(text, user_id, intensity=100):
    try:
        if int(user_id) < 0 or int(user_id) > 10:
            return text

        if int(intensity) < 0 or int(intensity) > 100:
            return text
    except ValueError:
        return text

    intensity = int(intensity)
    user_id = int(user_id)
    text = str(text)
    for i in vocab.vocab_list:
        text = vocab.transform_vocab(text, i, user_id, intensity)
    text = trend.transform(text, user_id)

    # Clean Up
    if text[-2:] == " .":
        text = StrP.str_trim(text, -2)
    return text
