# Class Definition
class Convo:
    def __init__(self, title, lines):
        # title: str
        # lines: str,int [][]
        self.title = title
        self.lines = lines
        self.amount = self.count()

    def count(self):
        count = 0
        for line in self.lines:
            if line[1] > count:
                count = line[1]

        return count


# Convos
'''
sg: slowgerman.com
'''
sg_01 = Convo("Im Café", [
    ["Hallo!", 1], ["Hallo!", 2], ["Wie geht es dir?", 1],
    [
        "Ach, ganz gut. Ich habe Halsschmerzen. Hoffentlich werde ich nicht krank.",
        2
    ],
    [
        "Oh, das tut mir leid. Na dann gute Besserung. Setz Dich doch erstmal.",
        1
    ], ["Danke. Bist Du schon lange hier?", 2],
    [
        "Nein, eben erst gekommen. Habe zum Glück gleich einen Parkplatz gefunden.",
        1
    ], ["Glück gehabt. Hast Du schon bestellt?", 2],
    ["Nein, die Kellnerin ist noch nicht aufgetaucht.", 1],
    ["Okay. Und, was gibt es Neues?", 2],
    ["Nicht viel. Aber ich war im Kino. Vorgestern.", 1],
    ["Was hast Du Dir angeschaut?", 2], ["Den Neuen von Marvel.", 1],
    ["Von denen habe ich noch gar nichts gehört.", 2],
    ["Solltest Du Dir anschauen! Ist wirklich ein schöner Film.", 1],
    [
        "Danke für den Tipp! Ich muss aber erst noch mein Buch zu Ende lesen, das ist gerade so spannend, dass ich gar keine Lust habe, etwas anderes zu machen.",
        2
    ], ["Wirklich? Das klingt gut! Kenne ich den Autor?", 1],
    [
        "Glaube ich nicht. Das ist ein ganz unbekannter japanischer Schriftsteller.",
        2
    ], ["Und wie bist Du auf das Buch gekommen?", 1],
    ["Das hat mir eine Kollegin empfohlen.", 2],
    [
        "Praktisch, wenn man solche Kolleginnen hat. Wie ist es bei Dir gerade in der Arbeit?",
        1
    ],
    [
        "Eigentlich ziemlich ruhig. Nicht viel los. Der Chef ist im Urlaub, und wir können mehr oder weniger machen, was wir wollen.",
        2
    ], ["Soso.", 1],
    [
        "Ganz so ist es natürlich nicht. Ich mache schon die wichtigsten Sachen. Aber ich lasse mich nicht stressen.",
        2
    ],
    [
        "Da hast du Recht. Sollen wir mal was bestellen? Da hinten ist die Kellnerin.",
        1
    ], ["Ja, klar. Wink ihr mal.", 2], ["Entschuldigung? Guten Tag!", 1],
    ["Guten Tag. Was darf es denn bei ihnen sein?", 3],
    [
        "Wir hätten gerne zwei Kännchen Milchkaffee, bitte. Und ich hätte gerne ein Stück Himbeerkuchen dazu.",
        1
    ], ["Oh ja, ich auch bitte.", 2],
    [
        "Zwei mal Milchkaffee und zwei Stück Himbeerkuchen. Ich bin damit gleich bei ihnen.",
        3
    ], ["Dankeschön!", 2],
    [
        "Warst Du eigentlich schonmal in diesem neuen Café da vorne an der Ecke?",
        1
    ], ["Nein, ist da ein neues Café? Ist mir gar nicht aufgefallen.", 2],
    ["Doch, das hat erst vor ein paar Wochen aufgemacht.", 1],
    ["Lohnt es sich?", 2],
    [
        "Ich finde schon, die haben selbstgebackene Kuchen und die Bedienung war wirklich sehr freundlich, als ich dort war.",
        1
    ], ["Klingt gut. Wir können uns ja nächstes Mal dort treffen.", 2],
    ["Warum nicht?", 1]
])

