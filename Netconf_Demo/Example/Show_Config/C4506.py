from ncclient import manager

with manager.connect(host="", port=22, username="", password = "", hostkey_verify=False, device_params={'name':'default'}) as m:
    c = m.get_config(source = 'running')
    print type(c)
#    with open("candidate.xml" , 'w') as f:
#       f.write(c)
