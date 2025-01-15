# [9일 차 문제2] 피자와 음료수를 주문한 뒤 영수증을 출력하는 프로그램을 모듈을 이용하여 만들어 보세요.
# 아래는 출력 결과
# ===...: 얘는 첫 줄에만
# 주문 내역:
# - 치즈 피자 (3200원) x 2 = 총 가격
# - ...
# 총 금액: ... 원: 얘는 피자와 음료수를 각각 구분할 것

from pizzaorder import *

pmenu, porder=Pizza()
dmenu, dorder=Drink()

pizza_price=0
print('='*25)
print('주문 내역:')
for pizza in porder:
    print(f'- {pizza} ({pmenu[pizza]}원) x {porder[pizza]} = {int(pmenu[pizza])*int(porder[pizza])}원')
    pizza_price=pizza_price+(int(pmenu[pizza])*int(porder[pizza]))

print(f'총 금액: {pizza_price}원')


drink_price=0
print('주문 내역:')
for drink in dorder:
    print(f'- {drink} ({dmenu[drink]}원) x {dorder[drink]} = {int(dmenu[drink])*int(dorder[drink])}원')
    drink_price=drink_price+(int(dmenu[drink])*int(dorder[drink]))
print(f'총 금액: {drink_price}원')