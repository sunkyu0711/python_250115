def rectArea(width,depth):
    return width*depth

def triArea(base,height):
    return base*height/2


if __name__ == '__main__': 
    # 의미: 이 함수를 호출할 때 만들어져 있는 곳에서 호출할 때만 if 문 실행, 즉 아래 설명이 먹히지 않음!
    # ipynb 파일로 옮겨 가며 테스트하지 않아도 될 것 같음
    print(f'사각형의 넓이 = {rectArea(5,10)}')
    print(f'삼각형의 넓이 = {triArea(5,10)}')
    # 이러면 import해서 사용하면 처음에 이 두 개 프린트된 결과가 나온 뒤에 실행 결과 나옴. 이게 안 되려면?
