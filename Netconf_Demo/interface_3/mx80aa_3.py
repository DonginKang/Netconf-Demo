#-*- coding: utf-8 -*-
from ncclient import manager
from datetime import datetime


username = 'id'
password = 'passwd'
ipv4 = '192.168.0.32'
port = 22

interface_name = "ge-1/0/2"
description = "GW_1/3"
ip_address = "12.1.3.2/24" #12.1.3.2
ping_ip = "12.1.3.1" #12.1.3.1

fullname = '       Juniper MX80 192.168.0.32'

def config_interface(m):
    dt = datetime.now()
    dt = str(dt)[:19] # 시간
    request_set_config_interface = """
      <config>
        <configuration>
          <interfaces>
            <interface>
                <name>%s</name>
                <description>%s</description>
                <unit>
                    <name>0</name>
                    <family>
                        <inet>
                            <address>
                            <name>%s</name>
                            </address>
                        </inet>
                    </family>
                </unit>
            </interface>
          </interfaces>
        </configuration>
      </config>
    """ % (interface_name, description, ip_address)

    request_config_interface = """
    <configuration>
        <interfaces>
            <interface>
                <name>%s</name>
            </interface>
        </interfaces>
    </configuration>
    """ % (interface_name)




    m.edit_config(target='candidate', config=request_set_config_interface)
    #m.validate(source='candidate')
    #a = m.get_config(source='candidate', filter=('subtree', request_config_interface)) # 변경된 config 데이터 저장
    m.commit()
    #connection.commit()
    #connection.discard_changes()"dd"
    #logger.info(" CMD : set interfaces ge-1/0/2 decription GW_1/3        " + fullname  +"\n       set interfaces ge-1/0/2 unit 0 family inet address 12.1.3.24")
    return " CMD : set interfaces ge-1/0/2 decription GW_1/3        "+ str(dt) + fullname  +"\n       set interfaces ge-1/0/2 unit 0 family inet address 12.1.3.2/24"

def check_interface(m):
    interface_msg = m.command('show interfaces terse' , format = 'text').data_xml
    crc_msg = m.command('show interfaces ge-1/0/2 detail media | match CRC ' , format = 'text').data_xml
    dt = datetime.now()
    dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    i_pos = interface_msg.find(interface_name)
    c_pos = crc_msg.find("CRC")
    #logger.info("CMD : show interfaces terse | match %s    " % interface_name +fullname+ '\n' + interface_msg[i_pos:i_pos+100] + '\n' + 'CMD : show interfaces ge-1/0/1 detail media | match CRC' + '\n' +crc_msg[c_pos:c_pos+60])
    return "CMD : show interfaces terse | match %s    " % interface_name + str(dt) +fullname+ '\n' + interface_msg[i_pos:i_pos+100] + '\n' + 'CMD : show interfaces ge-1/0/1 detail media | match CRC' + '\n' +crc_msg[c_pos:c_pos+60]

def check_ping(m):
    dt = datetime.now()
    dt = str(dt)[:19] # 시간
    cmd = 'ping %s count 5' % ping_ip
    msg = m.command( cmd , format = 'text').tostring
    dt = datetime.now()
    dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    if len(msg) < 100:
        #logger.info("CMD : %s    " % cmd +'      ' +fullname + '\n' + "%s 로 ping 이 정상적으로 됩니다" % ping_ip)
        return "CMD : %s    " % cmd +'      ' + str(dt)+fullname + '\n' + "%s 로 ping 이 정상적으로 됩니다" % ping_ip
    #logger.info( "CMD : %s    " % cmd +'      ' +fullname + '\n' + msg)
    return "CMD : %s    " % cmd +'      ' + str(dt)+fullname + '\n' + msg

#print check_interface()
#print check_ping()
