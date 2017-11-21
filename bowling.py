def score(game):
    """ Calculates the overall score of a bowling game"""
    
    in_first_half = True
    result = Constants.MINIMUM_POINT
    frame = 1
    previous_value = 0
    for index in range(len(game)):
        current_value = get_value(game[index])
        if game[index] == '/':
            result += Constants.MAXIMUM_POINT - previous_value
        else:
            result += current_value
        if frame < Constants.FRAMES_THRESHOLD and current_value == Constants.MAXIMUM_POINT:
            next_value = get_value(game[index + 1])
            if game[index] == '/':
                result += next_value
            elif game[index] == 'X' or game[index] == 'x':
                result += next_value
                if game[index + 2] == '/':
                    result += Constants.MAXIMUM_POINT - next_value
                else:
                    result += get_value(game[index + 2])
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
        if game[index].lower() == 'x':
            in_first_half = True
            frame += 1
        previous_value = current_value
    return result


def get_value(char):
    result = None
    if char >= '1' and char <= '9':
        result = int(char)
    elif char.lower() == 'x' or char == '/':
        result = Constants.MAXIMUM_POINT
    elif char == '-':
        result = Constants.MINIMUM_POINT
    else:
        raise ValueError()
    return result

class Constants():
    FRAMES_THRESHOLD = 10
    MAXIMUM_POINT = 10
    MINIMUM_POINT = 0
