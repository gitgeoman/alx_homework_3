#INTERFEJS DO OPISUJĄCY URZĄDZENIE
from abc import ABC, abstractclassmethod


class Device(ABC):
    
    @abstractclassmethod
    def connect(self)-> None:
        "base method for connection"
        
    @abstractclassmethod
    def disconnect(self)-> None:
        "base method for disconnection"

    @abstractclassmethod
    def send_message(self)->str:
        "base method for sending message"
    