# 로그를 재정렬하라
# 1. 로그의 가장 앞 부분은 식별자이다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.

test_cases = [
    ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
]


def reorder_log_files(test_case):
    num_list, char_list = [], []
    for logs in test_case:
        log = logs.split(" ")
        if '0' <= log[1][0] <= '9':
            num_list.append(logs)
        else:
            # char_list.append(logs)
            char_list.append(" ".join(log[1:] + log[:1]))

    char_list.sort()

    sorted_char_list = []
    for char in char_list:
        splited_list = char.split(" ")
        sorted_char_list.append(" ".join(splited_list[-1:] + splited_list[:-1]))

    return sorted_char_list + num_list


def main(test_case):
    print(reorder_log_files(test_case))


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")

start(test_cases)