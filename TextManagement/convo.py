# Class Definition
class Convo:
    def __init__(self, title, lines, additions):
        # title: str
        # lines: str,int [][]
        # additions: str,int [][]
        # additions: [[line, position, ID, add_ons]]
        self.title = title
        self.lines = lines
        self.additions = additions
        self.affected = self.check_affected()
        self.amount = self.count()

    # Counts amount of users talking/mentioned
    def count(self):
        count = 0
        for line in self.lines:
            if line[1] > count:
                count = line[1]

        extra = 0
        for change in self.additions:
            if change[2] > extra:
                extra = change[2]

        return count, extra

    # Counts amount of lines to be changed
    def check_affected(self):
        output = []
        if len(self.additions) == 0:
            return output

        for change in self.additions:
            output.append(change[0])

        return output


# Convos
'''
sg: slowgerman.com
'''
sg_01 = Convo("Im Café", [
    ["Hallo Name!", 1], ["Hallo Name!", 2], ["Wie geht es dir?", 1],
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
    [
        "Das hat mir Kollegin auf der Arbeit empfohlen.",
        2,
    ],
    [
        "Praktisch, wenn man so jemanden bei der Arbeit hat. Wie ist es bei Dir gerade dort?",
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
], [[1, 2, 2, "!"], [2, 2, 1, "!"], [20, 4, 4, ""]])

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
], [])

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
], [])

sg_04 = Convo("Ein Treffen alter Freunde", [
    ["Hallo Name! Lange nicht gesehen! Wie geht es Dir denn?", 1],
    [
        "Hallo Annik, mir geht es gut, danke! Es ist wirklich toll, dich wieder zu sehen.",
        2
    ], ["Wie geht’s Dir? Und was machst Du?", 2],
    [
        "Ach, ich bin zufrieden. Wie lange haben wir uns nicht gesehen? 15 Jahre? Stell Dir vor, ich arbeite immer noch in der gleichen Firma wie damals.",
        1
    ], ["Und Du? Lebst Du hier in Berlin?", 1],
    [
        "Du hast recht: Es ist mindestens 15 Jahre her, seit wir uns das letzte Mal gesehen haben. Ich bin gerade zu Besuch in Berlin, ich mache hier eine Weiterbildung.",
        2
    ],
    [
        "ch weiß nicht, ob Du Dich daran erinnerst, dass ich ja für BASF arbeite. Die Firma hat mich nach Amerika versetzt, also bin ich umgezogen. Ich lebe jetzt in einer kleinen Stadt in Tennessee.",
        2
    ],
    [
        "Wir müssen unbedingt Essen gehen, während ich in Berlin bin. Hast du Zeit? Ich zahle!",
        2
    ],
    [
        "Da sage ich nicht nein! Ich erinnere mich noch dass Du damals schwer verliebt warst in eine blonde Studentin. Habt Ihr noch Kontakt?",
        1
    ],
    [
        "Ja, wir waren drei Jahren zusammen. Sie fehlt mir immer noch sehr. Aber sie hat mich nicht geliebt. Sie wollte reisen und keine Kinder haben. Also ist sie Flugbegleiterin geworden, stell Dir vor! Ich glaube, sie ist es immer noch. Aber mir hat das schon das Herz gebrochen, als wir uns getrennt haben. Es hat mich einige Jahre gekostet, über den Liebeskummer weg zu kommen.",
        2
    ], ["Jetzt ist das alles vorbei. Ist ja schon lange her. Und Du?", 2],
    [
        "Ich habe mittlerweile drei Kinder, zwei Mädchen und einen Jungen. Sie gehen alle schon in die Schule. Ich bin aber allein erziehend, ich habe mich vom Vater der Kinder getrennt. Aber wir sind noch befreundet und er kümmert sich um die Kleinen.",
        1
    ],
    [
        "Lebst Du gerne in den USA? Gibt es etwas, das Du vermisst oder das in Deutschland besser war?",
        1
    ],
    [
        "Ja, Das Leben in Amerika ist gut. Meistens sind die Leute nett und das Wetter ist dort, wo ich wohne, milder als in Deutschland. Da, wo ich wohne, herrscht sehr gutes Wetter – es gibt einen zu heißen Monat, einen zu kalten Monat aber die anderen Monate haben alle angenehme Temperaturen. Das Gebirge ist wunderschön, aber Schnee gibt’s im Winter nur selten. Da ist’s in den Alpen schon zuverlässiger.",
        2
    ],
    [
        "Mein größtes Problem ist die Sprache: Der Dialekt in der Gegend ist echt sehr schwer zu verstehen. Man nennt das „Hillbilly-Southern English“.",
        2
    ],
    [
        "Das Schlimmste ist aber: Keinerlei Nachtleben. Oder keine Kneipen, in denen man nach der Arbeit ein gutes Bier trinken kann. Klar, es gibt in Tennessee schon Bars, aber die Atmosphäre ist nicht die Gleiche wie hier in einer Kneipe.",
        2
    ],
    [
        "Na ja. Aber mal eine persönliche Frage: Wie lange bist Du denn schon getrennt? Wie sind deine Kinder mit der Trennung umgegangen? Erzählst du mir mehr über deine Kinder?",
        2
    ],
    [
        "Wir haben uns vor vielen Jahren getrennt, als die Kinder noch klein waren. Sie kennen es also nicht anders – und da wir Freunde geblieben sind, ist es kein großes Problem. Aber es ist natürlich anstrengend.",
        1
    ],
    [
        "Meine jüngste Tochter ist 6 Jahre alt, sie wurde gerade eingeschult. Mein Sohn ist 9, er ist ein typischer Junge, liebt Dinosaurier und Piraten. Und meine älteste Tochter ist schon 14, sie ist also ein Teenager! Unglaublich, oder?",
        1
    ], ["Lebst du allein oder hast Du wieder eine Partnerin?", 1],
    [
        "Ich habe leider keine Kinder – obwohl ich gerne welche hätte. Vielleicht eines Tages. Aber momentan habe ich ja nicht einmal eine Partnerin. Ich würde aber schon gerne heiraten und Kinder haben, ich bin da echt altmodisch. Im Moment verbringe ich viel Zeit mit meinen Eltern, ihnen geht es gesundheitlich nicht gut.",
        2
    ],
    [
        "Oh, das tut mir leid! Aber ich merke schon, wir haben uns viel zu erzählen. Komm, lass uns gleich etwas essen gehen und in Ruhe weiterreden!",
        1
    ], ["Gerne.", 2],
    ["Super. Dann komm mit, da hinten ist mein Lieblingsrestaurant!", 1]
], [[1, 2, 2, "!"], [2, 2, 1, ","]])

