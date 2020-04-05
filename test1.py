# 数组
# a = (1,2,3,4,"哈哈","hehe","哦哦","anan","喔喔",True )

# # print(a)
# # 切片
# print(a[:3])   # 下标开始到3
# print(a[3:6]) # 下标3-6
# print(a[6:]) # 下标6到最后


# 元祖
a = [1,2,3,4,"哈哈","hehe","哦哦","anan","喔喔",True ]
a.append("append1")
# append追加数据到末尾
a.append("append2")
# print(a)
# 元祖一定是写好后不可以修改，而数组是可以修改的
# 元祖优点也是不可以修改，保存重要数据
a.insert(7,"insert")
# insert 插入数据到指定下标位置
# print(a)
# b = a.pop(5)
# print(b)
b = a.pop(0)
c = a.pop(0)
print(b+c)
print(a)
print(b)
xx = ["你好","不好"]
a.extend(xx)  #拼接
print(a)
print(a+xx)# 同extend合并数组
a.remove("哈哈") # 删除
print(a)

下标不要超出范围=越界
xx=[0,1,2,3]
xx=(99)
"""
python的语法
所有的方法都是小括号结尾（），比如，print(),intput(),len()
元祖，数组，字典的取值，都是用中括号，比如a[0]
元祖，数组，字典的定义，分别是(),[],{}
"""


