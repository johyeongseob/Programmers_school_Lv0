"""
피자 나눠 먹기 (1)

머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다.
피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
"""

def solution(n):
    if n%7==0:
        answer=n//7
    else:
        answer=n//7+1
    return answer

"""
피자 나눠 먹기 (2)

머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 
피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 
최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
"""

def solution(n):
    answer=10
    for i in range(1,601):
        if i%6 ==0 and i%n==0:
            answer=i/6
            break
    return answer  

#other solution

def solution(n):
    answer = 1
    while 6 * answer % n:
        answer += 1
    return answer

"""
피자 나눠 먹기 (3)

머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다. 
피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, 
n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
"""

def solution(slice, n):
    answer=0
    if n%slice ==0:
        answer=n/slice
    else:
        answer=n//slice+1
    return answer

# better solution

def solution(slice, n):
    return ((n - 1) // slice) + 1

