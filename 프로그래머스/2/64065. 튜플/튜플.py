import re
from collections import Counter

def solution(s):
    numbers = re.findall(r'\d+', s)
    count = Counter(numbers)
    
    result = [int(num) for num, _ in count.most_common()]
    
    return result
