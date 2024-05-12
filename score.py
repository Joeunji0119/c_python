# 문제3 : 선택 구조를 사용하여 사용자가 입력한 점수를 사용하여 성적 산출 기준표에 따라 성적이 출력되는 프로그램을 작성하시오.

val = input("점수를 입력하세요:")
val = int(val)
result = ""

if val > 100:
    result = "잘못된 점수"
elif 90 <= val <= 100:
    result = "A"
elif 80 <= val <= 89:
    result = "B"
elif 70 <= val <= 79:
    result = "C"
elif 60 <= val <= 69:
    result = "D"
elif 0 <= val <= 59:
    result = "F"
elif val < 0:
    result = "잘못된 점수"
print(result,'입니다.')


def calculate_grade(score):
    if score > 100:
        return "오류: 점수가 100을 초과했습니다."
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 0:
        return "F"
    else:
        return "오류: 음수 값이 입력되었습니다."

try:
    user_score = float(input("성적을 입력하세요: "))
    grade = calculate_grade(user_score)
    print("성적:", grade)
except ValueError:
    print("오류: 올바른 숫자가 입력되지 않았습니다.")





    