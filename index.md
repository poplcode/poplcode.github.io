---
layout: default
title: POPL
description: Plain Old Php Library
---

# Plain Old Php Library
POPL(**P**lain **O**ld **P**hp **L**ibrary) 은 __레거시 PHP 개발자__ 를 위한 **PHP 라이브러리 모음**입니다.   

가능한 러닝커브를 줄이고 기존에 오래된 방법으로 PHP 개발을 하시던 분들이 위화감을 적게 느끼시도록 설계했습니다.

* 네임스페이스는 쓰지 않습니다. 대신 모든 함수 이름은 `popl_` 로 시작합니다.
* composer 는 사용하지 않습니다.
* OOP는 전혀 사용하지 않습니다.
* 파일 단 1개만 require 하면 됩니다.
* 어떤 프로젝트, 어떤 프레임워크에도 적용할 수 있습니다.
* 개발자에게 특정한 구조나 디렉토리 형식, 이름 등을 강요하지 않습니다.

# 설치
1. git으로 [가져오시거나](git@github.com:poplcode/popl.git) zip 파일을 [다운로드](https://github.com/poplcode/popl/archive/master.zip) 합니다.
2. 압축을 해제하고 내부의 /popl 디렉토리를 적용하고자 하는 프로젝트 아무곳에나 복사합니다.
3. 적용하시고자 하는 프로젝트에 require 해서 사용합니다.

# 기능
* 배열 (array) : 배열 관련 함수가 모여있습니다. `popl_array` 로 시작합니다.
* 쿠키 (cookie) : 쿠키 관련 함수가 모여있습니다. `popl_cookie` 로 시작합니다.
* 데이터베이스 (database) : 데이터베이스 관련 함수가 모여있습니다. `popl_db` 로 시작합니다.
* 플래시 메세지 (flash message) : 플래시 메세지 관련 함수가 모여있습니다. `popl_flash` 로 시작합니다.
* 로그인 (login) : 로그인 관련 함수가 모여있습니다. `popl_login` 으로 시작합니다.
* http 파라미터 (http parameter) : get 혹은 post http 파라미터 관련 함수가 모여있습니다. 관련 함수가 모여있습니다. `popl_param` 으로 시작합니다.
* 비밀번호 (password) : 비밀번호 암호화 및 체크 함수가 모여있습니다.
* 응답 (response) : http response 관련 함수가 모여있습니다. `popl_response` 로 시작합니다.
* 세션 (session) : 세션 관련 함수가 모여있습니다. `popl_session` 으로 시작합니다.
* 문자열 (string) : 문자열 관련 함수가 모여있습니다. `popl_str` 로 시작합니다.
* 유효성 검사 (validation) : 유효성 검사 관련 함수가 모여있습니다. `popl_valid` 로 시작합니다.
* 뷰 (view) : 뷰 관련 함수가 모여있습니다. `popl_view` 로 시작합니다.

상세한 함수 메뉴얼은 [POPL 메뉴얼]() 을 참고하세요.

# 튜토리얼


# POPL BLOG

# 버전 히스토리
* 최신 버전은 **0.10** 입니다. 2020.03.09일에 릴리즈되었습니다.

# Contact
* POPL 에 기여하고 싶으시면 PULL REQUEST 를 해 주시면 감사하겠습니다.
* 그 외의 연락은 [contact@popl.ml](mailto:contact@popl.ml) 로 해 주세요.


# 라이센스
[MIT License](https://github.com/poplcode/popl/blob/master/LICENSE)