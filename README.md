# 🍚 School-Meal
파이썬으로 작성된 급식정보 모듈입니다.
## 사용법
school.School()
* region - 지역
* id - 나이스 학교ID<br/>
반환값 - SCHOOL object

SCHOOL.getMeal()
* *year - 년
* *month - 월
* *day - 일
* code - 1:조식 / 2:중식 / 3:석식
반환값 - List

school.getSchool()
* *region - 지역
* *name - 학교명
반환값 (예시)
```
{'sqlAction': '', 'orgCode': 'D100000851', 'kraOrgNm': '성광중학교', 'zipAdres': '대구광역시 북구 복현동', 'schulKndScCode': '03', 'atptOfcdcNm': '대구광역시교육청', 'atptOfcdcOrgCode': 'D100000001', 'schulCrseScCode': '3', 'schulCrseScCodeNm': '중학교'}
```

**본인이 사용중인 Chrome 버전에 따라 필요한 chromedriver.exe 파일의 (버전)[https://chromedriver.chromium.org/downloads]이 달라 오류가 발생할 수 있습니다.**

## 체크리스트
* [x] 급식정보 불러오기
* [x] 학교정보 불러오기
