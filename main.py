import school

schoolData = school.getSchool(name="성광중",region="dge")[0]
print(school.School(code=schoolData, region="dge").getMeal())