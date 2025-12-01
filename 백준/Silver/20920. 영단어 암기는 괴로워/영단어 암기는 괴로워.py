import sys
input = sys.stdin.readline

N, M = map(int, input().split())

freq = {}

for _ in range(N):
    word = input().strip()
    
    if len(word) < M:
        continue
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], -len(w), w))

print("\n".join(sorted_words))
