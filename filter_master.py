from collections import Set

FILTER_STAGE = 0  # agressive filtering to remove crap

ACCEPTABLE_CHARS = {'40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '50',
                    '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5c', '5d', '60', '61', '62', '63',
                    '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '70', '71', '72', '73', '74',
                    '75', '76', '77', '78', '79', '7a', '2c', '2e', '21', '3a', '20', '27', '2d', '3f', '0a', '80',
                    '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96',
                    '97', '98', '99', '8a', '8b', '8c', '8d', '8e', '9a', '9b', '9c', '9d', '9e', 'aa', 'ab', 'ac',
                    'ad', 'b4', 'b5', 'b6', 'b7', 'b8', 'c6', 'c7', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7',
                    'd8', 'dd', 'de', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec',
                    'ed', 'ee', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc'}


def filter_output():
    global FILTER_STAGE
    i = 0


def is_good_guess_hard(guess):  # Accepts only [a-z,A-Z] ! : - . , ? \n SPACE
    """
    Be a magician an guess
    :param guess:
    :return:
    """
    for value in guess:
        symbol = value.encode("hex")
        if (('40' < symbol < '5b') or ('60' < symbol < '7b')
            or (symbol == '2c')
            or (symbol == '21') or (symbol == '27')
            or (symbol == '2e') or (symbol == '2d')
            or (symbol == '3a') or (symbol == '3f')
            or (symbol == '20') or (symbol == '0a')):
            pass
        else:
            return False
    return True


def is_good_guess_hard_optimise(guess):
    return set([i.encode("hex") for i in guess]).issubset(ACCEPTABLE_CHARS)

# with open('allowedvals.txt', 'r') as _file:
#     vals = [i.strip("\n") for i in _file.readlines()]
#     print vals
#     print len(vals)
