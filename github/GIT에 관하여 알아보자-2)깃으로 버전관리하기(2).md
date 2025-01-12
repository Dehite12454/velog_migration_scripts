# 깃으로 버전관리하기(2)
---
### 3. 브랜치란 무엇일까
---
영어로 가지 라는 의미를 가지고 있는 브랜치는 깃 버전관리에서 가지와 같은 역할을 수행한다고 정의 가능하다. 앞서 배웠던 스테이징과 커밋이 단방향 기록의 성질을 띄고 있다면, 이 log 를 입체적으로 만들어주는 역할이 브랜치라고 볼 수 있다. 

쉽게 말해서 main 브랜치에 커밋을 계속하다가, 특별한 기능을 추가하고 싶을 때 서브로 a라는 브랜치를 만들어서 개발을 시작하는 것이다. a는 만든 시점의 main 코드를 전부 공유하고 있으며, a에 커밋한 수정사항은 main에 기록이 되지 않는다. 마치 가지가 분리해 나오듯이 온전히 별개의 개발공간을 구축하는 것이다.

이처럼 브랜치를 분리해서 작업하다가, 필요할 경우 main 코드에 병합도 가능하다. 이 경우 main과 a는 서로 동일한 부분은 유지하면서 변동사항만 합집합으로 가져가게 된다. 브랜치는 생성과 병합을 반복하며, 유사시 버전에 따라 코드를 분리하기 위해서 존재하게 된다.

![](https://velog.velcdn.com/images/dehite0704/post/777727fe-604d-408d-9244-930b5472e181/image.png)
출처: <https://6mini.github.io/git/2022/06/12/branch/>

### 브랜치 만들기 및 병합하기
---
새로운 브랜치를 만드는 명령은 다음과 같다.
```
git branch a
```
이는 새로운 브랜치 a를 만들라는 뜻이다. git branch 명령어를 쓰며 현재 만들어진 브랜치를 전부 확인 가능하다.
```
CKIRUser@W43142 MINGW64 ~/git_home (master)
$ git branch
  a
* master
```
이처럼 a, master(main) 두 개의 브랜치가 존재하는 것을 알 수 있다. 별표가 붙은 브랜치는 현재 작업공간을 나타낸다. t2.txt 파일을 추가해서 b를 입력하고 저장 후 커밋하자. 앞서 배웠던 내용을 통해 우리는 master branch에만 커밋이 올라가고 a에는 올라가지 않았을 것이라 유추 가능하다. git log --oneline을 통해 log를 조회해보자.
```
CKIRUser@W43142 MINGW64 ~/git_home (master)
$ git log --oneline
5bc8d92 (HEAD -> master) message2
2cc073c (a) message1
```
위에서 보이는 대로 HEAD(현재 작업공간)에서 추가한 최신 커밋은 master에만 반영되고 a는 message1커밋이 최신 커밋이라는 사실을 알 수 있다. 이번엔 a에서 작업을 진행해보자.
```
git switch a
```
위의 명령을 통해 작업공간을 a branch로 변경하였다. t3 파일을 만들어 c를 저장하고 커밋하자.
```
git log --oneline --branches
```
명령어로 log를 브랜치와 함께 간단하게 표시 가능하다.
```
CKIRUser@W43142 MINGW64 ~/git_home (a)
$ git log --oneline --branches
19f6130 (HEAD -> a) message3
5bc8d92 (master) message2
2cc073c message1
```
이처럼 a 브랜치는 master과 다른 최신 커밋 message3를 가진다는 사실을 알 수 있다.

브랜치들 사이의 차이점을 명확히 알고 있어야 나중에 병합시 예상치 못한 오류를 방지할 수 있다. 
```
git log main..a
```
명령어를 통해 main 에는 없고 a 에는 있는 커밋을 볼 수 있다. 이렇게 차이점을 인지한 후 병합을 수행한다. 병합시  HEAD는 main에 위치해야 하므로 main 브랜치로 넘어가자.
```
git switch master
```
master branch 기준으로 a branch를 병합하려면 다음과 같이 입력해야 한다.
```
git merge a
```
![](https://velog.velcdn.com/images/dehite0704/post/d3a0837d-9e86-4a92-8652-4008c3664f63/image.png)
위의 사진처럼 master branch의 t2파일과 a branch의 t3 파일이 병합되어서 새로운 버전의 master branch를 구성했음을 파악 가능하다.

추가적으로 병합과정에서 a 브랜치의 모든 변경사항을 합치는 것이 아닌, 특정 커밋만 선택적으로 병합할 수 있다. cherry-pick이라고 불리는 이 방법은 매우 유용하니 까먹지 않도록 하자.

branch a에 t3, t4두개의 파일을 저장했다고 가정하자. 이때 master branch로 넘어와서 병합할 때 t3 파일만 병합하고 싶다. 먼저 t3파일 커밋 해시를 복사하고, 다음과 같이 입력하자.
```
git cherry-pick 복사한-커밋해시
```
master branch에 t3 파일만 추가된 사실을 발견할 수 있다.

### 정리
---
깃으로 버전관리하기 1), 2)에서 다음과 같은 사실들을 배웠다.
- 스테이징과 커밋
- 브랜치

이를 통해 깃을 통한 가장 기본적인 버전관리를 수행할 수 있는 능력을 갖추었다.

다음 포스트에서는 깃허브의 원격 저장소를 컴퓨터의 지역 저장소와 연결하여 원격 버전관리를 하는 방식과, 깃허브를 통해 여러 개발자가 협업하는 과정을 알아보면서 git에 관하여 알아보자 시리즈를 마치려고 한다.