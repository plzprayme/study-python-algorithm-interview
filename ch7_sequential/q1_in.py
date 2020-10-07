test_cases = [
    dict(nums=[2,7,11,15], target=9),
]
def main(test_case):
    nums = test_case["nums"]
    target = test_case["target"]

    for idx, item in enumerate(nums):
        elem = target - item
        if elem in nums[idx+1:]:
            return idx, nums[idx+1:].index(elem) + idx + 1

    return False
    # return is_palindrome(char_num_list)


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")


start(test_cases)