from collections import Counter

name = input().strip()
cnt = Counter(name)

odd_chars = [ch for ch in cnt if cnt[ch] % 2 == 1]

if len(odd_chars) > 1:
    print("I'm Sorry Hansoo")
else:
    center = odd_chars[0] if odd_chars else ""
    left = ""

    for ch in sorted(cnt.keys()):
        left += ch * (cnt[ch] // 2)

    right = left[::-1]

    print(left + center + right)
