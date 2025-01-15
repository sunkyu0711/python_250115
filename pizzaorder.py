# [9일 차 문제2] 피자와 음료수를 주문한 뒤 영수증을 출력하는 프로그램을 모듈을 이용하여 만들어 보세요.
# 여러 줄 탭 키 지우기 - 드래그 후 shift+tab
# 아래 코드는 모범 답안과 엮은 결과: 중복을 줄이려는 노력을 해야!

def Order(menu,name):
    print(f'\n다음은 {name} 메뉴입니다.')
    for selection in menu: # or for name, price in menu.items():
        print(f'{selection} ({menu[selection]:,}원)')
    
    order={}

    while True:
        menu_selection=input(f'주문할 {name}를 입력하세요(종료는 exit): ')
        if menu_selection=='exit':
            break
        else:
            num_selection=int(input('수량을 입력하세요: '))
            order[menu_selection]=num_selection

    return order

def Money(order,menu,name):
    price=0
    print('='*25)
    print(f'{name} 주문 내역:')
    for i in order.keys():
        if i in menu.keys():
            price=price+(order[i]*menu[i])
        print(f'- {i} ({menu[i]:,}원) x {order[i]} = {menu[i]*order[i]:,}원')
    print(f'주문한 {name}의 총 금액: {price:,}원')
    return price