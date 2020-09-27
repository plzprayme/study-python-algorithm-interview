# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

import collections

test_cases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"]
]


def main(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")


start(test_cases)
