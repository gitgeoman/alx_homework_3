#klasy opisujące urządzenia
from iot.device import Device
from iot.message import MessageType

#hue light 
class Hue_light(Device):
    
    def connect(self):
        print('Connecting to Hue Light')
    
    def disconnect(self):
        print('Disconnectiong Hue Light')
        
    def send_message(self, message_type: MessageType, data:str)->None:
        print(f'Hue light handling message of type {message_type.name} with data [{data}]')
        
    def status_update(self):
        return 'Hue_light_status_ok'


#Speaker
class Remote_Speaker(Device):
    
    def connect(self):
        print('Connecting to Remote Speaker')
    
    def disconnect(self):
        print('Disconnectiong Remote Speaker')
        
    def send_message(self, message_type: MessageType, data:str)->None:
        print(f'Remote Speaker handling message of type {message_type.name} with data [{data}]')
        
    def status_update(self):
        return 'Remote_speaker_status_ok'

#Music player 
class Music_Player(Device):
    
    def connect(self):
        print('Connecting to Music Player')
    
    def disconnect(self):
        print('Disconnectiong Music Player')
        
    def send_message(self, message_type: MessageType, data:str)->None:
        print(f'Music Player handling message of type {message_type.name} with data [{data}]')
        
    def status_update(self):
        return 'Music Player_status_ok'
    
#Music player 
class Rolety(Device):
    
    def connect(self):
        print('Connecting to Rolety')
    
    def disconnect(self):
        print('Disconnectiong Rolety')
        
    def send_message(self, message_type: MessageType, data:str)->None:
        print(f'Rolety handling message of type {message_type.name} with data [{data}]')
        
    def status_update(self):
        return 'Rolety_status_ok'