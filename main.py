from iot.service import IOTService
from iot.devices import Hue_light
from iot.message import Message,MessageType

if __name__ == '__main__':
    # tworzy instancję IOTService
    iot_service = IOTService()

    # tworze instancje dostepnych urzadzeń
    hue_light = Hue_light()

    # rejestruje urzadzenia
    iot_service.register_device(dev=hue_light)

    # lista zarejestrowanych urzadzeń
    print(len(iot_service.devices))

    #testuje urządzenia
    iot_service.test_device()

    # tworzy programy (listy Message)
    lista_messagy =[
        Message(device_id=iot_service.devices[0].id, msg_type=MessageType.SWITCH_ON),
        Message(device_id=iot_service.devices[0].id, msg_type=MessageType.CHANGE_COLOR),
        Message(device_id=iot_service.devices[0].id, msg_type=MessageType.SWITCH_OFF),
    ]

    # uruchamiam programy
    iot_service.run_program(messages=lista_messagy)

    # wyrejestrowanie urządzeń
    for device in iot_service.devices:
        iot_service.unregister_device(device.id)

    # usuwa urzadzenia
    for device in iot_service.devices:
        iot_service.get_device(device.id)

    # konczy program