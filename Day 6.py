"""
문자열 my_string이 매개변수로 주어집니다. 
my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(my_string):
    answer = my_string[::-1]
    return answer

#other solution

def solution(my_string):
    return ''.join(list(reversed(my_string)))

"""
"*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 삼각형을 그리려고 합니다.
정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.
"""

