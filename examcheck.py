# [9일 차 문제1] 사용자가 3과목의 시험 점수를 입력하면 총점, 평균, 통과 여부를 출력하는 프로그램을 모듈을 이용해서 만들어 봅시다.

# import examCalculator as eCal: 이거는 줄인모듈명.함수명으로 써야
# import examCalculator: 이거는 풀네임
from examCalculator import * # 이거는 함수명만 써도 됨

print("\n시험 점수 계산 프로그램에 오신 걸 환영합니다!")
s1=float(input("첫 번째 과목의 점수를 입력하세요. "))
s2=float(input("두 번째 과목의 점수를 입력하세요. "))
s3=float(input("세 번째 과목의 점수를 입력하세요. "))

sum=total(s1,s2,s3)
avg=average(s1,s2,s3)
pf=passfail(s1,s2,s3)

print('\n입력이 완료되었습니다! 분석 결과를 확인해 주세요.')
print(f'총점: {sum}점')
print(f'평균: {avg}점')
print(f'통과 여부(Pass: 통과, Fail: 낙제): {pf}')