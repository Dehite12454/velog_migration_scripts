오늘 포스트에서는 함수에 대해 다루어보도록 하겠다. 

함수는 intput에 대한 output을 정의하는 방식이자, 반복 계산을 수행할 때, 코드의 효율적인 공간 활용을 위해 작성한다.

### 1)return 0;
저번 main 함수에서 return 0;를 하면 프로그램이 종료되었던 것처럼 int 형 함수도 동일한 기능을 가지고 있다.

```c
#include <stdio.h>
int return_func() {
  printf("난 실행된다 \n");
  return 0;
  printf("난 안돼 ㅠㅠ \n");
}
int main() {
  return_func();
  return 0;
}
```
이를 실행하면 return_func()함수 내부에서 "난 실행된다"가 출력되고, 함수를 빠져나가게 된다.

### 2)int main()
그렇다면 메인 함수의 return 0;는 누가 받는 것일까?

정답은 운영체제이다. c언어가 실행되는 운영체제 내부에서 main 함수의 리턴값을 받고 프로그램을 종료시키는 것이다.

### 3)드디어 써먹는 포인터
앞서 배웠던 c언어의 포인터를 드디어 써먹을 때가 왔다.

아래의 코드를 보자.
```c
#include <stdio.h>
int change_val(int i) {
  i = 3;
  return 0;
}
int main() {
  int i = 0;

  printf("호출 이전 i 의 값 : %d \n", i);
  change_val(i);
  printf("호출 이후 i 의 값 : %d \n", i);

  return 0;
}#include <stdio.h>
int change_val(int i) {
  i = 3;
  return 0;
}
int main() {
  int i = 0;

  printf("호출 이전 i 의 값 : %d \n", i);
  change_val(i);
  printf("호출 이후 i 의 값 : %d \n", i);

  return 0;
}
```
이건 사실상 이상한 짓인데, int main상의 i와 int change_val 상의 i는 이름만 같지 서로 다른 메모리의 공간에 저장되어 있는 다른 i이기 때문이다.

하지만 func(int *pi)라는 함수는 어떨까?
```c
#include <stdio.h>
int change_val(int *pi) {
  printf("----- chage_val 함수 안에서 -----\n");
  printf("pi 의 값 : %p \n", pi);
  printf("pi 가 가리키는 것의 값 : %d \n", *pi);

  *pi = 3;

  printf("----- change_val 함수 끝~~ -----\n");
  return 0;
}
int main() {
  int i = 0;

  printf("i 변수의 주소값 : %p \n", &i);
  printf("호출 이전 i 의 값 : %d \n", i);
  change_val(&i);
  printf("호출 이후 i 의 값 : %d \n", i);

  return 0;
}
```
실행하면 놀랍게도 main함수 상에서 i의 값이 3으로 바뀐것을 확인 가능하다!

### 4)함수의 원형

우리는 항상 함수를 main함수 앞에 정의해야 한다고 배운다. 이는 순차적으로 코드가 실행되는 c언어 특성상, 만일 함수가 main함수 뒤에 정의되면 오류가 났을 경우 디버깅 과정에서 이를 찾기 어렵게 때문이다.

이를 방지하고자 우리는 함수의 원형을 사용하는데, 쉽게 말해서, 함수의 선언을 main함수 이전에 간단하게 해주는것이다.

```c
#include <stdio.h>
int swap(int *a, int *b);  // 이 것이 바로 함수의 원형
int main() {
  int i, j;
  i = 3;
  j = 5;
  printf("SWAP 이전 : i : %d, j : %d \n", i, j);
  swap(&i, &j);
  printf("SWAP 이후 : i : %d, j : %d \n", i, j);

  return 0;
}
int swap(int *a, int *b) {
  int temp = *a;

  *a = *b;
  *b = temp;

  return 0;
}
```
이렇게 함수의 원형을 선언하는 것으로 성공적인 컴파일을 진행할 수 있다.

