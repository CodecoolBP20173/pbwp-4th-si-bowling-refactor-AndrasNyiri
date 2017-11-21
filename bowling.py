""" Bowling kata """


def score(game):
    """ Calculates the overall score of a bowling game"""

    in_first_half = True
    overall_score = Constants.MINIMUM_POINT
    frame = 1
    previous_point = 0
    for index, current_character in enumerate(game):
        current_point = get_value(current_character)
        if current_character == '/':
            overall_score += Constants.MAXIMUM_POINT - previous_point
        else:
            overall_score += current_point
        if frame < Constants.FRAMES_THRESHOLD and current_point == Constants.MAXIMUM_POINT:
            next_point = get_value(game[index + 1])
            after_next_character = game[index + 2] 
            overall_score += next_point
            if current_character == 'X' or current_character == 'x':
                if after_next_character == '/':
                    overall_score += Constants.MAXIMUM_POINT - next_point
                else:
                    overall_score += get_value(after_next_character)
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
        if current_character.lower() == 'x':
            in_first_half = True
            frame += 1
        previous_point = current_point
    return overall_score


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