sg_02 = Convo("Das Wetter", [
    ["Das ist ja mal wieder typisches Aprilwetter!", 1],
    ["Wieso, was meinst Du?", 2],
    [
        "Gestern habe ich gefroren, obwohl ich einen dicken Pullover anhatte. Und heute schwitze ich.",
        1
    ], ["Du hast ja auch eine Winterjacke an! Zieh sie doch einfach aus.", 2],
    ["Hast ja recht. Aber mich nervt dieses Wetter trotzdem.", 1],
    [
        "Warum? Ärgere Dich doch nicht über Dinge, die man nicht ändern kann.",
        2
    ], ["Ich könnte es ändern. Ich könnte nach Kalifornien ziehen.", 1],
    [
        "Aber das wäre doch langweilig. Immer nur schönes Wetter ist langweilig.",
        2
    ], ["Stimmt. Ich glaube ich würde den Winter vermissen.", 1],
    ["Schnee ist schon was Schönes, oder?", 2],
    [
        "Absolut! Aber diesen Winter hat es hier nur zwei Mal geschneit. So etwas habe ich noch nie erlebt.",
        1
    ], ["Oh, schau mal, jetzt regnet es wieder.", 2],
    [
        "Ich sag doch: Aprilwetter! Ist aber irgendwie ganz gemütlich. Zum Glück sind wir hier drin und müssen nicht raus.",
        1
    ],
    ["Vielleicht sehen wir ja noch einen Regenbogen, das wäre doch super!", 2],
    ["Ich hab schon lange keinen Regenbogen mehr gesehen.", 1],
    [
        "Unsere Chancen stehen nicht schlecht. Da hinten reißt die Wolkendecke auf.",
        2
    ], ["Ja, die Sonne scheint wieder! Aber kein Regenbogen in Sicht.", 1],
    [
        "Ich glaube diese Regenlücke sollten wir nutzen und schnell rüberlaufen in das Café an der Ecke. Was meinst Du?",
        2
    ],
    [
        "Alles klar. Und dann kaufe ich mir noch schnell bei der Drogerie einen Regenschirm, ich glaube das ist eine gute Investition.",
        1
    ],
    [
        "Wenn das so weitergeht in den nächsten Tagen auf jeden Fall. Hast Du den Wetterbericht gehört?",
        2
    ],
    [
        "Ich hab ihn sogar gesehen! Es kam im Fernsehen. Angeblich steigen die Temperaturen die nächsten Tage über und es wird wieder schöner.",
        1
    ],
    [
        "Das klingt doch gut. Dann spar Dir die paar Euro für den Regenschirm lieber und wir essen von dem Geld ein Eis, wenn es wärmer wird.",
        2
    ], ["Abgemacht! Jetzt aber los.", 1]
])

