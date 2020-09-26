import collections
import re

# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표) 또한 무시한다.
test_cases = [
    "Bob hit a ball, the hit BALL flew far after it was hit."
]

banned = ["hit"]


def main(words, banned):
    words = words.lower()
    words = re.sub(pattern='[^\w\s]', repl='', string=words)

    result = []
    for banned_word in banned:
        result = words.replace(banned_word, "")

    count = collections.Counter(result.split(" "))
    for item, common in count.most_common(2):
        if item != "":
            return item


def start(test_cases, banned):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case, banned)}")


start(test_cases, banned)
