import requests
import json

def posting(cf, data):
    url = "http://{Mobius IP}:{Mobius Port}/Mobius/AIHub/"+cf+"/report"
    print(url)
    payload = {}
    payload["m2m:cin"] = {}
    payload["m2m:cin"]["con"] = data
    payload = json.dumps(payload)

    headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'IoTHubMgmt',
    'Content-Type': 'application/json; ty=4'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)