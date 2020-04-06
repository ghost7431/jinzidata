good = {}
bad = {}  
stu = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
a = 0
while a < len(stu):
    grade = int(input("请输入"+stu[a]+"的成绩："))

    if grade >=60:
        good[stu[a]] = grade
    else:
        grade < 60
        bad[stu[a]] = grade
    
    a = a + 1
print("大于60的：",good)
print("小于60的：",bad)