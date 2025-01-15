# visual studio code에서 py는 실행용
# print('김선규')
# print(60+89)

import polyArea

print('사각형 넓이 계산')
width=float(input("넓이를 구하고자 하는 사각형의 가로(㎝)의 길이를 입력하세요. "))
depth=float(input("넓이를 구하고자 하는 사각형의 세로(㎝)의 길이를 입력하세요. "))
print(f'구하고자 하는 사각형의 넓이는 {polyArea.rectArea(width,depth)}㎠입니다.')

print('삼각형 넓이 계산')
base=float(input("넓이를 구하고자 하는 삼각형의 밑변(㎝)의 길이를 입력하세요. "))
height=float(input("넓이를 구하고자 하는 삼각형의 높이(㎝)의 길이를 입력하세요. "))
print(f'구하고자 하는 삼각형의 넓이는 {polyArea.triArea(base,height)}㎠입니다.')