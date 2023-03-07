"""
머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
"""

def solution(price):
    answer=0
    if price >= 500000:
        answer=price*0.8
    elif price >= 300000:
        answer=price*0.9
    elif price >= 100000:
        answer=price*0.95
    else:
        answer=price
    
    return int(answer)

# other solution

def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
        

"""
머쓱이는 추운 날에도 아이스 아메리카노만 마십니다.
아이스 아메리카노는 한잔에 5,500원입니다.
머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 
머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 
순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""

def solution(money):
    cup= money//5500
    changes=money-cup*5500
    answer = [cup, changes]
    return answer


"""
정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(num_list):
    answer = num_list[::-1]
    
    return answer

#other solution

def solution(num_list):
    num_list.reverse()
    return num_list