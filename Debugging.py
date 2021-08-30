# debugging

# linting -> num + 4(red underline -> linting | red underline)

# pdb -> The Python debugger for interactive interpreters.
import pdb


def add(num1, num2):
    pdb.set_trace()
    t = 4 * 5
    return num1 + num2


add(4, 'kjks')
