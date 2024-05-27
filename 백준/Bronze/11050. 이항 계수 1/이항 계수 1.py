n,k = map(int, input().split())

def factorial(num):
    result = 1
    for i in range(2, num+1):
        result *= i

    return result

print(int(factorial(n)/(factorial(k)*factorial(n-k))))