sg_05 = Convo("Die Familie", [
    ["Hallo Name.", 1], ["Hallo Name!", 2],
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
], [[1, 2, 2, "."], [2, 2, 1, "!"]])

sg_06 = Convo("Das Konzert", [
    ["Was für ein Sauwetter!", 1],
    ["Das kann man wohl sagen. Es regnet seit Stunden.", 2],
    [
        "Wenn es wenigstens nur ein leichter Nieselregen wäre. Aber es schüttet ja regelrecht!",
        1
    ],
    [
        "Ich habe leider meinen Schirm verloren, ich bin richtig nass geworden als ich vorhin kurz beim Einkaufen war.",
        2
    ],
    [
        "Wenn es ein paar Grad kälter wäre, würde es schneien. Das wäre gleich viel schöner.",
        1
    ],
    [
        "Stimmt. Aber dann wären auch die Straßen gleich wieder glatt – das kann ich gar nicht brauchen. Ich fahre heute Abend noch zu einem Konzert.",
        2
    ], ["Ein Konzert?", 1],
    ["Ja, die Band von Name spielt in der Columbiahalle.", 2],
    [
        "Die Columbiahalle mag ich gar nicht. Viel schöner sind doch Konzerte im Olympiastadion. Oder gleich auf der Waldbühne!",
        1
    ],
    [
        "Aber das geht doch nur im Sommer, wenn es schön warm ist und die Sonne erst spät untergeht. Jetzt im Winter würde ich erfrieren bei einem Open Air!",
        2
    ],
    [
        "Stimmt ja. Wobei ich mal bei einem Open Air war mitten im Sommer, und da war es so neblig, dass man die Bühne fast nicht gesehen hat.",
        1
    ], ["Wirklich?", 2],
    [
        "Ja! Und als der Nebel sich verzogen hatte, zog ein Gewitter auf. So richtig heftig mit starkem Wind, Blitz und Donner. Und Platzregen. Seitdem habe ich keine Konzertkarten mehr gekauft.",
        1
    ], ["Pessimist! Und was machst Du heute Abend?", 2],
    ["Ich gehe erstmal in die Badewanne. Meine Zehen sind ganz kalt.", 1],
    [
        "Dann mal viel Spaß. Ich erzähl Dir nächstes Mal, wie das Konzert war!",
        2
    ]
], [[8, 5, 3, ""]])

