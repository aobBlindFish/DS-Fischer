import random
import TextContent.transform as rt


# Class Definition
class Vocab:
    def __init__(self, targets, replacements):
        # targets: str []
        # replacements: str [][]
        self.targets = targets
        self.replacements = replacements


# Function Definition
def transform_vocab(text, vocab, user_id, intensity=50):
    if vocab.replacements[int(user_id)] != None:
        for single_vocab in vocab.targets:
            str_split = text.split(single_vocab)
            if len(str_split) == 1:
                text = str_split[0]
            else:
                text = ""
                for i in str_split:
                    text = text + i
                    if rt.rng(intensity):
                        if i != str_split[-1]:
                            text = text + random.choice(
                                vocab.replacements[int(user_id)]
                            )
                    else:
                        if i != str_split[-1]:
                            text = text + single_vocab

    return text


# Vocabular
vv_15 = Vocab(
    ["jemand"],
    [
        ["jmd", "someone"],
        None,
        ["jmd"],
        None,
        ["wer"],
        None,
        ["wer"],
        ["jmd"],
        None,
        None,
        None,
    ],
)

# Complete List
vocab_list = [vv_15]
