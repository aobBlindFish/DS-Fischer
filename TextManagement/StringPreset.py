def str_trim(text, index_str):
    index = int(index_str)
    output = ""
    if float(index) < 0:
        for i in range(len(text) - abs(index)):
            output += text[i]

    elif float(index) > 0:
        for i in range(len(text) - index):
            output += text[i + index]

    else:
        output = text
    return output

def exchange(text, word, position):
    def exchange_main(text, word, position):
        str_split = text.split(" ")
        output = ""
        counter = 0
        for i in str_split:
            counter += 1
            if counter == position:
                i = word

            output = output + i + " "

        return str_trim(output, -1)

    for j in position:
        text = exchange_main(text, word, j)

    return text