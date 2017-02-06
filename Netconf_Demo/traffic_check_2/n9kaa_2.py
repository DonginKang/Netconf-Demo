#-*- coding: utf-8 -*-

import requests
import json
from datetime import datetime # 시간표시를 위해서 사용
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
url='http://192.168.0.31/ins'
switchuser='admin'
switchpassword='cisco!2345'

fullname = '       Cisco 9396PX 192.168.0.31'


def show_int_eth1():
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show_ascii",
        "chunk": "0",
        "sid": "1",
        "input": "show int eth1/1 | i rate",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    logger.info("CMD : show int eth1/1 | i rate     "  +fullname+ '\n\n' + str(response['ins_api']['outputs']['output']['body']) +  '\n')
    return "CMD : show int eth1/1 | i rate     " + str(dt) +fullname+ '\n\n' + str(response['ins_api']['outputs']['output']['body']) +  '\n'

def show_int_eth2():
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show_ascii",
        "chunk": "0",
        "sid": "1",
        "input": "show int eth1/2 | i rate",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    logger.info("CMD : show int eth1/2 | i rate     "  +fullname+ '\n\n' + str(response['ins_api']['outputs']['output']['body']) +  '\n')
    return "CMD : show int eth1/2 | i rate     " + str(dt) +fullname+ '\n\n' + str(response['ins_api']['outputs']['output']['body']) +  '\n'

def show_int_eth5():
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show_ascii",
        "chunk": "0",
        "sid": "1",
        "input": "show int eth1/5 | i rate",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    logger.info("CMD : show int eth1/5 | i rate     " +fullname+ '\n\n' + str(response['ins_api']['outputs']['output']['body']) +  '\n')
    return "CMD : show int eth1/5 | i rate     " + str(dt) +fullname+ '\n\n' + str(response['ins_api']['outputs']['output']['body']) +  '\n'

def show_int_eth6():
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show_ascii",
        "chunk": "0",
        "sid": "1",
        "input": "show int eth1/6 | i rate",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    logger.info("CMD : show int eth1/6 | i rate     "  +fullname+ '\n\n' + str(response['ins_api']['outputs']['output']['body']) +  '\n')
    return "CMD : show int eth1/6 | i rate     " + str(dt) +fullname+ '\n\n' + str(response['ins_api']['outputs']['output']['body']) +  '\n'
