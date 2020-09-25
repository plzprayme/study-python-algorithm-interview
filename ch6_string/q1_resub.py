import re

test_cases = [
    "A man, a plan, a canal: Panama",  # True
    "race a car"  # False
]


def extract_num_char(test_case):
    test_case = test_case.lower()
    return re.sub('[^a-z0-9]', '', test_case)


def is_palindrome(test_case):
    return test_case == test_case[::-1]


def main(test_case):
    char_num_list = extract_num_char(test_case)
    return is_palindrome(char_num_list)


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")


start(test_cases)
