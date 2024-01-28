import logging
import uuid
import json
from datetime import datetime
logging.basicConfig(filename='hotel_app.log',level=logging.INFO,format='%(asctime)s,%(levelname)s,%(message)s')
class Room:
    def __init__(self,number,price,view,room_status):
        self.id_=str(uuid.uuid4())
        self.number=number
        self.price=price
        self.view=view
        self.room_status=room_status
        self.is_cleaned=True
        self.is_repaired=True
        logging.info(f'room with id {self.id_} and number  {self.number} and price {self.price},view: {self.view}, room_status: {self.room_status} is created')

    def __str__(self):
        return f'room_id: {self.id_},number: {self.number}, price: {self.price}, view: {self.view} , room_status: {self.room_status}'
    
    def set_room_status(self):
        self.statuses=input('enter the new status for your room: is_cleaned/is_repaired/is_booked/is_checked?')
        print(f'room status edited to new_status: {self.statuses}')
        logging.info(f'room status with {self.number} seted to new status: {self.statuses}')

    def schedule_room_maintenance(self):
        self.start_date=datetime.now()
        self.end_date='to 3 days later '
        self.maintenance_type=input('True or False?')
        if self.maintenance_type =='True':
            print(f'room s maintenance done from {self.start_date} to {self.end_date}') 
        elif self.maintenance_type =='False':
            print(f'room s maintenance it s not done')
        logging.info(f'the schedule room maintenance is from {self.start_date} to {self.end_date}')

    def load_from_file(filename): 
        with open (filename,'r') as file:
            dataa1=json.load(file)

            print(dataa1)

    r_dict={
    "room_id": "fb45d5c7-1322-4110-8dbb-f882ca2d61f8",
    "number": 14,
    "price": 500000,
    "view": "nature" ,
    "room_status": "is_checked"
}

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(r_dict,file,indent=4,sort_keys=True)
            print('done')

if __name__=='__main__':
    try:
        room=Room.load_from_file('roomm.json')
        logging.info('read from file')
    except FileNotFoundError:
        logging.info('file not found, creating...')
        r=Room('14',500000,'nature','is_checked')
        print(r)
    else:
        print(dataa1)

    r=Room('14',500000,'nature','is_checked')
    print(r)
    #r.set_room_status()
    #r.schedule_room_maintenance()
    try:
        Room.schedule_room_maintenance(self)
        rp=self.date_time
        print(rp)
    except NameError as error:
        print('error')
