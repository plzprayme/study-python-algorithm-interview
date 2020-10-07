test_cases = [
    dict(nums=[2,7,11,15], target=9),
]
def main(test_case):
    nums = test_case["nums"]
    target = test_case["target"]

    DICT = {}
    for idx, item in enumerate(nums):
        DICT[item] = idx

    for i, num in enumerate(nums):
        if target - num in DICT and i != DICT[target-num]:
            return nums.index(num), DICT[target-num]

    return False
    # return is_palindrome(char_num_list)


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")


start(test_cases)