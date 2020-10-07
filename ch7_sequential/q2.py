test_cases = [
    [0,1,0,2,1,0,1,3,2,1,2,1]
]

# left 와 right를 지정한다.
# left와 right 중 작은 수와
# 중간에 있는 녀석들을 빼고 합한다

def main(test_case):
    height = test_case

    result2 = 0
    result = []
    left = -1
    for i, item in enumerate(height):
        print(f"i: {i}, item: {item}")
        if left == -1 and i != 0:
            left = item
            result.append(i)
        elif left != -1 and item >= left:
            left = item
            result.append(i)

    print(result)
    for i in range(len(result[1:])):
        hole = height[result[i]:result[i + 1]]
        left = hole[0]
        for j in hole[1:]:
            result2 += left - j
            print(f"LEFT: {left} | j: {j}")

    return result2


def start(test_cases):
    for idx, case in enumerate(test_cases):
        print(f"case {idx}: {main(case)}")


start(test_cases)
