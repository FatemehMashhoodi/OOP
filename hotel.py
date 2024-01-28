import logging
from datetime import datetime
import json
import uuid
from guest import *
logging.basicConfig(filename='hotel_app.log',level=logging.INFO,format='%(asctime)s,%(levelname)s,%(message)s')

class Hotel:
    def __init__(self,name,gps,quality):
        self.name=name
        self.gps=gps
        self.quality=quality
        self.id_=str(uuid.uuid4())
        logging.info(f'there is hotel with name {self.name} and id {self.id_},quality {self.quality} from gps {self.gps}')

    def __str__(self):
        return f'hotel name :{self.name} ,hotel_id: {self.id_}, quality: {self.quality},gps: {self.gps}'
    
    def list_available_rooms(self,room_book_type):
        self.room_book_type=room_book_type
        self.lst_rooms=[1,2,3,4,5,6]
        if self.room_book_type==False:
            for i in self.lst_rooms:
                print(f'available_rooms: {i}', end=' ')
        else:
            print('available room not exsit. because those are booked already.')

    def get_guest_details(self,obj):
        print(f'guest details= name: {obj.first_name}, {obj.last_name},id: {obj.guest_id}, city: {obj.city}, age: {obj.age}')
        logging.info(f'guest details= name: {obj.first_name}, {obj.last_name},id: {obj.guest_id}, city: {obj.city}, age: {obj.age}')
    
    def summarize_daily_operations(self):
        self.hotel_ope={}
        for i in range(1,6):
            op=f'room {i} is added'
            self.hotel_ope['add_room']=op
            print(self.hotel_ope)
            logging.info(f'added the rooms: {self.hotel_ope}')

    def edit_room(self,number_room=None):
        self.number_room=number_room
        self.room={'room1':14,'room2':15,'room3':16}
        self.room['room3']=number_room
        print('rooms edited')
        print(self.room)
        logging.info(f'edited the rooms: {self.room}')




def load_from_file(filename): 
        with open (filename,'r') as file:
            data_h=json.load(file)

            print(data_h)

h_dict={
 
    "name": "cali",
      "gps": "shiraz",
        "quality": "5*",
        "id_": "04c05edb-200b-462d-a2d6-733c00452011"
        
}
def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(h_dict,file,indent=4,sort_keys=True)
            print('done')

if __name__=='__main__':
    try:
        hotel=Hotel.load_from_file('hotel.json')
        logging.info('read from file')
    except FileNotFoundError:
        logging.info('file not found, creating...')
        h=Hotel('cali','shiraz','5*')
    except IndentationError as e:
        print(e)
    except AttributeError:
        print('Hotel has no attribiute load_from_file')
    else:
        print(data_h) 

        g=Guest('ziba','rafiei','09123334567',156,55,25)
    h=Hotel('cali','shiraz','5*')
    print(vars(h))
    #h.get_guest_details(g)
    #h.summarize_daily_operations()
    #h.edit_room('22')
    #h.list_available_rooms(True)