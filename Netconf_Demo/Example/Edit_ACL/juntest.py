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
            <name>acltest</name>
            <term>
                <name>3</name>
                <from>
                    <source-address>
                        <name>10.10.10.10/32</name>
                    </source-address>
                    <destination-address>
                        <name>11.11.11.11/32</name>
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



connection = manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False )

print connection.edit_config(target='candidate', config=request_set_config_interface)

print connection.validate(source='candidate')
connection.commit()



