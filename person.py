import uuid
import logging
from abc import ABC,abstractmethod

logging.basicConfig(filename='hotel_app.log',level=logging.INFO,format='%(asctime)s,%(levelname)s,%(message)s')

class Person(ABC):
    def __init__(self,first_name,last_name,contact_info,height,weight,age):
        self.id_=str(uuid.uuid4())
        self.first_name=first_name
        self.last_name=last_name
        self.contact_info=contact_info
        self.height=height
        self.weight=weight
        self.age=age
        logging.info(f'person {self.first_name} {self.last_name} created with id {self.id_} and contact {self.contact_info} and age {self.age}.')
    
    def update_contact_info(self,new_contact_info=None):
        self.contact_info=new_contact_info or self.contact_info
        print('updated')

    def __str__(self):
        return f'first_name: {self.first_name},last_name: {self.last_name},id_: {self.id_},contact_info: {self.contact_info},height: {self.height},weight: {self.weight},age: {self.age}'

@abstractmethod
def show_role(self):
        pass