from ncclient import manager

username = 'juniper'
password = 'jun2per'
ipv4 = '192.168.0.32'
port = 22


request_set_config_interface = """
  <config>
    <configuration>
      <interfaces>
        <interface>
          <name>ge-0/0/0</name>
          <unit>
            <name>0</name>
            <family>
              <ethernet-switching>
                <port-mode>trunk</port-mode>
                <vlan>
                  <members>210</members>
                </vlan>
              </ethernet-switching>
            </family>
          </unit>
        </interface>
      </interfaces>
    </configuration>
  </config>
"""

request_config_interface = """
<configuration>
    <interfaces>
        <interface>
            <name>ge-0/0/0</name>
        </interface>
    </interfaces>
</configuration>
"""



connection = manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False )

print connection.edit_config(target='candidate', config=request_set_config_interface)

print connection.validate(source='candidate')

connection.commit()
#connection.discard_changes()

print connection.get_config(source='running', filter=('subtree', request_config_interface))
