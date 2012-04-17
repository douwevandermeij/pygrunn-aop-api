"""
This is an existing library with functions
"""


def add(lhs, rhs):
    return int(lhs) + int(rhs)


def sub(lhs, rhs):
    return int(lhs) - int(rhs)


def mult(lhs, rhs):
    return int(lhs) * int(rhs)


def div(lhs, rhs):
    return int(lhs) / int(rhs)


def something_cool(function, token):
    return '{0}-{1}'.format(function, token)
