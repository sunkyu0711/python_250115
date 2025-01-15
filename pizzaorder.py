# [9일 차 문제2] 피자와 음료수를 주문한 뒤 영수증을 출력하는 프로그램을 모듈을 이용하여 만들어 보세요.

def Pizza():
    pizza_menu={'페퍼로니 피자':'3000',
                '치즈 피자':'3200',
                '콤비네이션 피자':'3500',
                '불고기 피자':'3600',
                '해산물 피자':'3800'}
    print('다음은 피자 메뉴입니다.')
    for pizza in pizza_menu:
        print(f'{pizza} ({pizza_menu[pizza]} 원)')
    
    pizza_order={}

    while True:
        pizza_menu_selection=input('주문할 메뉴를 입력하세요(종료는 exit): ')
        if pizza_menu_selection=='exit':
            break
        else:
            pizza_num_selection=int(input('수량을 입력하세요: '))
            pizza_order[pizza_menu_selection]=pizza_num_selection

    return pizza_menu, pizza_order

def Drink():
    drink_menu={'콜라':'1500',
                '사이다':'1500',
                '생수':'1000'}
    print('다음은 음료수 메뉴입니다.')
    for drink in drink_menu:
        print(f'{drink} ({drink_menu[drink]} 원)')
    
    drink_order={}

    while True:
        drink_menu_selection=input('주문할 메뉴를 입력하세요(종료는 exit): ')
        if drink_menu_selection=='exit':
            break
        else:
            drink_num_selection=int(input('수량을 입력하세요: '))
            drink_order[drink_menu_selection]=drink_num_selection

    return drink_menu, drink_order

if __name__=='__main__':
    Pizza()
    Drink()

# if __name__=='__main__':
#     pmenu, porder=Pizza()
#     dmenu, dorder=Drink()

#     pizza_price=0
#     print('='*25)
#     print('주문 내역:')
#     for pizza in porder:
#         print(f'- {pizza} ({pmenu[pizza]}원) x {porder[pizza]} = {int(pmenu[pizza])*int(porder[pizza])}원')
#         pizza_price=pizza_price+(int(pmenu[pizza])*int(porder[pizza]))

#     print(f'총 금액: {pizza_price}원')


    # drink_price=0
    # print('주문 내역:')
    # for drink in dorder:
    #     print(f'- {drink} ({dmenu[drink]}원) x {dorder[drink]} = {int(dmenu[drink])*int(dorder[drink])}원')
    #     drink_price=drink_price+(int(dmenu[drink])*int(dorder[drink]))
    # print(f'총 금액: {drink_price}원')