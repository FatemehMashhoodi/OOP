from person import *
class University:
    def __init__(self,name):
        self.name=name
        self.student={}
        self.employee={}
   
    def add_student(self,obj):
        if obj.student_code not in self.student:
            self.student[obj.student_code]=obj
            print('add')
        else:
            print('not add')
    def add_employee(self,obj):
        if obj.employee_code not in self.employee:
            self.employee[obj.employee_code]=obj
            print('add')
        else:
            print('not add')
    def remove_student(self,code):
        if code in self.student:
            self.student.pop(code)
            print('remove')
        else:
            print('not remove')
    def remove_employee(self,code):
        if code in self.employee:
            self.employee.pop(code)
            print('remove')
        else:
            print('not remove')
    def edit_student(self,code):
        if code in self.student:
            self.first_name=first_name
            self.last_name=last_name
            self.age=age
            self.student_code=student_code
            self.score=score
            print('edit')
        else:
            print('not edit')
    def edit_employee(self,code):
       if code in self.employee:
            self.first_name=first_name
            self.last_name=last_name
            self.age=age
            self.employee_code=student_code
            self.salary=salary
            print('edit')
       
    def search_student(self,code):
        if code in self.student:
            print(self.student[code])
        else:
            print('not found')
    def search_employee(self,code):
        if code in self.employee:
            print(self.employee[code])
        else:
            print('not found')
    def display_student(self):
        for j in u.student.values():
            print(j) 
        
    def display_employee(self):
        for k in u.employee.values():
            print(k)
       
        


if __name__=='__main__':
    u=University('fasa')
    st1=Student('fatemeh','shurian',27,'123',20)
    ep1=Employee('narges','ahmadi',20,'124',200000)
    u.add_student(st1)
    u.add_employee(ep1)
    print(u.student)
    for i in u.student.values():
        print(i)
    u.remove_student(st1)
    u.remove_employee(ep1)
    ep2=Employee('zeynab','shuli',24,'145',400000)
    u.edit_employee(ep2)
    print(ep2)
    u.search_student('123')
    u.display_student()
    print(st1)
    u.display_employee()
    print(ep1)
    
