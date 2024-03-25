# Velog Migration

> `Velog`글 이주하기

Velog글들을 시리즈에 맞게 폴더링하여 정리해주는 `cronJob` 및 스크립트

_Why? -> 취업하면서 깃허브 커밋이 박살 조금이라두 살리기..._

---

#### CronJob Script

1. 매일 아침에 글 N개를 가져와서 작성되어있지 않은 글이면 작성하는 `Github Action Cron Job`
    1. 만약 작성한 글에 시리즈가 없다면 무시
    2. 시리즈 정보를 가져와서 폴더링
       - 이미 존재하면 무시
         - 존재유무는 `github 내부를 local 저장소로 활용`
    3. `velog graphQL API` 사용

#### Migration Script

2. 아이디를 입력하면 시리즈에 대한 모든 글을 깃허브로 올려주는 파이썬 스크립트 
    1. 시리즈 정보를 활용해 폴더링
    2. 이미 존재해도 덮어 쒸우기
