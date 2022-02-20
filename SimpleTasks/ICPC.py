from time import time
from functools import reduce
import math

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} s')
        return result

    return wrapper


# # Check for cycle word; True
# def check_palindrome(cycle_word):
#     if cycle_word.find(cycle_word[::-1]):
#         return False
#
#     return True
#
#
# @performance
# def drunken_palindrome(cycle_word):
#     if check_palindrome(cycle_word):
#         return cycle_word[:int(len(cycle_word) / 2):]
#
#     for i in range(0, len(cycle_word)):
#         if check_palindrome(cycle_word[:i:] + cycle_word) and check_palindrome(cycle_word + cycle_word[:i:]):
#             return cycle_word[:i:]
#
#     return cycle_word[::-1]
#
#
# def runInParallel(*fns):
#   proc = []
#   for fn in fns:
#     p = Process(target=fn)
#     p.start()
#     proc.append(p)
#   for p in proc:
#     p.join()
#
#
# def drunken_palindrome_parallel(cycle_word):
#     if len(cycle_word) == 0:
#         return
#


# Python 3 program for
# implementation of
# Sieve of Atkin

@performance
def decomposition(number):
    half_limit = int(number/2)
    if int(number / 2) * 2 < number:
        return half_limit + 1

    return half_limit

# def path_to_home(n, m, k):
#     if m == 0:
#         return 1
#     if m != 0 and k == 0:
#         return 0
#
#     return sum(path_to_home(n, m - i, k - 1) for i in range(1, n))

if __name__ == "__main__":
    # string_val = "".join(choice(ascii_lowercase) for i in range(int(1e2)))
    # result = drunken_palindrome(string_val)
    # print(result)
    # print(f"s + t: {check_palindrome(string_val + result)}")
    # print(f"t + s: {check_palindrome(result + string_val)}")
    # limit = int(51)
    # print(decomposition(int(limit)))
    # n, m, k = 4, 5, 3
    # all_vals = 0
    # for i in range(m, sum(range(1, n)), m):
    #     all_vals += path_to_home(n, i, k)
    # print(all_vals)
    print(reduce(lambda acc, item: abs(acc - item), [100, 200, int(1e9)]))