sg_07 = Convo("Beim Sport", [
    ["Hallo, Dich habe ich ja schon lange nicht mehr gesehen!", 1],
    ["Stimmt, ich Dich auch nicht. Was machst Du hier?", 2],
    ["Das siehst Du ja, ich jogge.", 1],
    ["Seit wann joggst Du denn? Ich dachte, Du magst keinen Sport?", 2],
    [
        "Mag ich auch nicht. Aber mein Arzt hat gesagt, ich soll mehr Sport machen.",
        1
    ], ["Da hat er natürlich recht. Und, macht es Dir Spaß?", 2],
    [
        "Nein, Spaß kann ich nicht behaupten. Aber es ist schon ok. Ich merke, dass es mir gut tut. Und Du, was machst Du so?",
        1
    ],
    [
        "Ich finde Sport toll. Ich gehe regelmäßig Laufen. Ich habe mich letztes Jahr sogar für einen Halbmarathon angemeldet und es hat gut geklappt!",
        2
    ], ["Wow. Gratuliere.", 1],
    [
        "Danke. Das war echt eine Überwindung. Ich musste mich überwinden, immer weiter zu laufen. Aber danach war ich wirklich glücklich.",
        2
    ], ["Ich bin glücklich, wenn ich zwei Runden um den See schaffe.", 1],
    [
        "Vielleicht ist ja Laufen nichts für Dich. Es gibt ja noch andere Sportarten. Ich gehe jeden Mittwoch zum Schwimmen und zwei Mal pro Woche ins Fitnessstudio.",
        2
    ], ["Wo nimmst Du nur die Zeit dafür her?", 1],
    ["Ach, das geht schon. Dafür bin ich so gut wie nie auf Netflix.", 2],
    [
        "Also ich versuche eher, mich im Alltag zu bewegen. Ich nehme die Treppe statt den Aufzug und ich fahre mit dem Fahrrad in die Arbeit statt mit dem Auto.",
        1
    ],
    [
        "Das sollte jeder so machen, wie er möchte. Ich freu mich jedenfalls, wenn wir uns hin und wieder hier beim Joggen sehen. Bis bald!",
        2
    ], ["Bis bald.", 1]
], [[1, 1, 2, ","]])

sg_08 = Convo("Haustiere", [
    ["Hey, schön Dich zu sehen. Sag mal, wie geht es Deinem Hund?", 1],
    ["Danke dass Du fragst. Schon viel besser.", 2],
    ["Was hatte er denn genau?", 1],
    ["Er hatte sich am Rücken verletzt und musste genäht werden.", 2],
    ["Oh, das klingt gar nicht gut.", 1],
    [
        "Es war zum Glück halb so schlimm. Die Wunde ist schnell verheilt. Er musste halt eine zeitlang einen Trichter um den Hals tragen, damit er sich die Fäden nicht selber zieht. Das hat ihn genervt.",
        2
    ], ["Das kann ich mir vorstellen. Sieht man eine Narbe?", 1],
    [
        "Ja, noch sieht man die Narbe leider sehr gut. Aber wenn das Fell wieder nachgewachsen ist fällt es sicher nicht mehr auf.",
        2
    ], ["Das war bei meiner Katze damals auch so.", 1],
    ["Ach stimmt ja, Du hast eine Katze.", 2],
    [
        "Ja, sie ist schon sehr alt. Fast 20 Jahre alt. Aber sie ist zum Glück sehr gesund. Nur ein bißchen schwerhörig.",
        1
    ],
    ["Mit 20 Jahren darf man ruhig schwerhörig sein. Als Katze zumindest.", 2],
    [
        "Finde ich auch. Der Tierarzt war jedenfalls ganz erstaunt, dass sie so fit ist.",
        1
    ], ["Ist sie denn ein Freigänger?", 2],
    [
        "Ja. Früher hat sie nur in der Wohnung gelebt, weil ich in der Stadt im dritten Stock lebte.",
        1
    ],
    [
        "Aber seit ein paar Jahren darf sie auch nach draußen. Ich bin froh, dass Katzen so selbständig sind!",
        1
    ], ["Warum?", 2], ["Ich hätte keine Lust, andauernd Gassi zu gehen.", 1],
    [
        "Da gewöhnt man sich daran. Ich glaube auch, dass ich deswegen so selten erkältet bin, weil ich bei Wind und Wetter raus gehe.",
        2
    ],
    [
        "Das kann gut sein. Dann wünsche ich Dir viel Spaß draußen, während ich drinnen gemütlich mit einer Tasse Tee sitze, die Katze auf dem Schoß und ein Buch in der Hand.",
        1
    ], ["Du bist gemein.", 2], ["War nicht so gemeint. Bis bald!", 1],
    ["Bis bald!", 2]
], [])

