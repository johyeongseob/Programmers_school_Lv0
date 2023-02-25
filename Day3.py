# 최빈값 구하기

from collections import Counter

arr=[1,1,2,2]
cnt = Counter(arr)
ans = cnt.most_common()

ans1=ans[0][1]
print(ans)

# 여러개 최빈값의 경우 -1

try:
    if ans[0][1]==ans[1][1]:
        ans1=-1
except:
    ans1=ans1

print(ans1)
