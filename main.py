import school

schoolData = school.getSchool(name="성광중학교",region="dge", beautify=True)[0]
print(school.School(region='dge', code=schoolData['code']).getMeal())