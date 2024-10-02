# Java
> 참고 ([점프 투 자바](https://wikidocs.net/book/31))

## Switch Case
```java
switch(입력변수) {
    case 입력값1: ...
        break;
    case 입력값2: ...
        break;
    ...
    default: ...
        break;
}
```
- 입력 변수의 자료형은 byte, short, char, int, enum, String 만 가능

## Print
- python 의 `print(f"{변수}")` 형식
```java
String str = "Java";
System.out.print("This is" + str);
int num = 10;
System.out.printf("This is %d", num);
```
| 지시자 | 설명 |
|---|---|
|%b|boolean 형식으로 출력|
|%d|정수 형식으로 출력|
|%o|8진수 정수의 형식으로 출력|
|%x 또는 %X|16진수 정수의 형식으로 출력|
|%f|소수점 형식으로 출력|
|%c|문자형식으로 출력|
|%s|문자열 형식으로 출력|
|%n|줄바꿈 기능|
|%e 또는 %E|지수 표현식의 형식으로 출력|

