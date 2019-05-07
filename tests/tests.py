from rlib.lists import count, sum, sort, max, min
from rlib.calc import mult, div, pot, fac

def create_test():
    return [
        {'test': lambda: count([2, 4, 6, 8, 10]), 'expected': 5, 'method': "count list with 5 items"},
        {'test': lambda: count([]), 'expected': 0, 'method': "count list with no items"},
        {'test': lambda: count(['one item']), 'expected': 1, 'method': "count list with 1 item"},

        {'test': lambda: sum([2, 4, 6, 8, 10]), 'expected': 30, 'method': "sum list with 5 items, total: 30"},
        {'test': lambda: sum([]), 'expected': 0, 'method': "sum list with no items"},
        {'test': lambda: sum([3]), 'expected': 3, 'method': "sum list with number 3"},

        {'test': lambda: sort([2, 8, 4, 10, 6]), 'expected': [2, 4, 6, 8, 10], 'method': "sort list with 5 items"},
        {'test': lambda: sort([2,2]), 'expected': [2,2], 'method': "sort list with 2 equal items"},
        {'test': lambda: sort([2,4]), 'expected': [2,4], 'method': "sort list with 2 ordered items"},
        {'test': lambda: sort([2]), 'expected': [2], 'method': "sort list with 1 item"},
        {'test': lambda: sort([]), 'expected': [], 'method': "sort list with no items"},

        {'test': lambda: max([2, 8, 4, 10, -6]), 'expected': 10, 'method': "max list with 5 items"},
        {'test': lambda: max([2,2]), 'expected': 2, 'method': "max list with 2 equal items"},
        {'test': lambda: max([4]), 'expected': 4, 'method': "max list with 1 items"},
        {'test': lambda: max([]), 'expected': 0, 'method': "max list with no items"},

        {'test': lambda: min([2, 8, 4, 10, -6]), 'expected': -6, 'method': "min list with 5 items"},
        {'test': lambda: min([2,2]), 'expected': 2, 'method': "min list with 2 equal items"},
        {'test': lambda: min([4]), 'expected': 4, 'method': "min list with 1 items"},
        {'test': lambda: min([]), 'expected': 0, 'method': "min list with no items"},

        {'test': lambda: mult(2,5), 'expected': 10, 'method': "mult two number"},
        {'test': lambda: mult(-2,5), 'expected': -10, 'method': "mult two number (fiest negative)"},
        {'test': lambda: mult(2,-5), 'expected': -10, 'method': "mult two number (second negative)"},
        {'test': lambda: mult(-2,-5), 'expected': 10, 'method': "mult two number (both negatives)"},
        {'test': lambda: mult(2,0), 'expected': 0, 'method': "mult by zero"},
        {'test': lambda: mult(0,2), 'expected': 0, 'method': "mult zero by number"},
        {'test': lambda: mult(0,0), 'expected': 0, 'method': "mult zero by zero"},

        {'test': lambda: div(2,5), 'expected': 0, 'method': "div 2/5"},
        {'test': lambda: div(5,2), 'expected': 2, 'method': "div 5/2"},
        {'test': lambda: div(10,2), 'expected': 5, 'method': "div 10/2"},
        {'test': lambda: div(-2,5), 'expected': 0, 'method': "div negative by positive number (-2/5)"},
        {'test': lambda: div(2,-5), 'expected': 0, 'method': "div positive by negative number (2/-5)"},
        {'test': lambda: div(-2,-5), 'expected': 0, 'method': "div two negative number (-2/-5)"},
        {'test': lambda: div(-5,2), 'expected': -2, 'method': "div negative by positive number (-5/2)"},
        {'test': lambda: div(5,-2), 'expected': -2, 'method': "div positive by negative number (5/-2)"},
        {'test': lambda: div(-5,-2), 'expected': 2, 'method': "div two negative numbers (-5/-2)"},
        {'test': lambda: div(2,0), 'expected': ZeroDivisionError.__name__, 'method': "div by zero"},
        {'test': lambda: div(0,2), 'expected': 0, 'method': "div zero by number"},
        {'test': lambda: div(0,0), 'expected': ZeroDivisionError.__name__, 'method': "div zero by zero"},

        {'test': lambda: pot(2,0), 'expected': 1, 'method': "pot exponent zero"},
        {'test': lambda: pot(-2,0), 'expected': 1, 'method': "pot negative base with exponent zero"},
        {'test': lambda: pot(0,2), 'expected': 0, 'method': "pot base zero"},
        {'test': lambda: pot(0,0), 'expected': 1, 'method': "pot base and expontent zero"},
        {'test': lambda: pot(-3,2), 'expected': 9, 'method': "pot negative base with even exponent"},
        {'test': lambda: pot(-3,3), 'expected': -27, 'method': "pot negative base with odd exponent"},
        {'test': lambda: pot(0,-3), 'expected': 0, 'method': "pot negative exponent with base zero"},
        {'test': lambda: pot(2,-3), 'expected': 0.125, 'method': "pot negative exponent with positive base"},
        {'test': lambda: pot(-2,-3), 'expected': -0.125, 'method': "pot negative exponent with negative base"},

        {'test': lambda: fac(-4), 'expected': 24, 'method': "fac of negative even number"},
        {'test': lambda: fac(-5), 'expected': -120, 'method': "fac of negative odd number"},
        {'test': lambda: fac(0), 'expected': 1, 'method': "fac of zero"},
        {'test': lambda: fac(-1), 'expected': -1, 'method': "fac of -1"},
        {'test': lambda: fac(1), 'expected': 1, 'method': "fac of 1"},
        {'test': lambda: fac(4), 'expected': 24, 'method': "fac of positive even number"},
        {'test': lambda: fac(5), 'expected': 120, 'method': "fac of positive odd number"},
        ]
