#-*- coding: utf-8 -*-

from ncclient import manager
from datetime import datetime


username = 'id'
password = 'pass'
ipv4 = '192.168.0.32'
port = 22

bgp_name = 'eBGP_GW_1/3'
bgp_type ='external'
local_address ='12.1.3.2'
bgp_peer ='100'
neighbor = '12.1.3.1'


fullname = '       Juniper MX80 192.168.0.32'



def config_bgp(m):
    dt = datetime.now()
    dt = str(dt)[:19]
    request_set_config_interface = """
      <config>
        <configuration>
            <protocols>
                <bgp>
                    <group>
                        <name>%s</name>
                        <type>%s</type>
                        <local-address>%s</local-address>
                        <peer-as>%s</peer-as>
                        <multipath>
                            <multiple-as/>
                        </multipath>
                        <neighbor>
                            <name>%s</name>
                        </neighbor>
                    </group>
                </bgp>
            </protocols>
        </configuration>
      </config>
    """ %(bgp_name, bgp_type, local_address, bgp_peer, neighbor)


    request_config_interface = """
    <configuration>
        <protocols>
            <bgp>
                <group>
                    <name>%s</name>
                </group>
            </bgp>
        </protocols>
    </configuration>
    """ % bgp_name



    m.edit_config(target='candidate', config=request_set_config_interface)
    m.commit()
    #a = m.get_config(source='candidate', filter=('subtree', request_config_interface))
    #print connection.validate(source='candidate')
    return " CMD : set protocols bgp group eBGP_GW_1/3 type external            "+ str(dt) + fullname  +"\n       set protocols bgp group eBGP_GW_1/3 local-address 12.1.3.2" + "\n       set protocols bgp group eBGP_GW_1/3 peer-as 100" + "\n       set protocols bgp group eBGP_GW_1/3 neighbor 12.1.3.1"
    #connection.commit()
    #connection.discard_changes()

def show_bgp(m):
    msg = m.command('show bgp summary' , format = 'text').tostring
    dt = datetime.now()
    dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    return "CMD : show bgp summary     " + str(dt) +fullname+ '\n\n' + msg
