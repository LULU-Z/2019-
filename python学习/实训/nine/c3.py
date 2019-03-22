class Human():
    sum=0
    def __init__(self,name11,age):
        self.name=name11
        self.age=age

    def get_name(self):
        
        print(self.name)

    def do_homework(self):
        # super(Student,self).do_homework
        print('this is a paremt method')
