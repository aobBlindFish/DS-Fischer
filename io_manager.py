import TextManagement.transform as trend
import TextManagement.vocab as vocab
import TextManagement.convo as convo
import TextManagement.StringPreset as StrP
import random

IDs = [
    "Adrian", "Gill", "Dilara", "Elli", "Ian", "Jamila", "Jila", "Lara",
    "Lisa", "Marvin", "Emilia"
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


# Conversation Function
def conversation(intensity=50):
    talk = random.choice(convo.convo_list)

    # Generate User IDs
    count = talk.amount
    max_amount = count[1]
    user_ids = []
    while max_amount > 0:
        rnd = random.randint(0, 10)
        if rnd not in user_ids:
            user_ids.append(rnd)
            max_amount -= 1

    # Assign User IDs to the Conversation
    assigned_talk = []
    for line in talk.lines:
        assigned_talk.append([line[0], user_ids[line[1] - 1]])

    # Exchange Words in lines
    exchanged_talk = []
    for line in assigned_talk:
        for change in talk.additions:
            if line in assigned_talk and assigned_talk.index(
                    line) + 1 == change[0]:
                name = IDs[user_ids[change[2] - 1]]
                word = name + change[3]
                line = [StrP.exchange(line[0], word, [change[1]]), line[1]]

        exchanged_talk.append(line)

    # Translate Conversation
    final_talk = []
    for line in exchanged_talk:
        final_talk.append("**" + IDs[line[1]] + "**: " +
                          transition(line[0], line[1], intensity))

    # Remove extra user_ids
    temp = user_ids
    user_ids = []
    main_amount = count[0]
    k = 0
    while main_amount != 0:
        user_ids.append(temp[k])
        main_amount -= 1
        k += 1

    return [talk.title, user_ids, final_talk]
