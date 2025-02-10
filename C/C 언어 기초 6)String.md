이번 포스팅에서는 문자열, 즉 string에 대하여 알아볼 것이다.

### 1) null 종료 문자열
문자열을 선언하는 방법은 다음과 같다.

```c
char sentence[4] = {"pdh"};
char sentence2[4] = {'p','d','h','\0'};
```
이처럼 pdh 라는 string을 출력하려면 컴퓨터에게 문자열의 길이를 알려줘야 한다.

하지만 매번 출력할 때마다 이를 알려주기 귀찮으므로 문자열의 종료 부분에 null 값을 지정함으로서 이를 간편화 한것이다.

null은 아스키 코드값이 0으로, 정수 0과 구별해야 한다.

null의 표현은 다음과 같다.

```'\0', 0, (char)NULL```

이처럼 3칸짜리 string을 4칸짜리 배열에 정의하는 이유는 끝에 null값이 들어가야 하기 때문이다.

다음의 코드를 분석하자.

```c
#include <stdio.h>
int main() {
  char sentence_1[4] = {'P', 's', 'i', '\0'};
  char sentence_2[4] = {'P', 's', 'i', 0};
  char sentence_3[4] = {'P', 's', 'i', (char)NULL};
  char sentence_4[4] = {"Psi"};

  printf("sentence_1 : %s \n", sentence_1);  // %s 를 통해서 문자열을 출력한다.
  printf("sentence_2 : %s \n", sentence_2);
  printf("sentence_3 : %s \n", sentence_3);
  printf("sentence_4 : %s \n", sentence_4);

  return 0;
}
```
위의 코드를 보면 모두 4칸짜리 배열을 정의하고 있는 것을 볼 수 있다. 이는 흔하게 실수 할 수 있는 부분이니, 유의하도록 하자.

밑의 printf 함수를 보자. 우리는 새로운 출력 함수를 배우게 된다. %s는 string 형태의 자료형을 받을 때 쓴다는 것을 알 수 있다. sentence_4는 해당 배열의 시작점을 의미한다.

%c는 한 문자만을 출력하지만, %s는 null값이 나올 때까지 계속해서 출력을 진행한다.

***"" 와 ''의 차이점***

''은 문자열 한개를 지정할 때 사용한다. ""은 한 개 이상의 문자열을 지정할 때 사용된다.

예를 들어 'abc'는 틀린 표현이고, "a"은 맞는 표현이다.

### 2) 문자열의 개수를 세자.

다음의 코드를 보자.

```c
#include <stdio.h>
int str_length(char *str);
int main() {
  char str[] = {"What is your name?"};

  printf("이 문자열의 길이 : %d \n", str_length(str));

  return 0;
}
int str_length(char *str) {
  int i = 0;
  while (str[i]) {
    i++;
  }

  return i;
}
```
빈칸을 제외한 숫자를 세고 싶으므로 while(srt[i])라는 아이디어를 통해서 마지막 null 값이 0이므로 while(0)까지의 반복 횟수를 세는 코드이다.

해당 아이디어를 잘 기억해두자.

### 3) 문자열 입력받기

다음의 코드를 보자.
```c
#include <stdio.h>
int main() {
  char words[30];

  printf("30 자 이내의 문자열을 입력해주세요! : ");
  scanf("%s", words);

  printf("문자열 : %s \n", words);

  return 0;
}
```
words는 29칸의 string을 받을 수 있는 배열이다.

scanf는 뒤에 포인터를 통해서 저장위치를 명시해줘야 하지만 이는 words라는 이름 자체가 해당 배열의 포인터와 같으므로 해결된다.

여기서 포인트는 sdfsdfsd 같은 연속된 string은 scanf를 통해 잘 받아지지만, what is your name 처럼 띄어쓰기가 존재하면 name만 받아진다는 사실이다.

이에 대해서는 추후 서술할 예정이다.