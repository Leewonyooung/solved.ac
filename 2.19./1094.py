"""
1094번 막대기
"""
X = int(input())

i = 6
stick: int = 64
saved = []

def listSum():
    sum = 0
    for i in saved:
        sum = sum + i
    return sum

while(True):
    stick = int(stick // 2)
    saved.append(int(2 ** i))
    if int(2 ** i) > stick:
        if(listSum() > X): saved.pop()
    i = i - 1
    if i == 0 : 
        saved.append(1)
        if(int(listSum()) != X):
            saved.pop()
        break

print(len(saved))
