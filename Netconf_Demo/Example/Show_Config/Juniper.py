from ncclient import manager

with manager.connect(host="192.168.0.32", port=22, username="", password = "", hostkey_verify=False, device_params={'name':'junos'}) as m:
    c = m.get_config(source = 'candidate').data_xml
   # print type(c)
    with open("host8xml" , 'w') as f:
        f.write(c)
