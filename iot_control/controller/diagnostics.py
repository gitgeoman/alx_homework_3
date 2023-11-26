# Ma zawierać funkcję collect_diagnostics, która przyjmie jako argument device i zwróci None
from iot.device import Device

def collect_diagnostics(device:Device)->None:
    print('Connecting to diagnostics server.')
    status = device.status_update()
    return f'Sending status update {status} to server'