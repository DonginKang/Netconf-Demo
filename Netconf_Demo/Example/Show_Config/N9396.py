from ncclient import manager

with manager.connect(host="192.168.0.34", port=22, username="admin", password = "cisco!2345", hostkey_verify=False, device_params={'name':'default'}) as m:
    c = m.get(source = 'candidate')
    print c
