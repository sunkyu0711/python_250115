# [9일 차 문제2] 피자와 음료수를 주문한 뒤 영수증을 출력하는 프로그램을 모듈을 이용하여 만들어 보세요.
# 여러 줄 탭 키 지우기 - 드래그 후 shift+tab
# 중요 - 아래 코드는 모범 답안과 엮은 결과: 중복을 줄이려는 노력을 해야!

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

print(f'\n전체 가격: {pizza_price+drink_price:,}원')