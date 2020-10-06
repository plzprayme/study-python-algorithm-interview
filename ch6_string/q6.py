# 가장 긴 팰린드롬 부분 문자열을 출력하라.

import collections

test_cases = [
    "babad",
    "cbbd"
]


def is_palindrome(list):
    list = collections.deque(list)
    print(list)
    while len(list) > 1:
        if list.popleft() != list.pop():
            return False

    return True


def main(test_case):
    s = test_case
    if len(s) == 1:
        return 1

    if len(s) == 2:
        if is_palindrome(s):
            return 2
        return 1

    window = 2
    result = 1
    while window < len(s):
        start = 0
        while start + window <= len(s):
            if is_palindrome(s[start:start + window]):
                result += 1
            start += 1
        window += 1

    return result


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")


start(test_cases)
