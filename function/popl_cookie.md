# 쿠키 함수
POPL 에서 사용하는 쿠키 함수 목록입니다.  
쿠키 함수는 모두 `popl_cookie_` 로 시작합니다.


## 함수 목록
* [popl_cookie_set](#poplcookieset)
* [popl_cookie_get](#poplcookieget)
* [popl_cookie_remove](#poplcookieremove)
* [popl_cookie_set_array](#poplcookiesetarray)
* [popl_cookie_get_array](#poplcookiegetarray)

---        
## popl_cookie_set
### 함수 원형
`popl_cookie_set($key, $val)`

### 설명
쿠키에 키(`$key`) 로 값(`$val`) 을 넣습니다.

---        
## popl_cookie_get
### 함수 원형
`popl_cookie_get($key, $default=null)`

### 설명
쿠키에 키(`$key`) 로 값을 가져옵니다. 만약 실패하면 `$default` 를 반환합니다.

---        
## popl_cookie_remove
### 함수 원형
`popl_cookie_remove($key)`

### 설명
쿠키에 키(`$key`) 가 있다면 키에 해당하는 값을 삭제합니다.

---        
## popl_cookie_set_array
### 함수 원형
`popl_cookie_set_array($key, $val)`

### 설명
쿠키에 키(`$key`)로 값(`$val`)을 문자열이 아닌 배열에 추가합니다.

---        
## popl_cookie_get_array
### 함수 원형
`popl_cookie_get_array($key, $default=[])`

### 설명
쿠키의 키(`$key`)로 값을 가져옵니다. 만약 실패하면 `$default` 를 반환합니다.

