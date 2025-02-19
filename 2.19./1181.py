"""
1181 단어 정렬
"""
cnt = int(input())

words = []
s_words = []
for _ in range(cnt):
    words.append(input())

maxlen = 0
for x in words:
    if(maxlen < len(x)): maxlen = len(x)

find_len = 0
while(maxlen >= find_len):
    sorted = []
    for j in range(len(words)):
        if (len(words[j]) == int(find_len)) and (words[j] not in sorted):
            sorted.append(words[j])
    sorted.sort()
    for x in sorted:
        s_words.append(x)
    find_len = find_len +1

for x in s_words:
    print(x)

"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
"""
