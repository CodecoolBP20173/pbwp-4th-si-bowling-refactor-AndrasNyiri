""" Bowling kata """


def score(game):
    """ Calculates the overall score of a bowling game"""

    in_first_half = True
    result = Constants.MINIMUM_POINT
    frame = 1
    previous_value = 0
    for index, current_element in enumerate(game):
        current_value = get_value(current_element)
        if current_element == '/':
            result += Constants.MAXIMUM_POINT - previous_value
        else:
            result += current_value
        if frame < Constants.FRAMES_THRESHOLD and current_value == Constants.MAXIMUM_POINT:
            next_value = get_value(game[index + 1])
            if current_element == '/':
                result += next_value
            elif current_element == 'X' or current_element == 'x':
                result += next_value
                if game[index + 2] == '/':
                    result += Constants.MAXIMUM_POINT - next_value
                else:
                    result += get_value(game[index + 2])
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
        if current_element.lower() == 'x':
            in_first_half = True
            frame += 1
        previous_value = current_value
    return result


def get_value(character):
    """ returns an the actual point value of a character """

    point = -1
    if character >= '1' and character <= '9':
        point = int(character)
    elif character.lower() == 'x' or character == '/':
        point = Constants.MAXIMUM_POINT
    elif character == '-':
        point = Constants.MINIMUM_POINT
    else:
        raise ValueError()
    return point


class Constants():
    """ Stores the constant values of a bowling game """

    FRAMES_THRESHOLD = 10
    MAXIMUM_POINT = 10
    MINIMUM_POINT = 0
