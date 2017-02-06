#-*- coding: utf-8 -*-

# nxos 의 경우 sandbox를 이용해서 python code 생성
# 192.168.0.31  ID: admin , PW : cisco!2345 로 접속해서 sandbox 사용

from datetime import datetime # 시간표시를 위해서 사용
import requests
import json
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


def copy_config():
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    cmd = "checkpoint file bootflash:"+ dt +"_GW_Config"
    myheaders={'content-type':'application/json-rpc'}
    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": cmd, # copy 파일명이 시간에 따라 달라져야 하기 떄문에 변수 사용
          "version": 1
        },
        "id": 1
      }
    ]
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    return dt+"_GW_Config"  # 복사한 config 파일명을 반환

def rollback_config(file_name): #copy_config 함수 반환값  = file_name
    dt = datetime.now()
    dt = str(dt)[:19].replace(" ","_")
    cmd = "rollback running-config file bootflash:"+file_name
    myheaders={'content-type':'application/json-rpc'}
    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": cmd,
          "version": 1
        },
        "id": 1
      }
    ]

    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    return response

def last_config():

    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "copy running-config startup-config",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()


def pre_show():
    myheaders={'content-type':'application/json-rpc'}
    payload=[
	{
		"jsonrpc": "2.0",
		"method": "cli_ascii",
		"params": {
		"cmd": "show module",
		"version": 1
		},
		"id": 1
	}]
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    #보기 편하게 하기위해서 수정한 코드 그냥 return respone['result']['msg'] 만 써도 된다
    content = "CMD : show module     " + fullname+'\n\n' + str(response['result']['msg']) +  '\n\n'
    logger.info(content)

    payload=[
	{
		"jsonrpc": "2.0",
		"method": "cli_ascii",
		"params": {
		"cmd": "show version",
		"version": 1
		},
		"id": 1
	}]
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    content = "CMD : show version     " +  fullname+'\n\n' + str(response['result']['msg']) +  '\n\n'
    logger.info(content)


    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "show PROcesses CPu | i CPU",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

    content =  "CMD : show processes cpu | i cpu     " +  fullname+'\n\n' + str(response['ins_api']['outputs']['output']['body']) + '\n\n'
    logger.info(content)



    myheaders={'content-type':'application/json-rpc'}
    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli_ascii",
        "params": {
          "cmd": "show logging last 100",
          "version": 1
        },
        "id": 1
      }
    ]
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    content = "CMD : show logging last 100    " + fullname+ '\n\n' + str(response['result']['msg']) + '\n\n'



    logger.info(content)

    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli_ascii",
        "params": {
          "cmd": "show ip int br",
          "version": 1
        },
        "id": 1
      }
    ]

    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    content = "CMD : show ip int br   " + fullname+'\n\n' + str(response['result']['msg']) + '\n\n'
    logger.info(content)


    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli_ascii",
        "params": {
          "cmd": "show ip route summary",
          "version": 1
        },
        "id": 1
      }
    ]

    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    content = "CMD : show ip route summary   " +  fullname+'\n\n' + str(response['result']['msg']) + '\n\n'
    logger.info(content)

    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli_ascii",
        "params": {
          "cmd": "show ip bgp summary",
          "version": 1
        },
        "id": 1
      }
    ]

    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    content = "CMD : show ip bgp summary   " +fullname+ '\n\n' + str(response['result']['msg']) + '\n\n'
    logger.info(content)

    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli_ascii",
        "params": {
          "cmd": "show running-config",
          "version": 1
        },
        "id": 1
      }
    ]

    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    content = "CMD : show running-config   " + fullname+ '\n\n' + str(response['result']['msg']) + '\n\n'
    logger.info(content)

    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli_ascii",
        "params": {
          "cmd": "show inventory",
          "version": 1
        },
        "id": 1
      }
    ]

    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    content = "CMD : show inventory   " + fullname+ '\n\n' + str(response['result']['msg']) + '\n\n'
    logger.info(content)


def get_initial_config():
    fname = "n9kaa_initial_config"
    myheaders={'content-type':'application/json-rpc'}
    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli_ascii",
        "params": {
          "cmd": "show running-config",
          "version": 1
        },
        "id": 1
      }
    ]
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    content = str(response['result']['msg'])
    with open(fname , 'w') as f:
        f.write(content)
    return fname

def get_last_config():
    fname = "n9kaa_last_config"
    myheaders={'content-type':'application/json-rpc'}
    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli_ascii",
        "params": {
          "cmd": "show running-config",
          "version": 1
        },
        "id": 1
      }
    ]
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    content = str(response['result']['msg'])
    with open(fname , 'w') as f:
        f.write(content)
    return fname

pre_show()