주의해야 할 점은 함수의 원형을 지정할 때에는 뒤에 ;을 붙여야 한다는 점이자. 잊지 말고 실행하도록 하자.

### 5)배열을 인자로 가지는 함수
```c
#include <stdio.h>

int add_number(int *parr);
int main() {
  int arr[3];
  int i;

  /* 사용자로 부터 3 개의 원소를 입력 받는다. */
  for (i = 0; i < 3; i++) {
    scanf("%d", &arr[i]);
  }

  add_number(arr);

  printf("배열의 각 원소 : %d, %d, %d", arr[0], arr[1], arr[2]);

  return 0;
}
int add_number(int *parr) {
  int i;
  for (i = 0; i < 3; i++) {
    parr[i]++;
  }
  return 0;
}
```
위의 함수를 분석해보자. add_number 이란 함수는 ```int*```형을 인자로 가지는데 우리가 앞서 포인터를 배울 때의 기억을 떠올려 보면, 일차원 배열 arr 또한 ```int*``` 형을 가지고 있다는 사실을 알 수 있다. 따라서 parr은 arr과 똑같은 역할을 수행할 수 있다.

이처럼 함수를 정의함에 있어 포인터의 형은 매우 중요한 문제이다. 형이 맞지 않을 경우, 컴파일 시 오류가 발생하기 때문이다.

### 6)포인터의 포인터
앞선 강의에서 포인터 ```int*``` 형을 가리키는 주소를 ```int**```형이라고 배웠다. 다음의 함수를 보자.
```c
#include <stdio.h>

int pswap(int **pa, int **pb);
int main() {
  int a, b;
  int *pa, *pb;

  pa = &a;
  pb = &b;

  printf("pa 가 가리키는 변수의 주소값 : %p \n", pa);
  printf("pa 의 주소값 : %p \n \n", &pa);
  printf("pb 가 가리키는 변수의 주소값 : %p \n", pb);
  printf("pb 의 주소값 : %p \n", &pb);

  printf(" ------------- 호출 -------------- \n");
  pswap(&pa, &pb);
  printf(" ------------- 호출끝 -------------- \n");

  printf("pa 가 가리키는 변수의 주소값 : %p \n", pa);
  printf("pa 의 주소값 : %p \n \n", &pa);
  printf("pb 가 가리키는 변수의 주소값 : %p \n", pb);
  printf("pb 의 주소값 : %p \n", &pb);
  return 0;
}
int pswap(int **ppa, int **ppb) {
  int *temp = *ppa;

  printf("ppa 가 가리키는 변수의 주소값 : %p \n", ppa);
  printf("ppb 가 가리키는 변수의 주소값 : %p \n", ppb);

  *ppa = *ppb;
  *ppb = temp;

  return 0;
}
```
여기서 pswap 안의 내용을 살펴보자. pswap은 ```int**```형을 인자로 받는다. a의 주소값이 pa의 주소값을 인자로 받아야 하니, 이는 당연한 일이다.

다음 내용이 중요한데, ```int*```형의 temp를 설정해서 ```*ppa```를 받고 있다.즉 temp = pa인 것이다. 이 함수에서 ppa 에 pb를 할당하고, ppb에 pa를 할당하므로 결과적으로 pa가 b, pb가 a를 가리키게 된다. 실행해보자.

### 7)이차원 배열을 인자로 가지는 함수
다음 함수를 분석하자.
```c
#include <stdio.h>
/* 열의 개수가 2 개인 이차원 배열과, 총 행의 수를 인자로 받는다. */
int add1_element(int (*arr)[2], int row);
int main() {
  int arr[3][2];
  int i, j;

  for (i = 0; i < 3; i++) {
    for (j = 0; j < 2; j++) {
      scanf("%d", &arr[i][j]);
    }
  }

  add1_element(arr, 3);

  for (i = 0; i < 3; i++) {
    for (j = 0; j < 2; j++) {
      printf("arr[%d][%d] : %d \n", i, j, arr[i][j]);
    }
  }
  return 0;
}
int add1_element(int (*arr)[2], int row) {
  int i, j;
  for (i = 0; i < row; i++) {
    for (j = 0; j < 2; j++) {
      arr[i][j]++;
    }
  }

  return 0;
}
```
앞서 포인터의 형에서 정의한대로, 이차원 배열에서 arr값은 arr[0], 즉 한 행을 형으로 가진다.위의 경우엔 ```int*[2]```을 형으로 가지는 것이다. 따라서 함수를 정의할 때 인자로 ```int (*arr)[2]```라고 ```int*[2]```형의 arr 포인터를 정의한 것은 잘한 일이다.

