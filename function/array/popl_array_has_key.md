# popl_array_has_key

## 개요
배열에 키가 있는지 정렬합니다.

## 함수 원형
`popl_array_has_key($arr, $key) : boolean`

## 사용 예제
```php
$arr = ['A'=> 1, 'B' => 2];

var_dump(popl_array_has_key($arr, 'A')); // true
var_dump(popl_array_has_key($arr, 'C')); // false
```
