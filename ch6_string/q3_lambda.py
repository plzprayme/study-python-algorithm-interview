# 로그를 재정렬하라
# 1. 로그의 가장 앞 부분은 식별자이다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.

test_cases = [
    ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
]


def reorder_log_files(test_case):
    letters, digits = [], []
    for log in test_case:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # x.split()[1:] 을 통해서 정렬 후 (식별자 외)
    # 같은 녀석끼리는 x.split()[0]을 통해서 정렬 (식별자)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


def main(test_case):
    print(reorder_log_files(test_case))


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")

start(test_cases)