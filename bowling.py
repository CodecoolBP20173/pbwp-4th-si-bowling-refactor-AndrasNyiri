""" Bowling kata """


def score(game):
    """ Calculates the overall score of a bowling game"""

    game = game.lower()
    in_first_half = True
    overall_score = Constants.MINIMUM_POINT
    frame = 1
    for index, current_character in enumerate(game):
        current_point = get_value(current_character)
        overall_score += current_point
        if current_character == '/':
            overall_score -= get_value(game[index - 1])
        if frame < Constants.FRAMES_THRESHOLD and current_point == Constants.MAXIMUM_POINT:
            next_point = get_value(game[index + 1])
            overall_score += next_point
            if current_character == 'x':
                overall_score += get_value(game[index + 2])
                if game[index + 2] == '/':
                    overall_score -= next_point

        if not in_first_half or current_character == 'x':
            in_first_half = True
            frame += 1
        else:
            in_first_half = False
    return overall_score


def get_value(character):
    """ returns an the actual point value of a character """

    point = -1
    if character >= '1' and character <= '9':
        point = int(character)
    elif character in ['x', '/']:
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
