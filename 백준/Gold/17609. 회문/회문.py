def is_palindrome(s, left, right):
    while left<right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True 


def check(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        
        else:
            remove_left  = is_palindrome(s, left+1, right)
            remove_right = is_palindrome(s, left, right-1)

            if remove_left or remove_right:
                return 1
            else:
                return 2
    return 0

t = int(input())
for _ in range(t):
    s = input().strip()
    print(check(s))