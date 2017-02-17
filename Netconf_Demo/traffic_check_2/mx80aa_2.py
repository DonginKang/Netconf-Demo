#-*- coding: utf-8 -*-

from ncclient import manager
from datetime import datetime
import logging


logger = logging.getLogger('log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr = logging.FileHandler('/home/vagrant/netconf_demo/log/show.log')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)


"""
접속 정보 표시
"""
username = 'id'
password = 'passwd'
ipv4 = '192.168.0.32'
port = 22


fullname = '       Juniper MX80 192.168.0.32'


def show_interfaces_ge0(m):
    msg = m.command('show interfaces ge-1/0/0 | match rate ' , format = 'text').tostring
    a = str(msg)
    b = a[863:955] # | match rate 명령어가 먹히지 않아서 프로그래밍으로 특정 부분만 보여주게 함
    dt = datetime.now()
    dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    #logger.info("CMD : show interfaces ge-1/0/0 | match rate     " +fullname+ '\n' + b +  '\n')
    return "CMD : show interfaces ge-1/0/0 | match rate     " + str(dt) +fullname+ '\n' + b +  '\n'

def show_interfaces_ge1(m):
    msg = m.command('show interfaces ge-1/0/1 | match rate ' , format = 'text').tostring
    a = str(msg)
    b = a[863:955]
    dt = datetime.now()
    dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    #logger.info("CMD : show interfaces ge-1/0/1 | match rate     "  +fullname+  '\n' + b +  '\n')
    return "CMD : show interfaces ge-1/0/1 | match rate     " + str(dt) +fullname+  '\n' + b +  '\n'

def show_interfaces_ge4():
    with manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False ) as m:
        msg = m.command('show interfaces ge-1/0/4 | match rate ' , format = 'text').tostring
        a = str(msg)
        b = a[863:955]
        dt = datetime.now()
        dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    logger.info("CMD : show interfaces ge-1/0/4 | match rate     "  +fullname+  '\n' + b  +  '\n')
    return "CMD : show interfaces ge-1/0/4 | match rate     " + str(dt) +fullname+  '\n' + b  +  '\n'

def show_interfaces_ge5():
    with manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False ) as m:
        msg = m.command('show interfaces ge-1/0/5 | match rate ' , format = 'text').tostring
        a = str(msg)
        b =  a[863:955]
        dt = datetime.now()
        dt = str(dt)[:19] # 시간 데이터를 조작하기 쉽게 str 형태로 바꾸고, 필요없는 뒷부분 내용은 버림
    logger.info("CMD : show interfaces ge-1/0/5 | match rate     "  +fullname+  '\n' + b +  '\n')
    return "CMD : show interfaces ge-1/0/5 | match rate     " + str(dt) +fullname+  '\n' + b +  '\n'



#print show_interfaces_ge0()
#print show_interfaces_ge1()
#print show_interfaces_ge4()
#print show_interfaces_ge5()
