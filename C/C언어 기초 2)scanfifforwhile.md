# C언어 기초
이번 포스팅에는 scanf, if, for, while 구문에서 쉽게 실수 할 수 있는 부분들에 관해 다뤄보려고 한다. 또한 씹어먹는 C언어의 진도에 맞춰서 해당 교재에 수록된 문제들 중 중상 이상의 난이도만 솔루션을 풀이할 것이다.

### 1) Scanf
---
scanf에 관해서 다루기 전, 먼저 아스키 코드에 관해 간략하게 다루도록 하겠다. 아스키 코드는 char 자료형을 지정할 때, 컴퓨터가 이를 저장하는 방식으로, 문자를 숫자와 병렬 매칭해서 저장하는 특징을 가지고 있다.
```
char a;
a = 'a';
printf("a has number %d, and alphabet %c\n",a,a);
```
다음과 같은 코드를 실행했다고 가정할 때, 아스키 코드 상으로 소문자 알파벳 a는 97이랑 동치라는 사실을 알 수 있다. 참고)대문자 A는 65이다. 각자 알파벳이 a,b,c 올라갈수록 숫자가 하나씩 증가한다.(암기해두는 편이 나중에 용이하다!)

이제 기본적인 scanf 문법으로 들어가보자. scanf는 printf 와 달리 자료형 마다 문법이 전부 다르므로 이에 유의해서 사용할 필요가 있다. 섭씨 온도를 화씨 온도로 바꾸어주는 다음 코드를 확인하자.
```
#include <stdio.h>
int main(){
double celsius;
printf("섭씨온도는? :");
scanf("%lf",&celsius); 
printf("그렇다면 화씨온도는 %f이다.\n",9*celsius/5 +32);
return 0;
}
```
scanf는 double과 float 자료형을 입력받는 방식이 다르다. double은 %lf float는 %f이다. char은 %c, long은 %ld short는 %hd이다. 참고하자.

### 2) if
---
for문 내부에는 break continue 처럼 코드의 흐름을 통제할 수 있는 수단이 갖추어져 있다. if 문에서도 이와 유사하게 역할을 하는 방법이 존재한다. 다음 코드를 참고하자.
```
int b = 1;
if (b==0){
    printf("b is 0\n");
    return 0;
}
printf("b is not 0\n");
```
이렇게 if문 안에 return 0를 넣어서 프로그램을 종료시킬 수 있다. 마치 for문의 break와 유사하지 않은가?

else if 구문을 사용할 때, 쉽게 실수할 수 있는 부분이 존재한다. 다음 코드를 보자.
```
int num = 7;
if (num == 7) {
	printf("a 행운의 숫자 7 이군요!\n");
} else if (num == 7) {
	printf("b 행운의 숫자 7 이군요! \n");
}
```
이처럼 else if는 if가 아닐때를 전제조건으로 가지므로 if를 만족하면 건너뛰어진다. 실행해보면 if문 안의 printf만 실행되는것을 볼 수 있다.

다음으로 볼것은 short circuit evaluation이라는 조건문의 특징이다.
```
int height = 170;
int weight;
if (height >= 180 && weight >= 90) {
    printf("you are so small\n");
}
```
위와 같이 실행하면 조건문 &&의 특징으로, 앞의 조건이 거짓이면 뒤의 조건을 무시하고 지나가게 된다. 이는 계산의 편의성을 위한 것으로 컴퓨터의 이런 특징을 short circuit evaluation이라 명명한다. 따라서 weight변수값이 정의되지 않았는데, 오류가 발생하지 않는 것을 볼 수 있다.

for 과 while문은 교재 상으로 실수할 수 있는 부분이 보이지 않으므로 다음 포스트로 넘어가도록 하겠다.