from school import School

code = School.getSchool('dge', '성광중')
print(School(region='dge', id=code['orgCode']).getMeal(year=2021, month=5, day=24))
print(code)