def multiply(num1, num2):
    try:
        return num1 * num2
    except (ValueError, TypeError):
        return 'Please input correct value'


def divide(num1, num2):
    try:
        return num1 / num2
    except (ValueError, TypeError):
        return 'Please input correct value'
    except ZeroDivisionError:
        return 'Second number can not be zero!'