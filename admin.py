import json
from person import *
from staff import *
from room import *
class Admin(Person):
    def __init__(self,first_name,last_name,contact_info,height,weight,age,role,gender):
        super().__init__(first_name,last_name,contact_info,height,weight,age)
        self.gender=gender
        self.role=role
        logging.info(f'admin {self.first_name} {self.last_name} created with id {self.id_} and contact {self.contact_info} and {self.age}.it is a {self.gender}')

    def __str__(self):
        data=super().__str__()
        return f'{data}, gender: {self.gender}'
    
    def show_role(self):
        print(f'{self.first_name} {self.last_name} is an admin.')

    def create_staff_account(self,obj):
        logging.info(f'staff {obj} created by admin {self.first_name}')
        print(f'{obj.first_name} is name of staff. ')

    def remove_staff_member(self,obj):
       logging.info(f'staff {obj} removed by admin {self.first_name}')
       del obj
       print('staff member removed')

    def update_staff_role(self,new_role=None):
        logging.info(f'role of staff {self.first_name} updated to {new_role} by admin {self.first_name}')
        self.role = new_role or self.role
        print(f'new_role: {self.role}. role of staff updated')

    def approve_maintenance_request(self,obj,maintenance_type):
        self.maintenance_type=maintenance_type
        if self.maintenance_type=='True':
            print('the  maintenance request is approved')
        elif self.maintenance_type=='False' :
            print('the maintenance request is not apporved')
        logging.info(f'maintenance request for room {obj.number} approved by admin {self.first_name}') 

    def generate_payroll_report(self,obj):
        logging.info(f'reported the payroll of staffs: {obj.salaries} ')
        self.payroll=input('True or False:')
        if self.payroll =='True':
            print(f'report: {obj.salaries}')
        elif self.payroll=='False':
            print('payroll not found')


    def load_from_file(filename): 
        with open (filename,'r') as file:
            dataa=json.load(file)

            print(dataa)

a_dict={
    "id": "8642261f-2f95-4ac9-a8ec-8315e3cfba78",
   "first_name": "Zeinab",
    "last_name": "Ahmadi", 
    "contact_info": "09059246043",
    "height": 165,
    "weight": 60, 
    "age": 30, 
    "gender": "woman", 
    "role": "admin"
}
def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(a_dict,file,indent=4,sort_keys=True)
            print('done')

if __name__=='__main__':
    try:
        admin=Admin.load_from_file('adminn.json')
        logging.info('read from file')
    except FileNotFoundError:
        logging.info('file not found, creating...')
        a = Admin('Zeinab','Ahmadi','09059246043',165,60,30,'admin','woman')
        print(a)
    except IndentationError as e:
        print(e)
    else:
        print(dataa)


    s=Staff('a','b','09383259698',189,70,30,500000)
    a=Admin('Zeinab','Ahmadi','09059246043',165,60,30,'admin','woman')
    print(vars(a))
    a.create_staff_account(s)
    a.update_staff_role('receptionist')
    r=Room(14,700,'nature','is_booked')
    a.approve_maintenance_request(r,'True')
    a.generate_payroll_report(s)
    a.show_role()
    a.remove_staff_member(s)