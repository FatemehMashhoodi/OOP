from person import *
from room import *
from datetime import datetime
class Staff(Person):
    def __init__(self,first_name,last_name,contact_info,height,weight,age,salary):
        super().__init__(first_name,last_name,contact_info,height,weight,age)
        self.role='receptionist or houskeeping or maintenance'
        self.salaries={'s_re':600000,'s_hou':700000,'s_mai':800000}
        self.salary=salary
        logging.info(f'staff {self.first_name} {self.last_name} created with id {self.id_} and contact {self.contact_info} and {self.age} and are salaries of staffs {self.salaries}')
       
    def __str__(self):
        data=super().__str__()
        return f'{data} , role: {self.role}, salaries: {self.salaries}' 
    
    def show_role(self):
        print(f'{self.first_name} {self.last_name} is a staff.')
        
class Receptionist(Staff):
    def __init__(self,first_name,last_name,contact_info,height,weight,age,salary,ability):
        super().__init__(first_name,last_name,contact_info,height,weight,age,salary)
        self.ability=ability

    def __str__(self):
        data=super().__str__()
        return f'{data} , ability: {self.ability}'

    def book_guest(self,obj):
        self.booking=[]
        self.start_date=datetime.now()
        self.end_date='to 1 week'
        self.is_booked=input('False or True:')
        if self.is_booked=='True':
            print('room is booked already')
        elif self.is_booked=='False':
            self.booking.append(obj.number)
            print(self.booking)
            print(f'the room is booked ')
        logging.info(f'the room with {obj.number} is booked from {self.start_date} to {self.end_date}')

    def check_out_guest(self,obj,start_date,end_date):
        self.checking=[]
        self.start_date=start_date
        self.end_date=end_date
        self.is_checked=input('True or False:')
        if self.is_checked=='True':
            self.checking.append(obj.number)
            print(self.checking)
            print(f'the room checked out ')
            logging.info(f'the room with {obj.number} checked out from {self.start_date} to {self.end_date}')
        elif self.is_checked=='False':
            print('room is not checked out')
            logging.info(f'the room with {obj.number} is not checked out from {self.start_date} to {self.end_date}')

class Houskeeping(Staff):
    def __init__(self,first_name,last_name,contact_info,height,weight,age,salary,national_code):
        super().__init__(first_name,last_name,contact_info,height,weight,age,salary)
        self.national_code=national_code
        logging.info(f'created houskeeping with name {self.first_name}+{self.last_name} and national_code {self.national_code}')

    def __str__(self):
       data=super().__str__()
       return f'{data} , national_code: {self.national_code}'

    def mark_room_cleaned(self,obj):
       obj.is_cleaned=True
       print(f'room_number {obj.number}: is cleaned')
       logging.info(f'room {obj.number} marked as cleaned by housekeeper {self.first_name} and with national_code {self.national_code}')
       
    def request_cleaning_suplies(self):
        re=input('if you need to cleaning suplies? yes/no: ')
        self.suplies={'cleaning_suplies':{}}
        ls_sup=[]
        if re=='yes':
            for i in range(4):
                suplies=input('enter the 4 cleaning suplies : ')
                ls_sup.append(suplies)
                self.suplies['cleaning_suplies']=ls_sup
            print('approved the request cleaning suplies')
            print(f'cleaning suplies are the {self.suplies}')
        elif re=='no':
            print('ok')
        logging.info(f'approved the request cleaning suplies.these are {self.suplies}')

class Maintenance(Staff):
   def __init__(self,first_name,last_name,contact_info,height,weight,age,salary):
    data=super().__init__(first_name,last_name,contact_info,height,weight,age,salary)
    self.second_job='driver'
    
    def __str__(self):
        data=super().__str__()
        return f'{data} , second_job: {self.second_job}'

   def order_repair_materials(self):
       self.order_materials={'repair_materials': {}}
       mat=[]
       for i in range(4):
           materials=input('enter the 4 repair materials : ')
           mat.append(materials)
           self.order_materials['repair_materials']=mat
           print(f' repair materials are the {self.order_materials}')
           logging.info(f'these repair materials {self.order_materials} were ordered')

    def report_repair_done(self,obj):
        obj.is_repaired=True
        print('reported the repaire room')
        logging.info(f'repair reported done for Room {obj.number} by maintainer {self.first_name}')

def load_from_file(filename): 
    with open (filename,'r') as file:
        dataa2=json.load(file)

        print(dataa2)
s_dict={
 
    "first_name": "a",
    "last_name": "b",
    "id_": "a1b13dc6-9edd-4440-b614-f9907e451f8f",
    "contact_info": "09383259698",
    "height": 189,
    "weight": 70,
    "age": 30 ,
    "role": "rceptionist or houskeeping or maintenance",
    "salaries": {"s_re": 600000, "s_hou": 700000, "s_mai": 800000}
}

   
def save_to_file(self, filename):
    with open(filename, 'w') as file:
        json.dump(s_dict,file,indent=4,sort_keys=True)
        print('done')

if __name__=='__main__':
    try:
        staff=Staff.load_from_file('stafff.json')
        logging.info('read from file')
    except (FileNotFoundError,AttributeError) :
        logging.info('file not found, creating...')
        s1=Staff('a','b','09383259698',189,70,30,500000)
        print(s1)
    else:
        print(dataa2)

    s1=Staff('a','b','09383259698',189,70,30,500000)
    print(s1)
    s1.show_role()
    re=Receptionist('ab','cb','09304567878',190,90,33,123000,'python')
    r=Room('17',900,'sea','is_booked')
    re.book_guest(r)
    re.check_out_guest(r,7,8)
    ho=Houskeeping('kk','ll','0908765',150,40,20,2200,'17434547879')
    ho.mark_room_cleaned(r)
    ho.request_cleaning_suplies()
    me=Maintenance('lk','po','12345',187,80,19,2900)
    me.report_repair_done(r)
    me.order_repair_materials()

    r=Room('17',900,'sea','is_booked')
    re=Receptionist('ab','cb','09304567878',190,90,33,123000,'python')
    try:
        re.book_guest(r)
    except ValueError as e:
        print(e.__class__.__name__)
    except NameError as error :
        print(error__class__.__name__)
    else:
        print(r)
    finally:
        print('end')