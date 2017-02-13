import requests
import json

"""
Modify these please
"""
url='http://192.168.0.31/ins'
switchuser='id'
switchpassword='pass'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "ip access-list TEST ;permit ip 192.168.9.9/24 host 13.13.13.13",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
