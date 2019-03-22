class Student():
    # name='aaa'
    # age=0
    sum1=0
    # name='s'
   
    def __init__(self,name11,age):
        self.name=name11
        self.age=age
        self.__score=0
        # print(self.__dict__)
        # print(name)  访问的是形参的name，所以将形参的名字改了之后就会报错
        # self.__class__.sum1+=1
        # print(Student.sum1)
        # print('当前班级学生总数为：'+str(self.__class__.sum1))
        # print(age)
        
        # print('student:',name,age)
        # print(score)

    def do_homework(self):
        print('homework')
        print(self.name)
    @classmethod
    def plus_sum(cls):
        cls.sum1+=1
        # print(cls.sum1)
        # print(self.name)
        print(self.name)

    @staticmethod
    def add(x,y):
        print('This is a static method')
        print(x+y)
        print(self.name)
    def __scoring__(self,score):
        if score<0:
            return '不能够给别人打负分'
        self.__score=score
        print(self.name+"同学本次考试分数为："+str(self.__score))
class Printer():
    def print_file(self):
        print('name:'+self.name)
        print('age:'+str(self.age))
class StudentHomework():
    homework_name=''


student1= Student('石敢当',18)
student2=Student('dfd',90)
# result=student1.__scoring__(59)
# print(result)
# result=student1.__scoring__(-1)
# print(result)
# student1.__score=-1
# student2.__score=-2
# print(student1.__score)
print(student2._Student__score)
# r=student1.__score
# print(r)
# print(student1.__dict__)
# student1.do_homework()
# student1.plus_sum()
# Student.plus_sum()
# print(student1.__dict__)
# print(student1.age)
# print(student1.name)
# print(Student.__dict__)
# student2=Student('dhdshg',15)
# Student.plus_sum()
# student3=Student('sdfassdf',45)
# Student.plus_sum()
# student.print_file()
# student1.plus_sum()
# student2.plus_sum()
# student3.plus_sum()
# student1.add(1,2)
# print(id(student1))
# print(id(student2))
# print(id(student3))
# a=student1.__init__()
# print(a)
# print(type(a))
