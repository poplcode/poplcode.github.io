# 익명 게시판 만들기
[POPL](https://github.com/poplcode/popl) 을 이용해서 익명 게시판을 만들어봅니다.

## PHP와 데이터베이스 세팅
간단하게 [XAMPP](https://www.apachefriends.org/index.html) 를 이용해 개발환경을 구축합니다.
개인적으로 선호하는 취향이 있다면 그대로 해도 무방합니다.

## 데이터베이스 테이블 생성
데이터베이스 **게시판** 테이블을 생성합니다.
```sql
CREATE TABLE anobbs (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(128) NOT NULL,
        content text NOT NULL,
        use_yn char(1) NOT NULL DEFAULT 'Y',
        insert_date varchar(19) NOT NULL,
        update_date varchar(19) NULL,
        PRIMARY KEY (id)
);
```
## 임시데이터 입력
테스트할 데이터를 임의로 데이터베이스에 입력합니다.
```sql
insert into anobbs (title,content,use_yn, insert_date) values ('title_01', 'content_01', 'Y', now());
insert into anobbs (title,content,use_yn, insert_date) values ('title_02', 'content_02', 'Y', now());
insert into anobbs (title,content,use_yn, insert_date) values ('title_03', 'content_03', 'Y', now());
```

## popl 설치
이 예제는 [POPL 프로젝트의 샘플 코드](https://github.com/poplcode/popl/tree/master/samples/) 를 기준으로 합니다.

1. git으로 [가져오시거나](https://github.com/poplcode/popl.git) zip 파일을 [다운로드](https://github.com/poplcode/popl/archive/master.zip) 합니다.
2. 내부에 popl 디렉토리를 복사합니다.

디렉토리 구조는 아래와 같습니다.
```
프로젝트 root
├─popl
│  ├─config
│  └─lib
└─samples
    └─anobbs
```

## 데이터베이스 설정
`popl/config/config.local.php` 파일을 텍스트 에디터로 엽니다.
```php
$db_config = [
    'host' => 'localhost',
    'port' => '3306',
    'dbname' => 'popl',
    'charset' => 'utf8',
    'username' => 'popl',
    'password' => 'popl_pw'
];
```
위 내용을 본인의 데이터베이스에 맞게 수정합니다.

`popl/config/config.php` 파일을 열어서 `$popl_env_config = "local";` 로 되어있는 지 확인합니다.
popl은 `popl_env_config` 변수의 값을 보고 "config.$popl_env_config.php" 파일의 세팅을 읽습니다.


## 목록 만들기
데이터베이스에 있는 값 목록을 보여주는 간단한 기능을 만들어 봅니다.
![익명게시판 목록](/assets/images/index/anobbs_list.png)  

`samples/anobbs/index.php` 파일을 생성하고 아래의 내용을 입력합니다.
```php
<?php
require_once("../../popl/popl_core.php");

$page_no = popl_param_get("page_no", "r,n,min:1", 1);
$bbs_list = popl_db_select_paging("anobbs", $page_no);
foreach($bbs_list as $bbs){
?>
    <p><a href='/content.php?bbs_id=<?= $bbs["id"] ?>'><?= $bbs['title'] ?></a></p>
<?php } // end of foreach ?>
```

위 코드는 아래와 같습니다.
* `$page_no = ` : get 파라미터 page_no를 입력받아 유효성을 검증하고 실패하면 기본값을 1로 세팅합니다.
* `$bbs_list = ` : 데이터베이스 anobbs에서 $page_no 에 해당하는 목록을 가져옵니다.
* 이하 부분은 평범한 php 구문입니다. foreach 로 루프를 돌면서 html을 보여줍니다.

웹브라우저에서 `http://localhost:8000` 을 입력해서 확인합니다.
개별 세팅에 따라 포트는 달라질 수 있습니다.

## 상세페이지 만들기
### 요청 처리 파일 생성
`samples/anobbs/content.php` 파일을 생성하고 아래의 내용을 입력합니다.

```php
<?php
require_once("../../popl/popl_core.php");
$bbs_id = popl_param_get("bbs_id", "r,n,min:1") or popl_response_redirect();
$bbs = popl_db_select_first_by_id("anobbs",$bbs_id) or popl_response_redirect();
popl_view("content.view", ["bbs"=>$bbs, "title"=>$bbs['title']]);
```

위 코드는 아래와 같습니다.
* `$bbs_id = ` : get 파라미터 page_no를 입력받아 유효성을 검증한 후 정상이면 파라미터를 가지고 옵니다. 실패하면 root path (/) 로 리다이렉트합니다.
* `$bbs = ` : 데이터베이스 테이블 anobbs 에서 $bbs_id 로 검색 후 첫번째 열을 가져옵니다. 실패하면 root path (/) 로 리다이렉트합니다.
* `popl_view` : 현재 디렉토리의 content.view.php 파일을 불러옵니다. 파라미터로는 데이터베이스에서 추출한 `$bbs` 변수를 bbs라는 이름으로 넘겨줍니다. `.php` 확장자는 없다는 점에 유의하세요.

이제 `content.php` 파일은 **MVC** 구조에서 **Controller** 라고 부르는 역할을 하게 되었습니다.

### 화면 파일 생성
요청을 처리하는 `content.php` 에서 `content.view.php` 파일을 사용하므로 `samples/anobbs/content.view.php` 파일을 생성하고 아래 내용을 입력합니다.

```php
<?php if (defined('POPL_IS_START') === false){die();} ?>
<h1><?= $title ?></h1>
<p>last modify : <?= $bbs['upsert_date'] ?></p>
<div>
    <?= $bbs['content'] ?>
</div>
```

* `if (defined('POPL_IS_START')` : 보안상의 이유로 content.view.php 파일이 웹브라우저에서 직접 접근했다면 실행을 멈춥니다. popl_view를 통해 호출되었다면 `POPL_IS_START` 라는 상수가 있으므로 아래 내용이 정상적으로 실행됩니다.
* `$title` : content.php 에서 파라미터로 전달한 'title' 배열 키를 변수명으로 사용합니다.
* `$bbs` : content.php 에서 전달한 bbs 변수를 직접 사용할 수 있습니다.

웹브라우저에서 `http://localhost:8000/content.php?bbs_id=1` 을 입력해서 확인합니다.

이제 `content.view.php` 파일은 **MVC** 구조에서 **View** 라고 부르는 역할을 하게 되었습니다.

### 공통 레이아웃 만들기
대부분의 웹사이트는 공통의 레이아웃을 사용하고 내용만 바뀝니다.
따라서 공통으로 사용할 레이아웃을 만들어 봅니다.
`samples/anobbs/common.view.layout.php` 파일을 생성하고 아래 내용을 붙여넣습니다.

```php
<?php if (defined('POPL_IS_START') === false){die();} ?>
<!DOCTYPE html>
<head>
    <title><?= $title ?></title>
</head>
<div>
    <h1>레이아웃을 사용합니다.</h1>
    <?= $POPL_VIEW_CONTENT ?>
</div>
```

* `<?= $title` : 일반 화면 파일처럼 레이아웃에서도 요청 처리 파일에서 넘겨준 값을 사용할 수 있습니다. 이 값은 아래 요청 처리 파일 수정 부분에서 수정해 봅니다.
* `<?= $POPL_VIEW_CONTENT ?>` : POPL은 레이아웃 사용시 먼저 컨텐츠 내용을 가져오고 그 내용에 `$POPL_VIEW_CONTENT` 라는 특수한 이름을 붙입니다. 따라서 레이아웃에서 `$POPL_VIEW_CONTENT` 변수의 값을 보여줍니다.

### 화면 파일 수정
`samples/anobbs/content.view.php` 파일을 조금 수정해서 공통 레이아웃을 사용해 보겠습니다.

```php
<?php if (defined('POPL_IS_START') === false){die();} ?>
<?php $POPL_VIEW_LAYOUT = "common.view.layout"; ?>
```
* `$POPL_VIEW_LAYOUT` : 2번째 줄에 `$POPL_VIEW_LAYOUT` 변수가 추가되었습니다. POPL은 `$POPL_VIEW_LAYOUT` 변수가 있다면 레이아웃을 지정하는 경로라고 판단하여 뷰를 렌더링합니다. `.php` 확장자는 없다는 점에 유의하세요.

한 줄 추가로 레이아웃을 사용할 수 있게 되었습니다.