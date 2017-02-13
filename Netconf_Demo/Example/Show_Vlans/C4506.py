from ncclient import manager

def main():

    with manager.connect(host='192.168.0.78',
                         port=22,
                         username='',
                         password='',
                         hostkey_verify=False,
                         device_params={'name': 'csr'},
                         allow_agent=False,
                         look_for_keys=False
                         ) as cisco_manager:

        vlans_filter = '''
                        <show xmlns="http://www.cisco.com/nxos:1.0">
                            <vlan>
                            </vlan>
                        </show>
                       '''

        cisco_vlans = cisco_manager.get(('subtree', vlans_filter))

        print cisco_vlans

if __name__ == '__main__':
    main()
