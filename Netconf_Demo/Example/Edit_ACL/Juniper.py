from ncclient import manager

username = 'juniper'
password = 'jun2per'
ipv4 = '192.168.0.32'
port = 22


request_set_config_interface = """
<config>
  <configuration>
    <firewall>
        <filter>
            <name>AclTest</name>
            <term>
                <name>3</name>
                <from>
                    <source-address>
                        <name>101.121.111.111/32</name>
                    </source-address>
                    <destination-address>
                        <name>101.121.111.111/32</name>
                    </destination-address>
                    <protocol>icmp</protocol>
                </from>
                <then>
                    <accept/>
                </then>
            </term>
        </filter>
    </firewall>
  </configuration>
</config>
"""

request_config_interface = """
<configuration>
    <firewall>
        <filter>
            <name>107</name>
        </filter>
</configuration>
"""



connection = manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False )

connection.edit_config(target='candidate', config=request_set_config_interface)

connection.validate(source='candidate')
connection.commit()

#print connection.get_config(source='running', filter=('subtree', request_config_interface))
