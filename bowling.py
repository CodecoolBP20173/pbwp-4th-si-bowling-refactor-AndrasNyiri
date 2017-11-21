def score(game):
    result = 0
    frame = 1
    in_first_half = True
    previous_value = 0
    for index in range(len(game)):
        if game[index] == '/':
            result += 10 - previous_value
        else:
            result += get_value(game[index])
        if frame < 10 and get_value(game[index]) == 10:
            if game[index] == '/':
                result += get_value(game[index + 1])
            elif game[index] == 'X' or game[index] == 'x':
                result += get_value(game[index + 1])
                if game[index + 2] == '/':
                    result += 10 - get_value(game[index + 1])
                else:
                    result += get_value(game[index + 2])
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
        if game[index].lower() == 'x':
            in_first_half = True
            frame += 1
        previous_value = get_value(game[index])
    return result


def get_value(char):
    result = None
    if char >= '1' and char <= '9':
        result = int(char)
    elif char.lower() == 'x' or char == '/':
        result = 10
    elif char == '-':
        result = 0
    else:
        raise ValueError()
    return result
