저번 포스트에 이어서 string에 관해서 더욱 깊게 다루어 보도록 하겠다.

### 1) 문자열 literal 에 대한 이해

아래의 코드를 실행시켜보자.

```c
#include <stdio.h>
int main() {
  char str[] = "sentence";
  char *pstr = "sentence";

  printf("str : %s \n", str);
  printf("pstr : %s \n", pstr);

  return 0;
}
```
성공적으로 컴파일 하면
```
str : sentence 
pstr : sentence
```
이 출력된다. 첫번째 초기화는 우리에게 익숙한, 칸이 지정되있지 않은 배열로서 string의 선언이다. 그렇다면 두번째 선언은 왜 말이 되는 것일까?

바로 "sentence"는 , "sentence" 라는 문자열이 저장된 주소값 (시작 주소값) 을 의미하기 때문이다. 따라서 포인터 pstr을 통해 지정할 수 있는 것이다.

우리의 상식과는 맞지 않는 기묘한 존재이다.

이를 이해하기 위해서는 프로그래밍 상에서 literal에 대한 의미를 집고 넘어가야 한다.

literal은 소스코드 상에서 고정된 값을 가지는 것들을 일컫는다. C언어 에서 큰 따옴표로 묶이는 것들을 문자열 literal이라고 말한다.

```
char *pstr = "goodbye";
printf("why so serious?");
scanf("%c", str[0]);
```
위의 세가지 경우 모두 프로그램 상에서 literal이라고 저장되며, 프로그램은 이러한 literal들을 따로 모아서 저장해둔다.

여기서 중요한 점은 literal은 절대 변경되지 말아야 하는 값이라는 것이다. 따라서 string값을 변경하려고 시도하면 오류가 뜨는것을 볼 수 있다.

```c
char *pstr = "goodbye";
pstr[1] = 'a';
```
위와 같은 코드를 실행하면 오류가 뜨는것을 볼 수 있다.

하지만 앞서 설정한 배열을 어떠한가?

```c
char str[] = "hello";
```
이 배열은 literal이라고 보기 애매하다. 배열 내부에 한글자씩 일려로 들어가기 때문이다. 이는 텍스트 세그먼트가 아니라 스택 저장공간에 들어가기 때문에 임의대로 수정이 가능하다.

참고적으로 VS 2017 이상에서는 리터럴을 char* 가 가리킬 수 없다. 반드시 const char* 가 가리켜야 하며, 덕분에 리터럴을 수정하는 괴랄한 짓을 컴파일 단에서 막을 수 있다.

### 2) c언어에서 문자열 편집하기

c언어에서 문자열은 생각보다 자유롭지 못한 자료형이다.

예를 들어 다음 코드들을 보자.
```c
char str1[] = {"abc"};
char str2[] = {"def"};
str1 = str1 + str2;
if (str1 == str2) 
if (str1 == "abc") 
```
위의 문장들은 전부 비문인데, 이는 당연한 일이다. 결국 str1, str2는 각각 주소값을 나타내고 "abc"또한 literal이므로 주소값을 의미한다. 따라서 이는 각각의 주소값을 비교하는 문장이 되버리는 것이다.

따라서 c언어 내부에서 문자열을 다루려면 이를 위한 함수를 따로 만들어야 한다.

> 문자열 내의 총 문자의 수를 세는 함수

이는 저번 시간에 다루었던 내용이다. 다음의 코드를 참고하자.
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

> 문자열을 복사하는 함수

다음과 같은 코드를 보자.

```c
char str[100];
str = "abcdefg";
```
우리는 literal을 배웠으므로 위의 코드가 무엇이 틀렸는지 정확하게 알 수 있다.

str 주소값과 literal의 주소값을 비교하고 있으므로 컴파일 오류가 뜨는 것이다.

그렇다면 이 코드는 어떨까?

```c
char str[100] = "abcdefg";
```

위의 코드가 말이 되는 이유는 사용자의 편의성을 위해서이다.

**오직 배열을 정의할 때만 위의 방식을 사용할 수 있다. 기억하자.**

우리는 이제 왜 문자열을 카피하기 위해서 새로운 함수까지 정의해야 하는 이유를 알 수 있다.

문자열 a,b를 받아서 b의 문자열을 a로 복사하고 싶으므로, 함수의 인자는 ```char *()``` 형으로 두개를 받으면 좋다.

또한 정확히 실행되었을 때, 1을 리턴하도록 만들고 싶다. 이를 구현하면 다음과 같다.

```c
int copy_str(char *dest, char *src) {
  while (*src) {
    *dest = *src;
    src++;  // 그 다음 문자를 가리킨다.
    dest++;
  }
  *dest = '\0';

  return 1;
}
```

포인터의 특성을 사용해서 src의 문자열을 dest 문자열로 복사하고 있다. 이때 중요한 점은 dest의 배열 크기가 src보다 커야 하고, 마지막 부분에 ```'\0'``` 을 추가하는 것을 잊지 않는 것이다.

> 문자열을 합치는 함수 (즉 더하는)

문자열끼리 더하는 함수도 위와 같은 방식으로 설정 가능하다.

```c
#include <stdio.h>
int stradd(char *dest, char *src);
int main() {
  char str1[100] = "hello my name is ";
  char str2[] = "Psi";

  printf("합치기 이전 : %s \n", str1);

  stradd(str1, str2);

  printf("합친 이후 : %s \n", str1);

  return 0;
}
int stradd(char *dest, char *src) {
  /* dest 의 끝 부분을 찾는다.*/
  while (*dest) {
    dest++;
  }

  /*
  while 문을 지나고 나면 dest 는 dest 문자열의 NULL 문자를 가리키고 있게 된다.
  이제 src 의 문자열들을 dest 의 NULL 문자 있는 곳 부터 복사해넣는다.
  */
  while (*src) {
    *dest = *src;
    src++;
    dest++;
  }

  /* 마지막으로 dest 에 NULL 추가 (왜냐하면 src 에서 NULL 이 추가 되지
   * 않았으므로) */
  *dest = '\0';

  return 1;
}
```

> 문자열을 비교하는 함수

문자열을 비교하는 함수는 다음과 같다.

```c
int compare(char *str1, char *str2) {
  while (*str1) {
    if (*str1 != *str2) {
      return 0;
    }

    str1++;
    str2++;
  }

  if (*str2 == '\0') return 1;

  return 0;
}
```
위의 코드의 매커니즘은 간단하다. 먼저 str1과 str2의 인자들을 하나씩 비교해 가며 틀린 부분이 있으면 0을 리턴한다.

만약 위의 과정속에서 문제가 없으면 경우는 둘중 하나이다.

str1이 str2와 같다.

아니면, str2가 str1보다 길이가 길어서 str1을 포함하고 있는 경우이다.

이를 판별하기 위해서 str2의 포인터가 null을 가리키는지 여부를 검사한다.

---
### 총평

문자열에 관한 기본적인 내용들은 여기서 마치도록 하겠다.

다음 포스트부터는 문자열을 사용하는 문제풀이에 대한 풀이가 올라갈 예정이다.

#### 틀린 부분에 대한 비판 및 피드백은 언제나 환영입니다. ^^