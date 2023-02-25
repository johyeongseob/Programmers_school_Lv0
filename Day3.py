# 최빈값 구하기

from collections import Counter

arr=[1,1,1,2,2,2]
cnt = Counter(arr)
order = cnt.most_common()

ans=order[0][0]

# 여러개 최빈값의 경우 -1

try:
    if order[0][1]==order[1][1]:
        ans=-1
except:
    ans=ans

print(ans)
