#-*- coding: utf-8 -*-
import requests
import json
from datetime import datetime # 시간표시를 위해서 사용

"""
접속 정보 표시
"""
url='http://192.168.0.31/ins'
switchuser='admin'
switchpassword='cisco!2345'

interface = "1/3"
ip = "12.1.3.1/24" # "12.1.3.1/24"
ping_ip = '12.1.3.2'

fullname = '       Cisco 9396PX 192.168.0.31'

def config_interface():
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    msg = "interface Ethernet"+interface+ " ;no switchport ;logging event port link-status ;load-interval counter 1 5 ;ip address "+ ip+ " ;no shutdown"
    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": msg,
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    return "CMD : interface Ethernet" + interface + "   "+ str(dt) +fullname+ "\n" + "       no switchport" + "\n" + "       logging event port link-status" + "\n" +"       load-interval counter 1 5" + "\n" +"       ip address " + ip + "\n" + "       no shutdown\n"

def check_interface():
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    msg = "show ip interface brief | include "+interface+" ;show interface ethernet "+ interface+" | i CRC"
    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show_ascii",
        "chunk": "0",
        "sid": "1",
        "input": msg,
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    return "CMD : "+"show ip interface brief | include "+interface+ "   "+str(dt) +fullname+ '\n' +str(response['ins_api']['outputs']['output'][0]['body']) + '\n' + "CMD : "+"show interface ethernet "+ interface+" | i CRC" +"   " +str(dt) + '\n\n' + str(response['ins_api']['outputs']['output'][1]['body'])

def check_ping():
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    msg = "ping "+ping_ip+" count 5"
    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": msg,
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    return "CMD : "+ msg + "       " + str(dt) +fullname+ '\n\n' + str(response['ins_api']['outputs']['output']['body'])

#print check_ping()
