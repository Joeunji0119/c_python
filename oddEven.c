#include <stdio.h>

#define even(a) (a % 2 == 0)
#define range(a) (5<= a && a<=10)

int main() {
    int jo_eunji;
    

    while(1){
        printf("\n 5부터 10 사이의 짝수를 입력하시오: ");
        scanf("%d", &jo_eunji);

        if(jo_eunji == 0){
            printf("♥프로그램을 종료합니다. 이름 : 조은지.");
            return 0;
        }

        if(even(jo_eunji) && !range(jo_eunji)){
            printf("☆ 5부터 10 사이의 짝수를 입력하시오. 학과 : 컴퓨터과학과");
        }
        if(!even(jo_eunji)){
            printf("★ 짝수를 입력하시오. 학번: 202434-364741");
        }
        if(even(jo_eunji) && range(jo_eunji)){
            printf("입력한 숫자 %d은 5부터 10사이의 짝수입니다.",jo_eunji);
        }
    }
};