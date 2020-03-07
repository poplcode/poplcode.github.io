---
layout: default
title: POPL
description: Plain Old Php Library
---

# Plain Old Php Library
POPL(**P**lain **O**ld **P**hp **L**ibrary) 은 __레거시 PHP 개발자__ 를 위한 **PHP 라이브러리 모음**입니다.   

* POJO(Plain Old Java Object), POCO(Plain Old CSharp Object) 등 상속 등을 사용하지 않고 순수한 객체를 만들어서 개발에 이용하는 것을 Plain Old {언어이름} Object 라고 부릅니다.  
* PHP 는 처음에 **객체 중심이 아닌 함수(~~function~~Procedure)** 중심 언어로 시작했기 때문에, Object 대신 **Libray** 라고 합니다.

# 설계의 목적
POPL은 __레거시 PHP 개발자__ 를 위한 라이브러리 셋입니다.  
따라서 가능한 러닝커브를 줄이고 기존에 오래된 방법으로 PHP 개발을 하시던 분들이 위화감을 적게 느끼시도록 설계했습니다.

* 네임스페이스는 쓰지 않습니다. 대신 모든 함수은 `popl_` 로 시작합니다.
* composer 는 사용하지 않습니다.
* 객체는 전혀 사용하지 않습니다.
* 파일 단 1개만 require 하면 나머지는 알아서 작동합니다.

# 설치
1. 그냥 [다운로드]() 합니다.
2. 아무 디렉토리에나 압축을 풉니다.
3. require 해서 사용합니다.
4. 만약 데이터베이스 설정이 필요하다면 `popl/config/config.{환경이름}.php` 파일을 열고 설정합니다.
5. 

# 튜토리얼
## 배포하기

# 함수 목록

# About Author

