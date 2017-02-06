from ncclient import manager

def main():

    with manager.connect(host='192.168.0.32',
                         port=22,
                         username='juniper',
                         password='jun2per',
                         hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False,
                         look_for_keys=False
                         ) as cisco_manager:

        vlans_filter = '''
                        <show xmlns="http://xml.juniper.net/junos/15.1R4/junos">
                            <vlan>
                            </vlan>
                        </show>
                       '''

        cisco_vlans = cisco_manager.get('vlans_filter')

        print cisco_vlans

if __name__ == '__main__':
    main()
