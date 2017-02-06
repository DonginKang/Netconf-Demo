from ncclient import manager
import sys


with manager.connect(host='ios-xe-mgmt.cisco.com', port=10000, username='root', password = "C!sc0123", hostkey_verify=False, device_params={'name':'default'}) as m:
    c = m.get_config(source = 'running').data_xml
    with open("host.xml" , 'w') as f:
       f.write(c)
