"""
1010번 다리 놓기
"""
import math
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    answer = math.comb(m,n)
    print(answer)

