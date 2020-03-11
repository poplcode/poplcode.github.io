# 데이터베이스 함수
POPL 에서 사용하는 데이터베이스 함수 목록입니다.  
데이터베이스 함수는 모두 `popl_db_` 로 시작합니다.


## 함수 목록
* [popl_db_get_pdo](#popldbgetpdo)
* [popl_db_execute](#popldbexecute)
* [popl_db_execute_last_id](#popldbexecutelastid)
* [popl_db_fetch_all](#popldbfetchall)
* [popl_db_make_terms](#popldbmaketerms)
* [popl_db_make_orderby](#popldbmakeorderby)
* [popl_db_make_limit](#popldbmakelimit)
* [set_upsert_date_column](#setupsertdatecolumn)
* [popl_db_select](#popldbselect)
* [popl_db_select_first](#popldbselectfirst)
* [popl_db_select_first_by_id](#popldbselectfirstbyid)
* [popl_db_select_exist](#popldbselectexist)
* [popl_db_select_paging](#popldbselectpaging)
* [popl_db_insert](#popldbinsert)
* [popl_db_set_default_values](#popldbsetdefaultvalues)
* [popl_db_insert_standard](#popldbinsertstandard)
* [popl_db_update_standard](#popldbupdatestandard)
* [popl_db_upsert](#popldbupsert)
* [popl_db_upsert_standard](#popldbupsertstandard)
* [popl_db_delete](#popldbdelete)
* [popl_db_delete_by_id](#popldbdeletebyid)

---        
## popl_db_get_pdo
### 함수 원형
`popl_db_get_pdo() : PDO`

### 설명
pdo 객체를 얻어올 때 쓰입니다.  
일반적으로는 `popl_db` 관련 다른 함수에서 데이터베이스를 핸들링할 때 쓰입니다.

---        
## popl_db_execute
### 함수 원형
`popl_db_execute($query, $param) : boolean`

### 설명
데이터베이스에 `update` 혹은 `delete` 실행시 사용합니다.  
직접 SQL 쿼리를 작성하고 반환값이 성공/실패 여부일 때 사용합니다.

---        
## popl_db_execute_last_id
### 함수 원형
`popl_db_execute_last_id($query, $param) : int or false`

### 설명
데이터베이스에 `insert` 실행시 사용합니다.  
성공하면 primary key id 를, 실패하면 false 를 반환합니다.

---        
## popl_db_fetch_all
### 함수 원형
`popl_db_fetch_all($query, $param)`

### 설명


---        
## popl_db_make_terms
### 함수 원형
`popl_db_make_terms($kvParam=[])`

### 설명


---        
## popl_db_make_orderby
### 함수 원형
`popl_db_make_orderby($orderby)`

### 설명


---        
## popl_db_make_limit
### 함수 원형
`popl_db_make_limit($limit)`

### 설명


---        
## set_upsert_date_column
### 함수 원형
`set_upsert_date_column($row)`

### 설명


---        
## popl_db_select
### 함수 원형
`popl_db_select($table_name, $kvParam=[], $orderby='', $limit=null)`

### 설명


---        
## popl_db_select_first
### 함수 원형
`popl_db_select_first($table_name, $kvParam=[], $orderby='')`

### 설명


---        
## popl_db_select_first_by_id
### 함수 원형
`popl_db_select_first_by_id($table_name, $id)`

### 설명


---        
## popl_db_select_exist
### 함수 원형
`popl_db_select_exist($table_name, $kvParam=[])`

### 설명


---        
## popl_db_select_paging
### 함수 원형
`popl_db_select_paging($table_name, $page_no, $kvParam=[], $orderby='insert_date desc', $count_per_page=10)`

### 설명


---        
## popl_db_insert
### 함수 원형
`popl_db_insert($table_name, $kvparam=[])`

### 설명

---        
## popl_db_set_default_values
### 함수 원형
`popl_db_set_default_values($kvparam, $default_key_vals)`

### 설명


---        
## popl_db_insert_standard
### 함수 원형
`popl_db_insert_standard($table_name, $kvparam)`

### 설명

---        
## popl_db_update_standard
### 함수 원형
`popl_db_update_standard($table_name, $kvparam, $where_terms)`

### 설명


---        
## popl_db_upsert
### 함수 원형
`popl_db_upsert($table_name, $kvparam, $where_terms)`

### 설명


---        
## popl_db_upsert_standard
### 함수 원형
`popl_db_upsert_standard($table_name, $kvparam, $where_terms)`

### 설명

---        
## popl_db_delete
### 함수 원형
`popl_db_delete($table_name, $where_terms)`

### 설명


---        
## popl_db_delete_by_id
### 함수 원형
`popl_db_delete_by_id($table_name, $id)`

### 설명