이때 인자로 정의한 arr은 함수 내부의 완전히 다른 포인터이다. main 함수 안에서 arr은 arr[0]을 가리키는 주소이므로 이를 받는 과정에서 자연스럽게 다음의 관계가 성립한다.
arr(함수내부) = arr(main함수);
즉, 함수 내부에서 arr[i][j]로 메인 함수의 arr로 접근이 가능하다는 뜻이다.

이것이 이차원 배열을 함수의 인자로 받는 방법이다.

오직 함수에 관해서 ```int*[2]```형 포인터를 간단하게 정의할 수 있는데 이는 다음과 같다.
```c
int add1_element(int arr[][2], int row)
```
오직, 함수에서만 이런 편의성을 제공하니, 다른 경우에 쓸일이 없도록 하자.

### 8)상수인 함수
```c
#include <stdio.h>
int read_val(const int val);
int main() {
  int a;
  scanf("%d", &a);
  read_val(a);
  return 0;
}
int read_val(const int val) {
  val = 5;  // 허용되지 않는다.
  return 0;
}
```
위의 코드에서 val은 const int로 선언되면서 a의 값을 가지게 되었다. 즉 val = 5는 const값을 바꾼다는 의미이므로 컴파일 과정에서 오류가 선언되게 된다.

### 9)함수의 포인터
함수에도 포인터가 존재한다. 이는 신기한 생각인데 생각해보면 당연하다.

코드가 실행될 때, 함수의 시작 지점을 가리키는 메모리상의 정보가 존재할 것이다. 그렇다면 이를 가리키는 주소를 함수의 포인터라고 할 수 있는 것이다.

보통 함수의 이름이, 함수의 포인터 역할을 하게 된다. 다음의 코드를 보자.
```c
#include <stdio.h>

int max(int a, int b);
int main() {
  int a, b;
  int (*pmax)(int, int);
  pmax = max;

  scanf("%d %d", &a, &b);
  printf("max(a,b) : %d \n", max(a, b));
  printf("pmax(a,b) : %d \n", pmax(a, b));

  return 0;
}
int max(int a, int b) {
  if (a > b)
    return a;
  else
    return b;

  return 0;
}
```
```int (*pmax)(int, int);```부분을 보자. 여기서 새로운 포인터의 형이 출현한다. 이는 max함수의 int,int인자를 그대로 가지고 있고, int값을 리턴한다는 사실도 명시되어 있다.

따라서 pmax는 max와 포인터의 형이 같으므로 pmax = max를 통해 pmax가 max를 향하도록 만들 수 있다.

앞서 ```int*[3]```형을 인자로 받았던 이차원 배열의 함수는 형을 어떻게 표시할까?
```int (*pfunc)(int (*)[3], int);```
위의 예시처럼 그냥 인자 형에 ```int (*)[3]```라고 명시한 것을 볼 수 있다.

즉 포인터를 인자로 받는 함수의 형을 나타낼 때, 인자로 위의 예시처럼 입력하면 잘 작동하는 것이다.

---
### 총평
포인터를 활용한 함수의 정의까지 마쳤으므로, 함수에 대한 기본적인 이야기는 여기서 마무리를 짓도록 하겠다.

다음 포스팅은 이를 활용한 여러가지 문제들의 풀이이다.

***피드백, 틀린 개념의 지적은 언제나 환영입니다.***