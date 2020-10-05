test_cases = [
    dict(nums=[2,7,11,15], target=9),
]
def main(test_case):
    nums = test_case["nums"]
    target = test_case["target"]



    for idx, num in enumerate(nums):
        for idx2, num2 in enumerate(nums[idx+1:]):
            if num + num2 == target:
                return idx, idx + idx2 + 1

    return False
    # return is_palindrome(char_num_list)


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")


start(test_cases)