sg_03 = Convo("Im Supermarkt", [
    ["Entschuldigung, wo sind denn hier die Tomaten?", 1],
    ["Da vorne, in der Gemüseabteilung.", 2],
    ["Da habe ich schon nachgeschaut, aber ich habe sie nicht gesehen.", 1],
    ["Doch, sie sind vorne links, gleich am Eingang.", 2],
    [
        "Danke, ich gehe nochmal nachsehen. Ist denn momentan irgendwas im Angebot?",
        1
    ], ["Wir haben frischen Spargel, da kostet das Kilo nur 5 Euro.", 2],
    [
        "Oh, das klingt gut. Ist der Spargel denn aus Deutschland oder wurde er importiert?",
        1
    ], ["Das ist deutscher Spargel. Bayerischer, um genau zu sein.", 2],
    ["Schön, da nehme ich ein Kilo mit. Oder besser gleich zwei.", 1],
    ["Sie haben wohl Hunger?", 2],
    [
        "Und wie! Ich weiß, man sollte nicht hungrig einkaufen gehen, sonst kauft man noch mehr ein als man braucht.",
        1
    ], ["Tja, mich würde es freuen. Kann ich Ihnen noch etwas anbieten?", 2],
    ["Zum Spargel bräuchte ich noch Kartoffeln.", 1],
    [
        "Die sind dort drüben, neben den Zwiebeln. Wir haben ganz junge, zarte Kartoffeln, die muss man nicht schälen.",
        2
    ],
    [
        "Gut, dann ist der Abend also gerettet. Spargel mit Kartoffeln. Schinken hole ich noch hinten an der Fleischtheke. Und ein bisschen Butter als Sauce habe ich noch daheim.",
        1
    ], ["Wie sieht es mit einer Nachspeise dazu aus?", 2],
    ["Nachspeise? Was passt denn zu Spargel?", 1],
    [
        "Natürlich der Klassiker: Erdbeeren. Frische Erdbeeren. Mit etwas Vanilleeis vielleicht.",
        2
    ],
    [
        "Oh ja! Gute Idee. Und dann bräuchte ich noch etwas Weißwein zum Spargel. Ich habe sonst nur Leitungswasser daheim.",
        1
    ], ["Stimmt, habe ich vergessen zu fragen. Sonst noch einen Wunsch?", 2
        ], ["Naja, ich weiß nicht wie ich das jetzt sagen soll.", 1],
    ["Was denn?", 2],
    [
        "Ich hab ehrlich gesagt gar keine Lust, das schöne Essen alleine zu essen. Haben Sie nicht Lust, mitzuessen?",
        1
    ], ["Na da sag ich nicht nein. Sehr gerne!", 2],
    [
        "Dann bis später – sagen wir um 8? Ich schreib Ihnen meine Adresse auf.",
        1
    ], ["Super. Bis dann!", 2], ["Tschüss!", 1]
])

sg_05 = Convo("Die Familie", [
    ["Hallo.", 1], ["Hallo!", 2],
    ["Ich hab letzte Woche Deine Schwester getroffen. Sie sah gut aus!", 1],
    [
        "Ja, sie hat mir davon erzählt. Sie hat Dich erst gar nicht erkannt, weil Du jetzt kurze Haare hast.",
        2
    ],
    [
        "Wirklich? Das habe ich gar nicht gemerkt. Also, dass sie mich nicht erkannt hat. Dass meine Haare kurz sind, habe ich schon gemerkt.",
        1
    ], ["Scherzkeks.", 2], ["Wie war Euer Weihnachten?", 1],
    [
        "Schön! Erst waren wir bei meinen Eltern zu Besuch, und am zweiten Weihnachtsfeiertag dann bei den Schwiegereltern. Mein Schwager war leider krank, er konnte nicht kommen.",
        2
    ],
    [
        "Aber sonst waren alle da. Sogar meine Nichte und mein Neffe – sie studieren im Ausland und sind extra nach Hause gekommen über die Feiertage.",
        2
    ], ["Und wie war’s bei Dir?", 2],
    [
        "Sehr entspannt eigentlich. Meine Cousine hat mit uns gefeiert, also die Tochter meiner Tante aus Hamburg. Sie versteht sich nicht mit ihrem neuen Stiefvater und ist lieber zu uns gekommen.",
        1
    ], ["Verständlich.", 2],
    [
        "Am ersten Weihnachtsfeiertag haben wir dann noch meine Großeltern besucht. Meine Oma und mein Opa wohnen in einem Altersheim, leider ziemlich weit weg von hier. Sonst würde ich sie öfter besuchen.",
        1
    ],
    [
        "Das ist wirklich schade. Bekommen sie denn insgesamt nur selten Besuch?",
        2
    ],
    [
        "Nein, zum Glück wohnt ja mein Onkel in der Nähe, und mein Cousin arbeitet auch im gleichen Ort.",
        1
    ],
    [
        "Na dann ist es ja gut. Du, ich muss jetzt weiter – wir sehen uns sicher bald mal wieder, oder?",
        2
    ], ["Ja. Schönen Tag noch!", 1], ["Tschüss!", 2]
])

# Convo list
convo_list = [sg_01, sg_02, sg_03, sg_05]
