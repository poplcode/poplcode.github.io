# 익명 게시판 만들기
[POPL](https://github.com/poplcode/popl) 을 이용해서 익명 게시판을 만들어봅니다.

## PHP와 데이터베이스 세팅
간단하게 [XAMPP](https://www.apachefriends.org/index.html) 를 이용해 개발환경을 구축합니다.
개인적으로 선호하는 취향이 있다면 그대로 해도 무방합니다.

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

## 오토테이블 기능 여부 확인
`popl/config/config.local.php` 파일 하단의 `use_create_table_config` 항목이 `true` 로 되어 있는지 확인합니다. 
`$use_create_table_config = true;`  
이 기능이 켜져 있으면 웹에서 바로 테이블 생성이 가능합니다.  
직접 테이블을 생성하시려면 `false` 여도 무관합니다.


## 데이터베이스 테이블 생성
데이터베이스 **게시판** 테이블을 생성합니다.

### 오토테이블 사용시
`popl/config/config.local.php` 파일의 `$use_create_table_config=true;` 인지 확인합니다.

`samples/anobbs/create_table.php` 파일을 생성하고 아래 내용을 입력합니다.
```php
<?php
require_once("../../popl/popl_core.php");
popl_db_create_table_standard("anobbs", ['title','content','bbs_pw']);
```

[방금 생성한 파일의 url](http://localhost:8000/create_table.php) 에 접속해 봅니다.

데이터베이스 설정이 정상적으로 되어 있다면 popl은 `id, title, content, bbs_pw, use_yn, insert_date, update_date` 컬럼을 가진 `anobbs` 테이블을 생성합니다.


### 직접 데이터베이스에서 생성하기
phpmyadmin 혹은 mysql workbench 등 편리한 툴로 데이터베이스에 접속 후 아래 쿼리를 실행합니다.
```sql
CREATE TABLE anobbs (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(128) NOT NULL,
        content text NOT NULL,
        bbs_pw text NOT NULL,
        use_yn char(1) NOT NULL DEFAULT 'Y',
        insert_date varchar(19) NOT NULL,
        update_date varchar(19) NULL,
        PRIMARY KEY (id)
);
```


## 목록 만들기
데이터베이스에 있는 값 목록을 보여주는 간단한 기능을 만들어 봅니다.
![익명게시판 목록](/assets/images/anobbs/anobbs_list.png)

`samples/anobbs/index.php` 파일을 생성하고 아래의 내용을 입력합니다.
```php
<?php
require_once("../../popl/popl_core.php");

$page_no = popl_param_get("page_no", "r,n,min:1", 1);
$bbs_list = popl_db_select_paging("anobbs", $page_no);
echo "<ul>";
foreach($bbs_list as $bbs){
?>
    <li><a href='/content.php?bbs_id=<?= $bbs["id"] ?>'><?= $bbs['title'] ?></a></li>
<?php } // end of foreach ?>
</ul>
<p><a href='write.php'>글쓰기</a></p>
```

위 코드는 아래와 같습니다.
* `popl_param_get` : get 파라미터 page_no를 입력받아 유효성을 검증하고 실패하면 기본값을 1로 세팅합니다.
* `popl_db_select_paging` : 데이터베이스 anobbs에서 $page_no 에 해당하는 목록을 가져옵니다.
* 이하 부분은 평범한 php 구문입니다. foreach 로 루프를 돌면서 html을 보여줍니다.

웹브라우저에서 `http://localhost:8000` 을 입력해서 확인합니다.  
아직 데이터가 없으므로 아무것도 나오지 않는 것이 정상입니다.  

## 상세페이지 만들기
![익명게시판 상세페이지 레이아웃 미사용](/assets/images/anobbs/anobbs_content_nolayout.png)

`samples/anobbs/content.php` 파일을 생성하고 아래의 내용을 입력합니다.

```php
<?php
require_once("../../popl/popl_core.php");
$bbs_id = popl_param_get("bbs_id", "r,n,min:1") or popl_response_redirect();
$bbs = popl_db_select_first_by_id("anobbs",$bbs_id) or popl_response_redirect();
$title = $bbs['title'];
$content = popl_str_wrap_each_lines($bbs['content'], "<p>","</p>");
?>
<h1><?= $title ?></h1>
<p>last modify : <?= $bbs['upsert_date'] ?></p>
<div>
    <?= $content ?>
</div>
<hr />
<h3>수정</h3>
<a href="bbs_pw.php?bbs_id=<?= $bbs_id ?>">수정하기</a>
<?php popl_flash_show("<p>","</p>"); ?>
```

위 코드는 아래와 같습니다.
* `popl_param_get` : get 파라미터 page_no를 입력받아 유효성을 검증한 후 정상이면 파라미터를 가지고 옵니다. 실패하면 root path (/) 로 리다이렉트합니다.
* `popl_db_select_first_by_id` : 데이터베이스 테이블 anobbs 에서 $bbs_id 로 검색 후 첫번째 열을 가져옵니다. 실패하면 root path (/) 로 리다이렉트합니다.
* `popl_str_wrap_each_lines` : 여러 줄로 이루어진 문자열에 매 줄마다 앞 뒤에 글자를 붙여줍니다. $content의 경우 줄바꿈으로 입력되지만 보여질 때는 `<p>` 태그로 감싸기 위해 사용합니다.
* `$bbs['upsert_date']` : upsert_date 는 최종 갱신일을 나타내기 위해 popl에서 동적으로 만들어내는 필드입니다. update_date 가 != null 일 경우 update_date 를, 아니면 insert_date 를 보여줍니다. 만약 insert_date나 update_date 가 없다면 null 입니다.
* `popl_flash_show` : 플래시 메세지를 보여줍니다.


## 공통 레이아웃 사용하기
![익명게시판 상세페이지 레이아웃 사용](/assets/images/anobbs/anobbs_content_layout.png)

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

* `POPL_IS_START` : 만약 사용자가 `/common.view.layout.php` 주소로 바로 접근한다면 내용을 보여주지 않고 바로 종료합니다. `POPL_IS_START` **상수** 는 popl 이 시작되면서 자동으로 `true` 로 설정됩니다.
* `<?= $title` : 일반 화면 파일처럼 레이아웃에서도 요청 처리 파일에서 넘겨준 값을 사용할 수 있습니다.
* `<?= $POPL_VIEW_CONTENT ?>` : POPL은 레이아웃 사용시 먼저 컨텐츠 내용을 가져오고 그 내용에 `$POPL_VIEW_CONTENT` 라는 특수한 이름을 붙입니다. 따라서 레이아웃에서 `$POPL_VIEW_CONTENT` 변수를 출력하면 컨텐츠 내용이 출력됩니다.

### 상세페이지 화면 파일 수정
`samples/anobbs/content.php` 파일을 조금 수정해서 공통 레이아웃을 사용해 보겠습니다.

```php
require_once("../../popl/popl_core.php");
$bbs_id = popl_param_get("bbs_id", "r,n,min:1") or popl_response_redirect();
$bbs = popl_db_select_first_by_id("anobbs",$bbs_id) or popl_response_redirect();
$title = $bbs['title'];
$content = popl_str_wrap_each_lines($bbs['content'], "<p>","</p>");
popl_view_layout_direct_start();

?>
<h1><?= $title ?></h1>
<p>last modify : <?= $bbs['upsert_date'] ?></p>
<div>
    <?= $content ?>
</div>
<hr />
<h3>수정</h3>
<a href="bbs_pw.php?bbs_id=<?= $bbs_id ?>">수정하기</a>
<?php popl_flash_show("<p>","</p>"); ?>
<?php
popl_view_layout_direct_end("common.view.layout", ['title'=> $title]);
?>
```

실제로 변한 곳은 `popl_view_layout_direct_start;` , `popl_view_layout_direct_end` 두곳입니다.

* `popl_view_layout_direct_start` : 레이아웃을 사용하기 위해 본문 영역이 시작하는 곳을 표시합니다.
* `popl_view_layout_direct_end` : 레이아웃을 지정하고 본문이 끝났다는 것을 알립니다.

## 글쓰기 폼 만들기
익명 게시판이니 누구나 글을 쓸 수 있습니다.

![글쓰기](/assets/images/anobbs/anobbs_write.png)

`samples/anobbs/write.php` 파일을 생성하고 아래 내용을 넣습니다.

```php
<?php
require_once("../../popl/popl_core.php");
popl_view_layout_direct_start();
?>
<form name="form" action="write.form.php" method="post">
    <p>제목 : <input type='text' name="title" style='width:80%;' /></p>
    <p>내용 : <textarea name="content" rows="5" style='width:80%;'></textarea></p>
    <p>비밀번호 : <input type="password" name="bbs_pw" /></p>
    <p><input type='submit' value="저장하기" /></p>
</form>
<?php popl_flash_show("<p>","</p>"); ?>
<?php
popl_view_layout_direct_end("common.view.layout", ['title'=> '글쓰기']);
?>
```

* `bbs_pw` : 익명 게시판이기 때문에 로그인 기반으로 글을 쓸 수는 없습니다. 따라서 글 비밀번호를 저장하고 수정시에 글 비밀번호를 입력하게 합니다.

## 글쓰기 기능 만들기
실제로 글이 쓰여지는 기능을 만들어 봅니다.
`samples/anobbs/write.form.php` 파일을 생성하고 아래 내용을 붙여넣습니다.

```php
<?php
require_once("../../popl/popl_core.php");
popl_valid_http_method_post() or popl_response_redirect("write.php");

$title = popl_param_post_san_html_remove("title", "r,minlen:1") or popl_response_redirect_flash("write.php", "제목은 1글자 이상입니다.");
$content = popl_param_post_san_html_encode("content", "r,minlen:10") or popl_response_redirect_flash("write.php", "컨텐츠는 10글자 이상입니다.");
$bbs_pw = popl_param_post_password_encrypt("bbs_pw", "r,minlen:4") or popl_response_redirect_flash("write.php", "비밀번호는 4글자 이상입니다.");

$last_id = popl_db_insert_standard("anobbs", ["title"=>$title, "content"=>$content, "bbs_pw"=>$bbs_pw]) or popl_response_redirect("write.php");
popl_response_redirect("content.php?bbs_id=" . $last_id);
```

* `popl_valid_http_method_post` : http method 가 **POST** 가 아니면 false 를 반환합니다. 
* `$title =` : title 파라미터를 검증해 보고 성공하면 html을 지운 채 반환합니다. 실패하면 플래시 메세지와 함께 write.php 로 다시 리다이렉트합니다.
* `$content=` : content 파라미터를 검증해 보고 성공하면 html을 인코딩한 후 반환합니다. 실패하면 플래시 메세지와 함께 write.php 로 다시 리다이렉트합니다.
* `$bbs_pw =` : bbs_pw 파라미터를 검증해 보고 성공하면 html을 지운 채 반환합니다. 실패하면 플래시 메세지와 함께 write.php 로 다시 리다이렉트합니다.
* `$last_id =` : anobbs 테이블에 기본값(insert_date, use_yn) 과 함께 insert 한 후 id 를 반환합니다. 실패하면 다시 write.php 로 리다이렉트합니다.
