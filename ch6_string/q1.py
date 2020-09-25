test_cases = [
    "A man, a plan, a canal: Panama",  # True
    "race a car"  # False
]


def extract_num_char(test_case):
    return [x for x in test_case if 'a' <= x < 'z' or '0' <= x < '9']


def slice_to_half(char_num_list):
    list_length = len(char_num_list)
    half_length = list_length // 2

    front = char_num_list[:half_length]
    back = char_num_list[half_length:list_length]

    if list_length % 2 == 1:
        back = char_num_list[half_length + 1:list_length]

    return front, back


def is_palindrome(*lists):
    front = lists[0]
    back = reversed(lists[1])

    for idx, item in enumerate(back):
        if front[idx] != item:
            return False

    return True


def main(test_case):
    char_num_list = extract_num_char(test_case.lower())
    front, back = slice_to_half(char_num_list)
    return is_palindrome(front, back)


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")


start(test_cases)
