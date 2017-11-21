def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i + 1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i + 1])
                if game[i + 2] == '/':
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
            in_first_half = True
        else:
            in_first_half = False
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
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
