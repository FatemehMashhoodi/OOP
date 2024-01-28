from person import *
from datetime import datetime 
class Guest(Person):
    def __init__(self,first_name,last_name,contact_info,height,weight,age):
        super().__init__(first_name,last_name,contact_info,height,weight,age)
        self.city='ahvaz'
        self.guest_id=str(uuid.uuid4())
        logging.info(f'guest is approved with {self.first_name} {self.last_name} and with id {self.id_} from city {self.city}')
    
    def __str__(self):
        data=super().__str__()
        return f'{data}, city: {self.city} '
    
    def show_role(self):
        print(f'{first_name} {self.last_name} is a guest.')

    
    def request_room_booking(self,room_type):
        self.bookings={}
        self.start_date=datetime.now()
        if room_type=='False':
            num_room=int(input('what is number of room you want to book? '))
            self.bookings['room_booking']=num_room
            print(f' {self.bookings} from date {self.start_date}')
            logging.info(f'room  booked by {self.first_name} from {self.start_date} ')
        elif room_type=='True':
            print('room is not empty')
    
    def amend_booking(self,booking_id,room_number):
        self.booking_id=booking_id
        self.room_number=room_number
        self.id_book=['123b','132a','189c']
        self.r_booking={}   
        self.new_start_date=datetime.now()
        self.new_end_date='to 2 week'
        for i in self.id_book:
            if i!=booking_id:
                self.r_booking['new room booking']=room_number
                print('booking amended')
                print(self.r_booking)
            else:
                print('not amended') 
                logging.info(f'booking {self.booking_id} amended by {self.first_name} to start on {self.new_start_date} and end on {self.new_end_date}')
            break  

    def cancel_booking(self, booking_id):
        self.booking_id=booking_id
        self.start_date=datetime.now()
        self.id_book=['123b','132a','189c']
        for j in self.id_book:
            if booking_id==j:
                del booking_id
                print('booking_id deleted')
                logging.info(f'booking {self.booking_id} cancelled by {self.first_name} from time {self.start_date}')
            elif booking_id!=j:
                print('not cancel')
            break

    def give_feedback(self):
        feedback_text=input('room booking,amend booking,cancel booking?')
        if feedback_text =='room booking':
            request=Guest.request_room_booking(self,room_type='False')
            logging.info(f'feedback for request_room_booking: {request}')
        elif feedback_text=='amend booking':
            amend=Guest.amend_booking(self,booking_id='123',room_number=3)
            logging.info(f'feedback for amend_booking: {amend}')
        elif feedback_text=='cancel booking':
            cancel=Guest.cancel_booking(self,booking_id='123b')
            logging.info(f'feedback for cancel_booking: {cancel}')
        else:
            print('feedback_text not found')


    def load_from_file(filename): 
        with open (filename,'r') as file:
            dataa3=json.load(file)

            print(dataa3)
g_dict={
    "first_name": "ziba",
    "last_name": "rafiei",
    "id_": "89233d8e-3e5c-422d-aa07-a9305f00b56c",
    "contact_info": "09123334567",
    "height": 156,
    "weight": 55,
    "age": 25, 
    "city": "ahvaz"
}

   
def save_to_file(self, filename):
       with open(filename, 'w') as file:
            json.dump(g_dict,file,indent=4,sort_keys=True)
            print('done')

if __name__=='__main__':
    try:
        guest=Guest.load_from_file('guestt.json')
        logging.info('read from file')
    except (FileNotFoundError,AttributeError) :
        logging.info('file not found, creating...')
        g=Guest('ziba','rafiei','09123334567',156,55,25)
        print(g)
    else:
        print(dataa3)

    g=Guest('ziba','rafiei','09123334567',156,55,25)
    print(g)
    #g.request_room_booking('False')
    #g.amend_booking('123',3)
    #g.cancel_booking('123b')
    #g.give_feedback()
    #g.get_guest_details('890')
    try:
        g=Guest('ziba','rafiei','09123334567',156,55)
    except TypeError as e:
        print(f'error: {e.__class__.__name__}')
