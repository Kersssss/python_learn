# -*- ecoding: utf-8 -*-
# @ModuleName: 总笔记
# @Author: Kerris
# @Time: 2023/2/9 10:59

"""----------基础语句----------"""
"""
python模块导入用(import 模块名称）
print()                         #输出

input()                         #输入

整型(int)
浮点型(float)
布尔类型(bool)
字符串(str)

----------分支结构----------
————————if语句(if语句的核心是值为True或False的表达式)

if 条件表达式1:
    代码块1
elif 条件表达式2:
    代码块2
elif 条件表达式3:
    代码块3
...
else:
    结束代码块
    
----------三元表达式----------

语句1 if 条件表达式 else 语句2
(条件表达式成立则执行语句1,不成立则执行语句2)

----------循环结构----------
————————while循环(通常需要设置一个计数器来判断循环，避免进入死循环）

while 条件表达式:
    代码段
    
————while...else...循环

while 条件表达式:
    代码块1
    代码块2
else:
    代码块3

————————for循环(将每一个可迭代对象中的每一个元素赋给临时变量，再执行循环)

for 临时变量 in 可迭代对象:
    循环体

break                           #完全结束一个循环，跳出循环执行后面的语句
continue                        #只终止本次循环，继续执行后面的循环
range(1,10,1)                   #生成从1开始10为止（不包括10），步长为1的数列
                                （1，2，3，4，5，6，7，8，9），产生的是一个迭代对象
                                 如果要产生列表，需要将生成的结果用list()函数转换

----------列表----------（单个元素）
（列表用[]来表示列表，并且用,来分隔其中的元素）
可以通过对列表元素索引的重新赋值来更换列表元素x[-2]="hello"
删除列表元素可以用del，如del x[-2]
如果不知道索引，只知道要删除的元素值，则需要使用remove()方法如x.remove("hello")
使用remove时，被删除的值无法被接收，因为remove()函数没有返回值。

列表生成式x=[i for i in range(1,100,1)]
[表达列表元素的表达式 for 自定义变量 in 可迭代对象]

————切片操作（至少删除一个元素，但将产生一个新的列表对象）
列表名[start:stop:step]
切片的结果：原列表片段的拷贝
可以在切片位置添加元素

列表的直接赋值操作是使地址指向相同，所以其中一个元素内存地址中的值改变时，同个列表
都会发生改变。

需引用import copy
浅复制x2=x.copy()               #只复制表层，内层还是和原列表相同
深复制x2=x.deepcopy()           #完全复制，有独立的内存空间，和原列表无关系

del可以删除列表，而clear()可以清空列表

x.                              #表示让python让对名为x的变量执行点后面的方法
x.append()                      #在名为x的列表的末尾添加()元素       '栈'
x.pop()                         #pop()方法不指定参数可删除列表末尾的元素，
                                 并且可以接着用它，列表就像一个数据中的栈
len(x)                          #确定名为x的列表有几个元素

x.sort()                        #对列表进行排序
x.sort(reverse=True)            #反向排序
sort排序为永久排序，无法恢复原来排序，临时排序可以用sorted()

x.insert()                      #在名为x的列表'插队'添加()元素，如(2,"world")
x.index()                       #从名为x的列表中获取（）内参数的索引
x.title()                       #把名为x的列表字符串每个单词首字母变成大写
x.upper()                       #把字符串的字母全部变为大写
x.lpwer()                       #把字符串的字母全部变为小写
x.rstrip()                      #清除字符串末尾的空白
x.lstrip()                      #清除字符串开头的空白

----------字典----------（对）
字典名={'张三':3,'李四':4,'王五':5}
字典是以'键'用：来对应值。以键值对的方式储存数据，是一个无序的序列。

字典的创建也可以用dict()创建。
dict(name='张三',age=3)
=左边的是键，右边的是值，是否使用''取决于元素的类型。

可以直接用x={}创建空字典。

————字典中元素的获取
字典名[key]
[]如果字典中不存在指定的key，则会报错。

字典名.get(key)
get()如果字典中不存在指定的key，不会报错，而是返回None,
而且可以设定默认的value，比如字典名.get('张三',3)，当字典中不存在张三时，会默认输出3。

————字典元素的新增
scores['李四']=4   (也可以用于修改值)

删除也可使用del方法

————获取字典视图
.keys()                         #获取字典中所有的key
.values()                       #获取字典中所有的values
.items()                        #获取字典中所有的key，value对 
所获取的元素的类型都是字典的类型，需要转类型，而items转类型的元素是元组。

————字典元素的遍历
for i in scores:                        #i获取的是字典当中的键
    print(i)                            #这样输出的还是键
    print(scores[i],scores.get(i))      #字典值的获取也是用[]或者get(key)
    





%                               #取余符号(数值运算时)
//                              #整除符号
**                              幂符号

\t                              #制表符
\n                              #换行符
\\                              #反斜杠\
\'                              #单引号
\"                              #双引号
\r                              #回车

%字符
详细见（https://www.cnblogs.com/nutix/p/4504899.html）

数学统计函数
min()                           #求最小值
max()                           #求最大值
sum()                           #求和
"""
