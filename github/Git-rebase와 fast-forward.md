# rebase와 fast-forward에 대한 고찰
---
나는 평소와 같이 github-dev를 통해서 c언어 workspace를 구축하고 있던 도중 다음과 같은 문제를 마주하게 되었다. main header와 origin/main header가 서로 다른 브랜치를 가리키고 있어서 vscode상의 동기화에 에러가 걸린것이다. 

이럴 경우, 단순히 main과 origin main의 헤더가 브랜치 자체가 다르기 때문에 git pull 및 git push가 작동하지 않는것을 볼 수 있다.

```
@Dehite12454 ➜ /workspaces/c (main) $ git push
To https://github.com/Dehite12454/c
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/Dehite12454/c'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
### 1. fast-forward 관계란?
오류 코드를 읽어보면 non-fast-forward 이기 때문에 rejected 되었다고 서술되어 있다.
그렇다면 fast-forward 란 무엇일까? fast-forward 관계를 단순하게 말하자면, 분기된 브랜치가 기존 브랜치의 커밋 히스토리를 포함하고 있다면 두 브랜치를 fast-forward 관계라고 정의한다.
![](https://velog.velcdn.com/images/dehite0704/post/6072709e-0429-4e31-8018-1f02f84ab96f/image.png)
###### 출처:<https://otzslayer.github.io/git/2021/12/05/git-merge-fast-forward.html#%EB%A7%88%EB%AC%B4%EB%A6%AC>
이처럼 B 브랜치는 A 브랜치와 fast-forward 관계이므로 단순히 header 위치를 바꾸는 것으로 동기화가 가능하다. 단순하게 git merge [브랜치명] 명령어로 이를 실행할 수 있다.
![](https://velog.velcdn.com/images/dehite0704/post/ac8cb2c6-5716-4519-8c9a-8a806b316b01/image.png)
###### 출처:<https://otzslayer.github.io/git/2021/12/05/git-merge-fast-forward.html#%EB%A7%88%EB%AC%B4%EB%A6%AC>
위와 같이 A 브랜치와 B 브랜치가 서로 포함하지 않는 히스토리를 가지고 있다면 이는 서로 non-fast-forward 관계이므로 단순한 merge로 합치는 것이 아닌 git merge --no-ff [브랜치명] 으로 병합한다. 이럴 경우 병합 커밋이 새롭게 생성되며, 기록에 남는다.

현재 나의 workspace는 두 브랜치가 non-fast-forward 상태이므로 git push가 먹히지 않았던 것이었다. 나는 그렇다면 git pull은 잘 작동하는가 에 대한 궁금증이 생겼다. 다음은 git pull을 했을 때 발생한 오류 코드이다.
```
@Dehite12454 ➜ /workspaces/c (main) $ git pull
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
```
위와 같은 오류 메시지에서 git pull 을 제대로 동작하게 하려면 다음과 같은 명령어를 시도해보라고 나와있다. 이때, pull.ff only는 ff 관계일 때 pull을 하라는 명령으로 해석이 가능하다. 그렇다면 rebase는 무엇일까?
### 2. rebase 는 무엇일까
한 브랜치를 다른 브랜치와 합치는 것은 두가지 방식이 존재한다. 하나는 merge이고 다른 하나는 rebase이다. 두 브랜치를 merge 한다고 가정하자. 이때는 우리에게 익숙하게, 새로운 merge commit 이 생성되고 두 브랜치를 하나로 병합할 수 있다. 그렇다면 rebase는 무엇일까?

rebase는 이름 그대로 base를 다시 맞춘다는 것이다. 두 브랜치를 merge할 때, master 브랜치에 새로운 커밋들과 분기한 브랜치의 커밋들이 달라 발생하는 conflict를 해결하는 방식 중 하나이다. 분기된 브랜치의 커밋들을 master 브랜치의 최신 커밋을 새로운 base로 설정해서 새로운 해시 커밋으로 수정사항을 반영하는 것이다.
![](https://velog.velcdn.com/images/dehite0704/post/33e2f236-784b-4159-9fb4-a38620bbda0f/image.png)
![](https://velog.velcdn.com/images/dehite0704/post/56eb602b-f68c-4a0a-bace-7cb08ead0e07/image.png)
###### 출처: <https://ho8487.tistory.com/90>
rebase를 하게 되면 git log 가 깔끔해진다는 장점이 있다.
브랜치가 분기했다는 사실을 지워버리고 선형적인 log 상태로 사용자에게 보여지기 때문이다.
하지만 무분별한 rebase 사용은 협업하는 다른 사용자에게 치명적일 수 있는데, rebase 할 경우 바뀌어 버리는 해시들에 의해 다른 사용자가 쌓아왔던 코드가 꼬여버릴 수 있기 때문이다.
나는 혼자서 작업하는 c workspace를 사용하고 있으므로 rebase를 통해 코드를 간단화 시켰다.

rebase를 통해 현재 origin/main 과 main 브랜치가 ff 관계인것을 확인할 수 있다. 이후 header 동기화 작업을 수행했을 때 오류 없이 잘 작동하는 것을 볼 수 있다.