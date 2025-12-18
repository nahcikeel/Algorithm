def is_valid(tree):
    if len(tree) == 1:
        return True

    mid = len(tree) // 2
    root = tree[mid]

    left = tree[:mid]
    right = tree[mid+1:]

    if root == '0':
        if '1' in left or '1' in right:
            return False

    return is_valid(left) and is_valid(right)


def solution(numbers):
    answer = []

    for num in numbers:
        binary = bin(num)[2:]

        length = 1
        while length < len(binary):
            length = length * 2 + 1

        binary = binary.zfill(length)
        answer.append(1 if is_valid(binary) else 0)

    return answer
