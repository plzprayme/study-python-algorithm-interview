import collections

test_cases = [
    "A man, a plan, a canal: Panama",  # True
    "race a car"  # False
]


def extract_num_char(test_case):
    deque = collections.deque()

    for x in test_case:
        if 'a' <= x < 'z' or '0' <= x < '9':
            deque.append(x)

    return deque


def is_palindrome(deque):
    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return False

    return True


def main(test_case):
    char_num_list = extract_num_char(test_case.lower())
    return is_palindrome(char_num_list)


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")


start(test_cases)