sg_09 = Convo("Eltern und Kind", [
    ["Na, wie war es heute in der Schule?", 1], ["Schön!", 2],
    ["Geht es etwas genauer? Was habt Ihr gemacht?", 1], ["Keine Ahnung.", 2],
    ["Immer muss ich Dir alles aus der Nase ziehen!", 1],
    [
        "In Kunst haben wir einen Wald gemalt. Und in Sport haben wir Fußball gespielt.",
        2
    ], [
        "Das klingt gut. Hast Du in der Pause mit Deinen Freunden gespielt?", 1
    ], ["Ja, wir haben Fangen gespielt.", 2], ["Wer hat gewonnen?", 1],
    ["Jacob und Ich haben gewonnen!", 2], ["War sonst noch irgendwas?", 1],
    ["Ja. Heute hat sich Finnja in der Pause verletzt.", 2],
    ["Oh je! Was ist mit ihr passiert?", 1],
    [
        "Sie ist von der Schaukel gefallen und hat sich das Knie aufgeschlagen.",
        2
    ], ["Hat es geblutet?", 1],
    [
        "Ja, es hat geblutet. Sie hat dann ein Pflaster von der Lehrerin bekommen.",
        2
    ], ["Dann ist ja gut.", 1], ["Bald gibt es Zeugnisse.", 2],
    ["Stimmt. Ich bin gespannt, welche Noten Du bekommst.", 1],
    ["Ist das wichtig?", 2],
    [
        "Noten sind wichtig, damit man weiß, wie gut oder schlecht man in einem Fach ist. Also was man noch besser machen kann oder wo man noch mehr üben muss.",
        1
    ], ["Aber weißt Du, was das beste am Zeugnis ist?", 2], ["Was denn?", 1],
    ["Dass danach die Ferien anfangen!", 2], ["Da hast Du recht!", 1]
], [[10, 1, 3, ""], [12, 5, 4, ""], [13, 6, 4, ""], [14, 1, 4, ""],
    [16, 5, 4, ""]])

sg_10 = Convo("Jobsuche", [
    ["Sag mal, ich wollte dich mal was fragen.", 1], ["Was denn?", 2],
    [
        "Ich bin gerade auf der Suche nach einer neuen Arbeitsstelle. Und ich dachte mir, vielleicht weißt du was?",
        1
    ], ["Oh. Nein, leider nicht. Was ist denn mit deiner alten Stelle?", 2],
    ["Da wurden leider einige Mitarbeiter entlassen.", 1],
    ["Entlassen? Wieso denn?", 2],
    [
        "Weil das Geschäft nicht gut läuft. Also hat man die Mitarbeiter, die noch nicht so lange im Betrieb waren, entlassen.",
        1
    ], ["Geht das einfach so?", 2],
    [
        "Nein, ganz so war es auch nicht. Ich habe eine gute Abfindung bekommen.",
        1
    ], ["Was ist eine Abfindung?", 2],
    [
        "Eine Abfindung ist Geld, damit ich nicht von heute auf morgen ohne Einkommen dastehe.",
        1
    ], ["Aha, verstehe. In welchem Bereich suchst du denn?", 2],
    [
        "Ich würde gerne weiter im Bereich Marketing arbeiten. In den letzten Jahren habe ich mich vor allem auf Social Media Marketing spezialisiert.",
        1
    ], ["Und möchtest du Vollzeit arbeiten?", 2],
    [
        "Nein, Vollzeit kann ich leider nicht arbeiten, weil ich drei Kinder habe. Aber Teilzeit wäre super. Dann kann ich vormittags arbeiten und mich nachmittags um die Familie kümmern.",
        1
    ], ["Hast du sonst noch Einschränkungen?", 2],
    [
        "Ich habe leider kein Auto, daher wäre es gut, wenn ich mit den öffentlichen Verkehrsmitteln in die Arbeit fahren könnte. Ansonsten ist eigentlich alles flexibel. Das Geld ist mir nicht so wichtig.",
        1
    ],
    [
        "Ich hoffe natürlich auf nette Kollegen, aber das zeigt sich ja erst später, wenn man dort arbeitet.",
        1
    ],
    [
        "Ich habe da eine Idee. Ein Bekannter von mir, Falk, arbeitet in einer recht großen Firma, und die haben erst vor kurzem gesagt, dass sie zu wenig im Bereich Facebook und so machen.",
        2
    ],
    [
        "Oh, das wäre super! Könntest du ihn mal fragen, ob ich mich vorstellen kann?",
        1
    ],
    [
        "Das mache ich! Schick mir doch mal deine Initiativbewerbung per Mail, dann gebe ich sie weiter.",
        2
    ], ["Gerne. Ich danke dir tausend mal!", 1
        ], ["Kein Problem. Bis bald!", 2], ["Bis bald!", 1]
], [[19, 10, 3, ","], [20, 7, 3, ""]])

