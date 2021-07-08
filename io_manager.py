import TextManagement.transform as trend
import TextManagement.vocab as vocab
import TextManagement.convo as convo
import random

IDs = [
    "Blind Fish", "Trainerd", "Dilara", "Elli", "Ian", "Jamila", "Jila",
    "Lara", "Lisa", "Logikerus", "Emilia"
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
    return text


# Conversation Function
def conversation(intensity=50):
    talk = random.choice(convo.convo_list)

    # Generate User IDs
    count = talk.amount
    user_ids = []
    while count > 0:
        rnd = random.randint(0, 10)
        if rnd not in user_ids:
            user_ids.append(rnd)
            count -= 1

    # Assign User IDs to the Conversation
    assigned_talk = []
    for line in talk.lines:
        assigned_talk.append([line[0], user_ids[line[1] - 1]])

    # Translate Conversation
    final_talk = []
    for line in assigned_talk:
        final_talk.append(IDs[line[1]] + ": " +
                          transition(line[0], line[1], intensity))

    return [talk.title, user_ids, final_talk]
