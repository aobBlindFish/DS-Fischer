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