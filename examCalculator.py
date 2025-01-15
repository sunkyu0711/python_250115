# [9일 차 문제1] 사용자가 3과목의 시험 점수를 입력하면 총점, 평균, 통과 여부를 출력하는 프로그램을 모듈을 이용해서 만들어 봅시다.

def total(score1,score2,score3):
    return score1+score2+score3

def average(score1,score2,score3):
    return total(score1,score2,score3)/3

def passfail(score1,score2,score3):
    if average(score1,score2,score3)>=60 and score1>=40 and score2>=40 and score3>=40:
        return "Pass"
    else:
        return "Fail"
    
if __name__=='__main__':
    print(total(100,34,56))