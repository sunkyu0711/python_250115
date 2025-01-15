# [9일 차 문제2] 피자와 음료수를 주문한 뒤 영수증을 출력하는 프로그램을 모듈을 이용하여 만들어 보세요.
# 아래는 출력 결과
# ===...: 얘는 첫 줄에만
# 주문 내역:
# - 치즈 피자 (3200원) x 2 = 총 가격
# - ...
# 총 금액: ... 원: 얘는 피자와 음료수를 각각 구분할 것

from pizzaorder import *

pizza_menu={'페퍼로니 피자':3000,
            '치즈 피자':3200,
            '콤비네이션 피자':3500,
            '불고기 피자':3600,
            '해산물 피자':3800}
drink_menu={'콜라':1500,
            '사이다':1500,
            '생수':1000}

pizza_order = Order(pizza_menu,'피자')
print(pizza_order)
drink_order = Order(drink_menu,'음료수')
print(drink_order)

pizza_price=Money(pizza_order,pizza_menu,'피자')
drink_price=Money(drink_order,drink_menu,'음료수')

print(f'전체 가격: {pizza_price+drink_price:,}원')