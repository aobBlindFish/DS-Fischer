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
vv_03_a = Vocab(
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
vv_03_b = Vocab(
    [" das heißt?", " Das heißt?"],
    [
        None,
        None,
        [" d.h.?"],
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
vv_04_a = Vocab(
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
vv_04_b = Vocab(
    [" dumm.", " Dumm."],
    [
        None,
        None,
        [" doof."],
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
vv_04_c = Vocab(
    [" dumm?", " Dumm?"],
    [
        None,
        None,
        [" doof?"],
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
vv_04_d = Vocab(
    [" dumm!", " Dumm!"],
    [
        None,
        None,
        [" doof!"],
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
    [" eine ", " Eine "],
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
        [" ne "],
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
        [" nen "],
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
vv_10_a = Vocab(
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
vv_10_b = Vocab(
    [" gemein.", " unfreundlich.", " Gemein.", " Unfreundlich."],
    [
        [" dreist.", " mean.", " rude."],
        None,
        None,
        [" doof.", " gemein."],
        None,
        None,
        None,
        [" doof."],
        None,
        None,
        None,
    ],
)
vv_10_c = Vocab(
    [" gemein?", " unfreundlich?", " Gemein?", " Unfreundlich?"],
    [
        [" dreist?", " mean?", " rude?"],
        None,
        None,
        [" doof?", " gemein?"],
        None,
        None,
        None,
        [" doof?"],
        None,
        None,
        None,
    ],
)
vv_10_d = Vocab(
    [" gemein!", " unfreundlich!", " Gemein!", " Unfreundlich!"],
    [
        [" dreist!", " mean!", " rude!"],
        None,
        None,
        [" doof!", " gemein!"],
        None,
        None,
        None,
        [" doof!"],
        None,
        None,
        None,
    ],
)
vv_11_a = Vocab(
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
vv_11_b = Vocab(
    [" habe.", " haben."],
    [
        None,
        None,
        [" hab."],
        None,
        None,
        None,
        None,
        [" hab."],
        None,
        None,
        None,
    ],
)
vv_11_c = Vocab(
    [" habe?", " haben?"],
    [
        None,
        None,
        [" hab?"],
        None,
        None,
        None,
        None,
        [" hab?"],
        None,
        None,
        None,
    ],
)
vv_11_d = Vocab(
    [" habe!", " haben!"],
    [
        None,
        None,
        [" hab!"],
        None,
        None,
        None,
        None,
        [" hab!"],
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
vv_13_a = Vocab(
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
vv_13_b = Vocab(
    [" ist denn?"],
    [
        None,
        None,
        [" isn?"],
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
vv_15_a = Vocab(
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
vv_15_b = Vocab(
    [" jemand?", " Jemand?"],
    [
        [" jmd?", " someone?"],
        None,
        [" jmd?"],
        None,
        [" wer?"],
        None,
        [" wer?"],
        [" jmd?"],
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
vv_18_a = Vocab(
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
vv_18_b = Vocab(
    [" langweilig.", " Langweilig."],
    [
        None,
        None,
        [" lw."],
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
vv_18_c = Vocab(
    [" langweilig?", " Langweilig?"],
    [
        None,
        None,
        [" lw?"],
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
vv_18_d = Vocab(
    [" langweilig!", " Langweilig!"],
    [
        None,
        None,
        [" lw!"],
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
vv_20_aa = Vocab(
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
vv_20_ba = Vocab(
    [" Lust."],
    [
        None,
        None,
        None,
        None,
        [" Bock."],
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_20_ca = Vocab(
    [" Lust?"],
    [
        None,
        None,
        None,
        None,
        [" Bock?"],
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_20_da = Vocab(
    [" Lust!"],
    [
        None,
        None,
        None,
        None,
        [" Bock!"],
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_20_ab = Vocab(
    ["keine Lust "],
    [
        None,
        None,
        None,
        None,
        ["keinen Bock "],
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_20_bb = Vocab(
    ["keine Lust."],
    [
        None,
        None,
        None,
        None,
        ["keinen Bock."],
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_20_cb = Vocab(
    ["keine Lust?"],
    [
        None,
        None,
        None,
        None,
        ["keinen Bock?"],
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_20_db = Vocab(
    ["keine Lust!"],
    [
        None,
        None,
        None,
        None,
        ["keinen Bock!"],
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
vv_22_a = Vocab(
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
vv_22_b = Vocab(
    [" mit drin.", " drin.", " Mit drin.", " Drin."],
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
        [" drinne."],
        None,
    ],
)
vv_22_c = Vocab(
    [" mit drin?", " drin?", " Mit drin?", " Drin?"],
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
        [" drinne?"],
        None,
    ],
)
vv_22_d = Vocab(
    [" mit drin!", " drin!", " Mit drin!", " Drin!"],
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
        [" drinne!"],
        None,
    ],
)
vv_23_a = Vocab(
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
vv_23_b = Vocab(
    [" okay.", " Okay."],
    [
        None,
        None,
        [" ok.", " oke."],
        None,
        [" ok."],
        [" ok."],
        None,
        [" ok."],
        None,
        None,
        None,
    ],
)
vv_23_c = Vocab(
    [" okay?", " Okay?"],
    [
        None,
        None,
        [" ok?", " oke?"],
        None,
        [" ok?"],
        [" ok?"],
        None,
        [" ok?"],
        None,
        None,
        None,
    ],
)
vv_23_d = Vocab(
    [" okay!", " Okay!"],
    [
        None,
        None,
        [" ok!", " oke!"],
        None,
        [" ok!"],
        [" ok!"],
        None,
        [" ok!"],
        None,
        None,
        None,
    ],
)
vv_24_a = Vocab(
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
vv_24_b = Vocab(
    [" sowieso.", " Sowieso."],
    [
        None,
        None,
        None,
        None,
        [" eh."],
        None,
        None,
        None,
        None,
        None,
        None,
    ],
)
vv_25_a = Vocab(
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
vv_25_b = Vocab(
    [" super.", " Super."],
    [
        None,
        None,
        None,
        [" supi."],
        [" schick."],
        None,
        [" supi."],
        None,
        None,
        None,
        None,
    ],
)
vv_25_c = Vocab(
    [" super!", " Super!"],
    [
        None,
        None,
        None,
        [" supi!"],
        [" schick!"],
        None,
        [" supi!"],
        None,
        None,
        None,
        None,
    ],
)
vv_26_a = Vocab(
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
vv_26_b = Vocab(
    [" toll.", " cool.", " Toll.", " Cool."],
    [
        None,
        None,
        None,
        [" Coll."],
        [" Coll."],
        None,
        None,
        [" Coll."],
        None,
        None,
        None,
    ],
)
vv_26_c = Vocab(
    [" toll?", " cool?", " Toll?", " Cool?"],
    [
        None,
        None,
        None,
        [" Coll?"],
        [" Coll?"],
        None,
        None,
        [" Coll?"],
        None,
        None,
        None,
    ],
)
vv_26_d = Vocab(
    [" toll!", " cool!", " Toll!", " Cool!"],
    [
        None,
        None,
        None,
        [" Coll!"],
        [" Coll!"],
        None,
        None,
        [" Coll!"],
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
vv_28_a = Vocab(
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
vv_28_b = Vocab(
    [" ups."],
    [
        [" whoops.", " oops."],
        None,
        [" Whoops."],
        None,
        None,
        None,
        None,
        None,
        None,
        [" upsi."],
        None,
    ],
)
vv_28_c = Vocab(
    [" ups!"],
    [
        [" whoops!", " oops!"],
        None,
        [" Whoops!"],
        None,
        None,
        None,
        None,
        None,
        None,
        [" upsi!"],
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

confirmation_1a = Vocab(
    [" Ja.", " ja."],
    [
        [" yes. ", " richtig. ", " korrekt. ", " sure. ", " ye. "],
        None,
        [" jup. "],
        None,
        None,
        [" jap. "],
        [" jup. "],
        [" jap. ", " yes. "],
        None,
        None,
        None,
    ],
)
confirmation_1b = Vocab(
    [" Ja!", " ja!"],
    [
        [" yes!", " richtig!", " sure!", " ye!"],
        None,
        [" jup!"],
        None,
        None,
        [" jap!"],
        [" jup!"],
        [" jap!", " yes!"],
        None,
        None,
        None,
    ],
)

confirmation_2a = Vocab(
    [" Nein ", " nein "],
    [
        [" ne "],
        None,
        [" nope "],
        [" ne "],
        [" nö ", " nene "],
        [" ne "],
        [" nope "],
        None,
        None,
        None,
        None,
    ],
)
confirmation_2b = Vocab(
    [" Nein.", " nein."],
    [
        [" ne."],
        None,
        [" nope."],
        [" ne."],
        [" nö.", " nene."],
        [" ne."],
        [" nope."],
        None,
        None,
        None,
        None,
    ],
)
confirmation_2c = Vocab(
    [" Nein?", " nein?"],
    [
        [" ne?"],
        None,
        [" nope?"],
        [" ne?"],
        [" nö?", " nene?"],
        [" ne?"],
        [" nope?"],
        None,
        None,
        None,
        None,
    ],
)
confirmation_2d = Vocab(
    [" Nein!", " nein!"],
    [
        [" ne!"],
        None,
        [" nope!"],
        [" ne!"],
        [" nö!", " nene!"],
        [" ne!"],
        [" nope!"],
        None,
        None,
        None,
        None,
    ],
)

greeting_1 = Vocab(
    ["Hallo.", "Hallo!"],
    [
        ["Hi.", "Guten Tag.", "Hey.", "Yo."],
        None,
        ["Hi.", "Hey."],
        ["Hi.", "Hey."],
        None,
        ["Hi.", "Hey."],
        ["Hi.", "Hey."],
        None,
        None,
        ["Moinmoin!", "Moinmoin."],
        None,
    ],
)

# Complete List
vocab_list = [
    lb_0, lb_1, lb_2, vv_01, vv_02, vv_03_a, vv_03_b, vv_04_a, vv_04_b, vv_04_c, vv_04_d, vv_05, vv_06, vv_07, vv_08,
    vv_09, vv_10_a, vv_10_b, vv_10_c, vv_10_d, vv_11_a, vv_11_b, vv_11_c, vv_11_d, vv_12, vv_13_a, vv_13_b, vv_14, vv_15_a, vv_15_b, vv_16, vv_17, vv_18_a, vv_18_b, vv_18_c, vv_18_d,
    vv_19, vv_20_aa, vv_20_ba, vv_20_ca, vv_20_da, vv_20_ab, vv_20_bb, vv_20_cb, vv_20_db, vv_21, vv_22_a, vv_22_b, vv_22_c, vv_22_d, vv_23_a, vv_23_b, vv_23_c, vv_23_d, vv_24_a, vv_24_b, vv_25_a, vv_25_b, vv_25_c, vv_26_a, vv_26_b, vv_26_c, vv_26_d, vv_27, vv_28_a, vv_28_b, vv_28_c,
    vv_29, vv_30, confirmation_1a, confirmation_1b, confirmation_2a, confirmation_2b, confirmation_2c, confirmation_2d, greeting_1
]
