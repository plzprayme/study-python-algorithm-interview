# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.


test_cases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"]
]


def main(strs):
    dict = {}
    for str in strs:
        sorted_str = "".join(sorted(str))

        try:
            if dict[sorted_str]:
                dict[sorted_str] = dict[sorted_str] + [str]
        except:
            dict[sorted_str] = [str]

    return [x for x in dict.values()]


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")


start(test_cases)
