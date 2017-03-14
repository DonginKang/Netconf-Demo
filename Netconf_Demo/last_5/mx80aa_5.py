#-*- coding: utf-8 -*-
from ncclient import manager
from datetime import datetime

"""
접속 정보 표시
"""
username = ''
password = ''
ipv4 = '192.168.0.32'
port = 22

fullname = '       Juniper MX80 192.168.0.32'


def show_interfaces_ge0(m):

    msg = m.command('show interfaces ge-1/0/0' , format = 'text').data_xml
    dt = datetime.now()
    pos = msg.find("Input")
    dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    return "CMD : show interfaces ge-1/0/0 | match rate    " + str(dt) +fullname +  '\n\n' +"  " +msg[pos:pos+91]

def show_interfaces_ge1(m):

    msg = m.command('show interfaces ge-1/0/1' , format = 'text').data_xml
    dt = datetime.now()
    pos = msg.find("Input")
    dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    return "CMD : show interfaces ge-1/0/1 | match rate    " + str(dt) + fullname + '\n\n' +"  "+msg[pos:pos+91]

def show_interfaces_ge2(m):

    msg = m.command('show interfaces ge-1/0/2' , format = 'text').data_xml
    dt = datetime.now()
    pos = msg.find("Input")
    dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    return "CMD : show interfaces ge-1/0/2 | match rate    " + str(dt) +fullname +  '\n\n' +"  "+msg[pos:pos+91]

def show_interfaces_ge4():
    with manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False ) as m:
        msg = m.command('show interfaces ge-1/0/4' , format = 'text').data_xml
        dt = datetime.now()
        pos = msg.find("Input")
        dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    return "CMD : show interfaces ge-1/0/4 | match rate    " + str(dt) + fullname + '\n\n' +"  "+msg[pos:pos+91]

def show_interfaces_ge5():
    with manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False ) as m:
        msg = m.command('show interfaces ge-1/0/5' , format = 'text').data_xml
        dt = datetime.now()
        pos = msg.find("Input")
        dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    return "CMD : show interfaces ge-1/0/5 | match rate    " + str(dt) +fullname +  '\n\n' +"  " +msg[pos:pos+91]

#print show_interfaces_ge0()
#print show_interfaces_ge1()
#print show_interfaces_ge2()
#print show_interfaces_ge4()
#print show_interfaces_ge5()
