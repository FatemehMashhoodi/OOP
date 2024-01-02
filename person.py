from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    
    def __str__(self):
        return f'first_name:{self.first_name},last_name:{self.last_name},age:{self.age}.'
    @abstractmethod
    def info_display(self):
        pass



class Student(Person):
    def __init__(self,first_name,last_name,age,student_code,score):
        super().__init__(first_name,last_name,age)
        self.student_code=student_code
        self.score=score
    def __str__(self):
        data=super().__str__()
        return f'{data},student_code:{self.student_code},score:{self.score}.'
    def info_display(self):
        print(self.first_name,self.last_name,self.age)
    def all_info_display(self):
        data=super().__str__()
        print(f'{data},student_code:{self.student_code},score:{self.score}.')
        
        



class Employee(Person):
    def __init__(self,first_name,last_name,age,employee_code,salary):
       super().__init__(first_name,last_name,age)
       self.employee_code=employee_code
       self.salary=salary
    def __str__(self):
        data=super().__str__()
        return f'{data},employee_code:{self.employee_code},salary:{self.salary}.'
    def info_display(self):
        print(self.first_name,self.last_name,self.age)
    def all_info_display(self):
        data=super().__str__()
        print(f'{data},employee_code:{self.employee_code},salary:{self.salary}.')
        

if __name__=='__main__':
    st=Student('fatemeh','mashhoodi',22,'123',20)
    ep=Employee('narges','ahmadi',20,'124',200000)
    print(vars(st))
    print(vars(ep))
    #per=Person('ahu','rezaei',33)
    #print(vars(per))
    st.info_display()
    ep.info_display()
    print(ep)
    st.all_info_display()
    print(st)
    
        
