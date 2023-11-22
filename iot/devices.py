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



