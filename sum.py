# 문제2 : 순차 구조를 사용하여 0과 1000 사이의 정수를 사용자로부터 입력받아 다음과 같이 각 자릿수의 합을 출력하는 프로그램을 구하시오.

val = input("0과 1000사이의 정수를 입력하세요:")
total = 0
for i in val:
    total = int(i)+total

print(total)