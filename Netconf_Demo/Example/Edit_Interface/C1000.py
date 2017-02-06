from ncclient import manager
import sys
config = 'interface.xml'

with manager.connect(host='ios-xe-mgmt.cisco.com', port=10000, username='root', password = "C!sc0123", hostkey_verify=False, device_params={'name':'default'}) as m:

    with open(config) as f:
        rpc_reply = m.edit_config(target='running', config=f.read())
