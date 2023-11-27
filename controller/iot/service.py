import random
import string
from iot.devices import Device
from iot.diagnostics import collect_diagnostics
from iot.message import Message


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class IOTService:
    devices: list = []

    def register_device(self, dev: Device) -> None:
        dev.id = generate_id()
        device = dev.connect()
        IOTService.devices.append(dev)

    def unregister_device(self, device_id: str) -> None:
        for device in IOTService.devices:
            if device.id == device_id:
                device.disconnect()

    def get_device(self, device_id: str):
        for device in IOTService.devices:
            if device.id == device_id:
                IOTService.devices.remove(device)

    def run_program(self, messages: list[Message, Message]):

        for message in messages:
            print("=======RUNNING PROGRAM========")
            for device in IOTService.devices:
                if device.id == message.device_id:
                    device.send_message(message_type=message.msg_type,data=message.data)
            print("=======END OF PROGRAM========")

    def test_device(self):
        print('start test device')
        for device in IOTService.devices:
            print(collect_diagnostics(device))
