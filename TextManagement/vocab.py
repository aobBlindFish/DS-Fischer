import random
import TextManagement.transform as rt


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
                                vocab.replacements[int(user_id)])
                    else:
                        if i != str_split[-1]:
                            text = text + single_vocab

    return text


# Vocabular
lb_0 = Vocab(
    [". "],
    [
        [". ", ".\n", ".\n", "\n", "\n", "\n", "\n", "\n", ".\n", ".\n"],
        [". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ".\n"],
    ],
)
lb_1 = Vocab(
    ["? "],
    [
        ["? ", "?\n", "?\n", "\n", "\n", "\n", "\n", "\n", "?\n", "?\n"],
        ["? ", "? ", "? ", "? ", "? ", "? ", "? ", "? ", "? ", "?\n"],
    ],
)
lb_2 = Vocab(
    ["! "],
    [
        ["! ", "!\n", "!\n", "\n", "\n", "\n", "\n", "\n", "!\n", "!\n"],
        ["! ", "! ", "! ", "! ", "! ", "! ", "! ", "! ", "! ", "!\n"],
    ],
)
vv_01 = Vocab(
    [" auf dem ", " Auf dem "],
    [
        None,
        [" aufm "],
    ],
)
vv_03_a = Vocab(
    [" das heißt ", " Das heißt "],
    [
        None,
        [" d.h. "],
    ],
)
vv_03_b = Vocab(
    [" das heißt?", " Das heißt?"],
    [
        None,
        [" d.h.?"],
    ],
)
vv_04_a = Vocab(
    [" dumm ", " Dumm "],
    [
        None,
        [" doof "],
    ],
)
vv_04_b = Vocab(
    [" dumm.", " Dumm."],
    [
        None,
        [" doof."],
    ],
)
vv_04_c = Vocab(
    [" dumm?", " Dumm?"],
    [
        None,
        [" doof?"],
    ],
)
vv_04_d = Vocab(
    [" dumm!", " Dumm!"],
    [
        None,
        [" doof!"],
    ],
)
vv_05 = Vocab(
    [" eigentlich ", " Eigentlich "],
    [
        None,
        [" eig "],
    ],
)
vv_06 = Vocab(
    [" eine ", " Eine "],
    [
        None,
        [" nh "],
    ],
)
vv_10_a = Vocab(
    [" gemein ", " unfreundlich ", " Gemein ", " Unfreundlich "],
    [
        [" dreist ", " mean ", " rude "],
        None,
    ],
)
vv_10_b = Vocab(
    [" gemein.", " unfreundlich.", " Gemein.", " Unfreundlich."],
    [
        [" dreist.", " mean.", " rude."],
        None,
    ],
)
vv_10_c = Vocab(
    [" gemein?", " unfreundlich?", " Gemein?", " Unfreundlich?"],
    [
        [" dreist?", " mean?", " rude?"],
        None,
    ],
)
vv_10_d = Vocab(
    [" gemein!", " unfreundlich!", " Gemein!", " Unfreundlich!"],
    [
        [" dreist!", " mean!", " rude!"],
        None,
    ],
)
vv_11_a = Vocab(
    [" habe ", " haben "],
    [
        None,
        [" hab "],
    ],
)
vv_11_b = Vocab(
    [" habe.", " haben."],
    [
        None,
        [" hab."],
    ],
)
vv_11_c = Vocab(
    [" habe?", " haben?"],
    [
        None,
        [" hab?"],
    ],
)
vv_11_d = Vocab(
    [" habe!", " haben!"],
    [
        None,
        [" hab!"],
    ],
)
vv_13_a = Vocab(
    [" ist denn "],
    [
        None,
        [" isn "],
    ],
)
vv_13_b = Vocab(
    [" ist denn?"],
    [
        None,
        [" isn?"],
    ],
)
vv_14 = Vocab(
    ["ist so."],
    [
        None,
        ["isso."],
    ],
)
vv_15_a = Vocab(
    [" jemand ", " Jemand "],
    [
        [" jmd ", " someone "],
        [" jmd "],
    ],
)
vv_15_b = Vocab(
    [" jemand?", " Jemand?"],
    [
        [" jmd?", " someone?"],
        [" jmd?"],
    ],
)
vv_17 = Vocab(
    [" keine Ahnung ", " Keine Ahnung "],
    [
        None,
        [" ka "],
    ],
)
vv_18_a = Vocab(
    [" langweilig ", " Langweilig "],
    [
        None,
        [" lw "],
    ],
)
vv_18_b = Vocab(
    [" langweilig.", " Langweilig."],
    [
        None,
        [" lw."],
    ],
)
vv_18_c = Vocab(
    [" langweilig?", " Langweilig?"],
    [
        None,
        [" lw?"],
    ],
)
vv_18_d = Vocab(
    [" langweilig!", " Langweilig!"],
    [
        None,
        [" lw!"],
    ],
)
vv_19 = Vocab(
    [" Laptop "],
    [
        None,
        [" Lapi "],
    ],
)
vv_21 = Vocab(
    [" mindestens ", " Mindestens "],
    [
        None,
        [" mind. "],
    ],
)
vv_23_a = Vocab(
    [" okay ", " Okay "],
    [
        None,
        [" ok ", " oke "],
    ],
)
vv_23_b = Vocab(
    [" okay.", " Okay."],
    [
        None,
        [" ok.", " oke."],
    ],
)
vv_23_c = Vocab(
    [" okay?", " Okay?"],
    [
        None,
        [" ok?", " oke?"],
    ],
)
vv_23_d = Vocab(
    [" okay!", " Okay!"],
    [
        None,
        [" ok!", " oke!"],
    ],
)
vv_28_a = Vocab(
    [" ups "],
    [
        [" whoops ", " oops "],
        [" Whoops "],
    ],
)
vv_28_b = Vocab(
    [" ups."],
    [
        [" whoops.", " oops."],
        [" Whoops."],
    ],
)
vv_28_c = Vocab(
    [" ups!"],
    [
        [" whoops!", " oops!"],
        [" Whoops!"],
    ],
)
vv_29 = Vocab(
    [" vielleicht ", " Vielleicht "],
    [
        [" vllt ", " maybe "],
        [" vllt "],
    ],
)
vv_30 = Vocab(
    [" YouTube ", " Youtube ", " youtube "],
    [
        [" yt ", " YT "],
        None,
    ],
)

confirmation_1a = Vocab(
    [" Ja.", " ja."],
    [
        [" yes. ", " richtig. ", " korrekt. ", " sure. ", " ye. "],
        [" jup. "],
    ],
)
confirmation_1b = Vocab(
    [" Ja!", " ja!"],
    [
        [" yes!", " richtig!", " sure!", " ye!"],
        [" jup!"],
    ],
)

confirmation_2a = Vocab(
    [" Nein ", " nein "],
    [
        [" ne "],
        [" nope "],
    ],
)
confirmation_2b = Vocab(
    [" Nein.", " nein."],
    [
        [" ne."],
        [" nope."],
    ],
)
confirmation_2c = Vocab(
    [" Nein?", " nein?"],
    [
        [" ne?"],
        [" nope?"],
    ],
)
confirmation_2d = Vocab(
    [" Nein!", " nein!"],
    [
        [" ne!"],
        [" nope!"],
    ],
)

greeting_1 = Vocab(
    ["Hallo.", "Hallo!"],
    [
        ["Hi.", "Guten Tag.", "Hey.", "Yo."],
        ["Hi.", "Hey."],
    ],
)

# Complete List
vocab_list = [
    lb_0, lb_1, lb_2, vv_01, vv_03_a, vv_03_b, vv_04_a, vv_04_b, vv_04_c, vv_04_d, vv_05, vv_06,
    vv_10_a, vv_10_b, vv_10_c, vv_10_d, vv_11_a, vv_11_b, vv_11_c, vv_11_d, vv_13_a, vv_13_b, vv_14, vv_15_a, vv_15_b, vv_17, vv_18_a, vv_18_b, vv_18_c, vv_18_d,
    vv_19, vv_21, vv_23_a, vv_23_b, vv_23_c, vv_23_d, vv_28_a, vv_28_b, vv_28_c,
    vv_29, vv_30, confirmation_1a, confirmation_1b, confirmation_2a, confirmation_2b, confirmation_2c, confirmation_2d, greeting_1
]
