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

bgp_number = "100"
neighbor_ip = "12.1.3.2"


fullname = '       Cisco 9396PX 192.168.0.31'

def config_bgp():
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "router bgp 100 ;neighbor 12.1.3.2 ;remote-as 3786 ;description # Core1 # ;address-family ipv4 unicast ;soft-reconfiguration inbound always",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    return "CMD : router bgp 100                 " + str(dt) +fullname+ "\n" + "       neighbor 12.1.3.2" + "\n" + "       remote-as 3786" + "\n" +"       description # Core1 #" + "\n" +"       address-family ipv4 unicast "  + "\n" + "       soft-reconfiguration inbound always\n"

def show_bgp():
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show_ascii",
        "chunk": "0",
        "sid": "1",
        "input": "show ip bgp summary",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    return "CMD : show ip bgp summary     " + str(dt) +fullname+   str(response['ins_api']['outputs']['output']['body'])[482:]
