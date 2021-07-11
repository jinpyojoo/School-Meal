# school.py
파이썬으로 작성된 학교정보 모듈입니다.

## 지역코드
 - sen - 서울
 - pen - 부산
 - dge - 대구
 - ice - 인천
 - dje - 대전
 - use - 울산
 - sje - 세종
 - goe - 경기
 - kwe - 강원
 - cbe - 충북
 - cne - 충남
 - jbe - 전북
 - jne - 전남
 - gbe - 경북
 - jje - 제주

## 함수
school.School()
* *region - 지역
* *code - 나이스 학교코드<br/>
반환값 - SCHOOL object

SCHOOL.getMeal()
``기본값 : 오늘``
* *year - 년
* *month - 월
* *day - 일
* code - 1:조식 / 2:중식 / 3:석식 ``기본값 2``
반환값 - List

school.getSchool()
* *region - 지역
* *name - 학교명
* beautify - 반환값 정리 ``기본값 True``
반환값 (예시)
```
{'office': '대구광역시교육청', 'code': 'D100000851', 'name': '성광중학교', 'zip': '대구광역시 북구 복현동', 'type': '3'}
```
School 함수에 사용되는 코드는 `code` 입니다.


## 체크리스트
* [x] 급식정보 불러오기
* [x] 학교정보 불러오기