sg_11 = Convo("Mein Kind ist krank", [
    ["Hast du heute Zeit für einen Spaziergang?", 1],
    ["Leider nicht. Mein Sohn ist krank.", 2], ["Oh je. Was hat er denn?", 1],
    [
        "Er ist heute morgen mit Fieber aufgewacht. Er hat ein wenig Schnupfen und Husten. Und vorhin hat er gesagt, dass er Kopfschmerzen hat.",
        2
    ], ["Das klingt nach einer Grippe.", 1],
    [
        "Ja, oder eine Erkältung. Er muss jetzt viel trinken. Ich habe ihn in der Schule entschuldigt.",
        2
    ], ["Gehst du mit ihm zum Arzt?", 1],
    [
        "Ich weiß es noch nicht. Wenn es ihm morgen nicht besser geht, werde ich mit ihm zum Kinderarzt gehen.",
        2
    ],
    [
        "Würde ich auch so machen. Du kannst ihm gegen die Kopfschmerzen ein Schmerzmittel geben.",
        1
    ],
    [
        "Das werde ich tun. Ich habe einen Saft, der gegen Fieber und Schmerzen hilft.",
        2
    ], ["Ich hasse das Gefühl, ein krankes Kind zu haben.", 1],
    [
        "Ja, ich wäre auch lieber selber krank. Aber man kann es nicht ändern.",
        2
    ],
    [
        "Jetzt im Winter sind einfach viele Viren unterwegs. In der Schule haben die Kinder viel Kontakt zueinander. Da stecken sie sich dann halt auch an.",
        2
    ],
    [
        "Aber als Kind war ich eigentlich ganz gerne krank, erinnere ich mich.",
        1
    ],
    [
        "Kein Wunder! Mein Sohn darf den ganzen Tag fernsehen, ich bringe ihm Essen und Getränke und die Katze hat auch bei ihm geschlafen. Das ist doch perfekt, um gesund zu werden.",
        2
    ], ["Stimmt! Na dann wünsche ich deinem Sohn gute Besserung.", 1],
    ["Danke. Ich werde es ihm ausrichten.", 2],
    ["Hoffentlich steckst du dich nicht an! Bleib gesund!", 1],
    ["Ich gebe mir Mühe. Ich war erst vor zwei Wochen krank.", 2],
    ["Wirklich? Das habe ich gar nicht mitbekommen!", 1],
    [
        "Doch, da konnte ich zwei Tage nicht in die Arbeit gehen. Zum Glück war ich am dritten Tag wieder fit, sonst hätte ich ein Attest vom Arzt gebraucht.",
        2
    ],
    [
        "Ich bin auch froh, wenn ich nicht zum Arzt muss. Im Wartezimmer zu sitzen mit lauter anderen kranken Menschen ist nicht so toll.",
        1
    ],
    [
        "Stimmt, aber manchmal geht es eben nicht anders. Vor allem wenn man ein Rezept braucht für Medikamente.",
        2
    ],
    [
        "Also dann – ich melde mich übermorgen nochmal bei dir. Vielleicht hast du dann Zeit für einen Spaziergang.",
        1
    ], ["Gerne. Bis dann!", 2], ["Bis dann!", 1]
], [])

# Convo list
convo_list = [sg_01, sg_02, sg_03, sg_04, sg_05, sg_06, sg_07, sg_08, sg_09, sg_10, sg_11]
