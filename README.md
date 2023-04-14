# 06_pjt


## Getting started
- Django web framework를 사용한 데이터처리
- Django Model 과 ORM
- database many to one ralationship
- database many to many realationship

프로그램주제: 영화 데이터를 생성 조회 수정 삭제할 수 있는 web application제작하기


## Description

  PJT프로젝트안에는 movies와 accounts 두개의 앱이 있습니다.
  movies 앱은 영화 게시글의 생성,수정,삭제 등을 담당합니다.
  이외에도 게시글에 댓글생성과 좋아요 기능을 views의 함수로 구현하였습니다.

  accounts앱은 전반적인 회원관리와 follow기능을 담당하는 앱입니다.



## Project status
<movies>
-댓글-
[Commentform]을 이용해 게시글에 댓글을 달 수 있도록 구성하였습니다.
views.py에 요청과 게시글의 pk를 넘겨받은 comments_create(request,pk) 함수와
요청,게시글의 pk, 댓글의 pk를 넘겨받은 comments_delete(request, pk, comment_pk)를
각각 구현하여 댓글을 생성,삭제할 수 있는 기능을 구현하였습니다.

-권한 검증-
[user.is_authenticated] 를 이용해 로그인한 계정의 유저가 생성자인
경우에만 게시글과 댓글을 작성,수정,삭제할 수 있도록 하였습니다.

-like-
[filter]와 [exists]함수를 통해 게시글을 좋아요한 경우에는 좋아요 취소를,
그렇지 않은 경우에는 좋아요를 누를 수 있게 했습니다.

<accounts>

-로그인,로그아웃,회원정보변경,회원가입,비밀번호 변경.. -
로그인은  [AuthenticationForm]을 이용하였고
회원가입과 정보수정은[CustomUserChangeForm],
비밀번호 변경은 [PasswordChangeForm]을 이용하였습니다.

-프로필 보기-
detail페이지에서 작성자를 클릭하면 profile.html로 넘어갈 수 있는 a링크를 작성하였습니다.
profile 함수에서는 get_user_model()를 이용해 어떤 유저의 프로필을 확인할 것인지 넘겨받고
유저가 쓴 게시글, 좋아요한 글을 확인할 수 있는 html페이지로 넘어갈 수 있게 합니다.

-팔로우-
[user.is_authenticated]를 사용하여 사용자가 로그인 한 경우에만 팔로우 기능을 사용할 수 있습니다.
사용자와 팔로우하고자 하는 유저가 다른 계정일때만 팔로우 기능이 활성화 됩니다.
[filter]와 [exists]함수를 통해 이미 팔로우한 경우에는 팔로우 취소가 , 반대의 경우에는
팔로우 버튼이 뜨도록 했습니다.
User 모델에서 symmetrical=False로 설정하여 내가 다른 사용자를 팔로우했을때 자동으로 다른 사용자도 팔로우하지 않도록 설정했습니다.


## 어려웠던 점

url에서 views로 넘어가는 과정에서 넘겨주는 변수와 넘겨받는 변수의
형을 일치 시켜줘야 하는데 그렇게 하지 못해 에러가 자주 발생했던 것 같습니다.

모델 변경후 migration을 잊어버려 migration에러에 빈번하게 직면 하였습니다. 



## 배운점

1:N 과 N:M 관계를 구분할 수 있게 됐습니다.
좋아요 기능을 구현하며 다대다 관계를 잘 이해할 수 있게 됐습니다.

User를  AbstractUser로 상속받아 쓰려면 seetiongs.py에 명시해줘야 함을 알게 됐습니다.


## 발전시키고 싶은 점

좋아요 버튼을 하트 모양으로 바꿔보고 해쉬태그를 넣으면 검색 할 수 있는 기능과 싫어요 기능 , 대댓글 기능을 더 추가해 보고 싶습니다.