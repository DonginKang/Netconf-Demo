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
password = 'pass'
ipv4 = '192.168.0.32'
port = 22


fullname = '       Juniper MX80 192.168.0.32'

def copy_config(m):
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    t_fname = dt+"_Core_Config.text"
    cmd = "file://var/var/home/juniper/" + t_fname    #m.copy_config(source="running", target="file:// /var/home/juniper/new_checkpoint.text")
    m.copy_config(source="running", target= cmd )
    return t_fname


def rollback_config(m2, filename):
    cmd = "file://var/var/home/juniper/"+filename
    m2.copy_config(source= cmd , target="candidate")
    m2.commit()

def commit(m):
    m.commit()
'''
def pre_show():
    with manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False ) as m:
        msg = m.command('show chassis environment' , format = 'text').tostring
        logger.info("CMD : show chassis environment     " + fullname +'\n\n' + msg +  '\n\n')
        msg = m.command('show chassis hardware' , format = 'text').tostring
        logger.info("CMD : show chassis hardware     "  + fullname +'\n\n' + msg +  '\n\n')
        msg = m.command('show chassis firmware' , format = 'text').tostring
        logger.info( "CMD : show chassis firmware     "  + fullname +'\n\n' + msg +  '\n\n')
        msg = m.command('show system processes extensive' , format = 'text').tostring
        logger.info("CMD : show system processes extensive     " +fullname + '\n\n' + msg +  '\n\n')
        msg = m.command('show log messages | last 100' , format = 'text').tostring
        logger.info("CMD : show log messages | last 100     "  +fullname + '\n\n' + msg +  '\n\n')
        msg = m.command('show interfaces terse' , format = 'text').tostring
        logger.info("CMD : show interfaces terse     "  +fullname + '\n\n' + msg +  '\n\n')
        msg = m.command('show route summary' , format = 'text').tostring
        logger.info("CMD : show route summary     " + fullname +'\n\n' + msg +  '\n\n')
        msg = m.command('show bgp summary' , format = 'text').tostring
        logger.info("CMD : show bgp summary     "  +fullname + '\n\n' + msg +  '\n\n')
        msg = m.command('show ospf neighbor' , format = 'text').tostring
        logger.info("CMD : show ospf neighbor     "+ fullname +'\n\n' + msg +  '\n\n')
        msg = m.command('show configuration' , format = 'text').tostring
        logger.info("CMD : show configuration     "  + fullname +'\n\n' + msg +  '\n\n')
        msg = m.command('show chassis hardware ' , format = 'text').tostring
        logger.info("CMD : show chassis hardware     " + fullname +'\n\n' + msg +  '\n\n')
'''


def get_initial_config(m):
    fname = "mx80aa_initial_config"
    c = m.get_config(source = 'running').tostring
    with open(fname , 'w') as f:
        f.write(c)
    return fname

def get_last_config(m):
    fname = "mx80aa_last_config"
    c = m.get_config(source = 'running').tostring
    with open(fname , 'w') as f:
        f.write(c)
    return fname

#pre_show()
#print show_chassis_hardware()
#print show_chassis_firmware()
#print show_running_config()
#print show_bgp_summary()
#print show_ospf_neighbor()
#print show_route_summary()
#print show_interfaces_terse()
#print show_log_massages()
#print show_system_processes_extensive()
