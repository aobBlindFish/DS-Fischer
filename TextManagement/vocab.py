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
        None,
        [". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ".\n"],
        None,
        [". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ".\n"],
        [". ", ".\n", ".\n", "\n", "\n", "\n", "\n", "\n", ".\n", ".\n"],
        None,
        None,
        None,
        None,
        None,
    ],
)
lb_1 = Vocab(
    ["? "],
    [
        ["? ", "?\n", "?\n", "\n", "\n", "\n", "\n", "\n", "?\n", "?\n"],
        None,
        ["? ", "? ", "? ", "? ", "? ", "? ", "? ", "? ", "? ", "?\n"],
        None,
        ["? ", "? ", "? ", "? ", "? ", "? ", "? ", "? ", "? ", "?\n"],
        ["? ", "?\n", "?\n", "\n", "\n", "\n", "\n", "\n", "?\n", "?\n"],
        None,
        None,
        None,
        None,
        None,
    ],
)
lb_2 = Vocab(
    ["! "],
    [
        ["! ", "!\n", "!\n", "\n", "\n", "\n", "\n", "\n", "!\n", "!\n"],
        None,
        ["! ", "! ", "! ", "! ", "! ", "! ", "! ", "! ", "! ", "!\n"],
        None,
        ["! ", "! ", "! ", "! ", "! ", "! ", "! ", "! ", "! ", "!\n"],
        ["! ", "!\n", "!\n", "\n", "\n", "\n", "\n", "\n", "!\n", "!\n"],
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_01 = Vocab(
    [" auf dem ", " Auf dem "],
    [
        None,
        None,
        [" aufm "],
        None,
        None,
        None,
        None,
        None,
        None,
        [" aufm "],
        None,
    ],
)
vv_02 = Vocab(
    [" darüber ", " Darüber "],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        [" drüber "],
        None,
        None,
        None,
    ],
)
vv_03 = Vocab(
    [" das heißt ", " Das heißt "],
    [
        None,
        None,
        [" d.h. "],
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_04 = Vocab(
    [" dumm ", " Dumm "],
    [
        None,
        None,
        [" doof "],
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_05 = Vocab(
    [" eigentlich ", " Eigentlich "],
    [
        None,
        None,
        [" eig "],
        None,
        None,
        None,
        None,
        [" eig "],
        None,
        None,
        None,
    ],
)
vv_06 = Vocab(
    [" ein ", " eine ", " Ein ", " Eine "],
    [
        None,
        None,
        [" nh "],
        None,
        [" ne "],
        None,
        None,
        [" ne "],
        None,
        [" ne ", " nen "],
        None,
    ],
)
vv_07 = Vocab(
    [" einen ", " Einen "],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        [" ne ", " nen "],
        None,
    ],
)
vv_08 = Vocab(
    [" einzige ", " Einzige "],
    [
        None,
        None,
        None,
        None,
        [" einzigste "],
        None,
        None,
        None,
        None,
        [" einzigste "],
        None,
    ],
)
vv_09 = Vocab(
    [" es ", " das "],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        ["s "],
        None,
        None,
    ],
)
vv_10 = Vocab(
    [" gemein ", " unfreundlich ", " Gemein ", " Unfreundlich "],
    [
        [" dreist ", " mean ", " rude "],
        None,
        None,
        [" doof ", " gemein "],
        None,
        None,
        None,
        [" doof "],
        None,
        None,
        None,
    ],
)
vv_11 = Vocab(
    [" habe ", " haben "],
    [
        None,
        None,
        [" hab "],
        None,
        None,
        None,
        None,
        [" hab "],
        None,
        None,
        None,
    ],
)
vv_12 = Vocab(
    [" irgendwie ", " Irgendwie "],
    [
        None,
        None,
        None,
        None,
        None,
        [" iwie "],
        None,
        [" iwie "],
        None,
        None,
        None,
    ],
)
vv_13 = Vocab(
    [" ist denn "],
    [
        None,
        None,
        [" isn "],
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_14 = Vocab(
    ["ist so."],
    [
        None,
        None,
        ["isso."],
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_15 = Vocab(
    [" jemand ", " Jemand "],
    [
        [" jmd ", " someone "],
        None,
        [" jmd "],
        None,
        [" wer "],
        None,
        [" wer "],
        [" jmd "],
        None,
        None,
        None,
    ],
)
vv_16 = Vocab(
    [" jetzt ", " Jetzt "],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        [" jz "],
        None,
        None,
        None,
    ],
)
vv_17 = Vocab(
    [" keine Ahnung ", " Keine Ahnung "],
    [
        None,
        None,
        [" ka "],
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_18 = Vocab(
    [" langweilig ", " Langweilig "],
    [
        None,
        None,
        [" lw "],
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_19 = Vocab(
    [" Laptop "],
    [
        None,
        None,
        [" Lapi "],
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_20 = Vocab(
    [" Lust "],
    [
        None,
        None,
        None,
        None,
        [" Bock "],
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_21 = Vocab(
    [" mindestens ", " Mindestens "],
    [
        None,
        None,
        [" mind. "],
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_22 = Vocab(
    [" mit drin ", " drin ", " Mit drin ", " Drin "],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        [" drinne "],
        None,
    ],
)
vv_23 = Vocab(
    [" okay ", " Okay "],
    [
        None,
        None,
        [" ok ", " oke "],
        None,
        [" ok "],
        [" ok "],
        None,
        [" ok "],
        None,
        None,
        None,
    ],
)
vv_24 = Vocab(
    [" sowieso ", " Sowieso "],
    [
        None,
        None,
        None,
        None,
        [" eh "],
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_25 = Vocab(
    [" super ", " Super "],
    [
        None,
        None,
        None,
        [" supi "],
        [" schick "],
        None,
        [" supi "],
        None,
        None,
        None,
        None,
    ],
)
vv_26 = Vocab(
    [" toll ", " cool ", " Toll ", " Cool "],
    [
        None,
        None,
        None,
        [" Coll "],
        [" Coll "],
        None,
        None,
        [" Coll "],
        None,
        None,
        None,
    ],
)
vv_27 = Vocab(
    [" und "],
    [
        None,
        None,
        None,
        None,
        [" & "],
        [" & "],
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_28 = Vocab(
    [" ups "],
    [
        [" whoops ", " oops "],
        None,
        [" Whoops "],
        None,
        None,
        None,
        None,
        None,
        None,
        [" upsi "],
        None,
    ],
)
vv_29 = Vocab(
    [" vielleicht ", " Vielleicht "],
    [
        [" vllt ", " maybe "],
        None,
        [" vllt "],
        None,
        [" vlt "],
        None,
        None,
        [" vlt "],
        None,
        None,
        None,
    ],
)
vv_30 = Vocab(
    [" YouTube ", " Youtube ", " youtube "],
    [
        [" yt ", " YT "],
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)

# Complete List
vocab_list = [
    lb_0, lb_1, lb_2, vv_01, vv_02, vv_03, vv_04, vv_05, vv_06, vv_07, vv_08,
    vv_09, vv_10, vv_11, vv_12, vv_13, vv_14, vv_15, vv_16, vv_17, vv_18,
    vv_19, vv_20, vv_21, vv_22, vv_23, vv_24, vv_25, vv_26, vv_27, vv_28,
    vv_29, vv_30
]
