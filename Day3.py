"""
최빈값 구하기

최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 
최빈값이 여러 개면 -1을 return 합니다.
"""

from collections import Counter

def solution(array):
    cnt = Counter(array)
    ans = cnt.most_common()
    ans1=ans[0][0]
    
    try:
        if ans[0][1]==ans[1][1]:
            ans1=-1
    except:
        ans1=ans1
    
    return ans1