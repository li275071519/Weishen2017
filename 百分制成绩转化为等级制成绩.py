score = float(input("请输入成绩："))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >=  70:
    grade ='C'
elif score >= 60:
    grade ='D'
else:
    grade = '不及格'
print ('对应的成绩等级是：',grade)