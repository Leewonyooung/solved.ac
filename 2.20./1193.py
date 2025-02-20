"""
1193번 분수찾기
"""

def sol(maketry):
    m = 1
    n = 1
    if maketry < 0: 
        return 1, 1
    else:
        if temp % 2 == 0:
            for j in range(maketry):
                n = j + 1
                m = temp - j
            return n, m
        else:
            for j in range(maketry):
                m = j + 1
                n = temp - j
            return n, m


t:int = int(input())
i = 0
temp = 1
cnt = 0
while(t > i):
    if(t > i + temp):
        i = i + temp
        temp = temp + 1
        cnt = t-i
    else:
        break
    
first, second = sol(cnt)
print(f"{first}/{second}")
