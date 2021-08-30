def simple_func(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err
