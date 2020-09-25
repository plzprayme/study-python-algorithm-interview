test_cases = [
    ["h", "e", "l", "l", "o"],
    ["H", "a", "n", "n", "a", "h"]
]


def reverse_list(test_case):
    # test_case.revers()
    # test_case[::-1]

    front, back = 0, len(test_case) - 1
    while front < back:
        test_case[front], test_case[back] = test_case[back], test_case[front]
        front += 1
        back -= 1
    return test_case


def main(test_case):
    return reverse_list(test_case)


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")


start(test_cases)
