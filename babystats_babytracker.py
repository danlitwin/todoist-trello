import uuid
import json
import requests
import base64

from keybox import keybox

bt_deviceuuid = str(uuid.uuid4())

def td_request(endpoint='', method='post', **kwargs):
    url = 'https://beta.todoist.com/API/v8/' + endpoint.strip('/')
    kwargs = {k:v for k,v in kwargs.items() if v is not None}
    if method.lower() == 'get':
        response = requests.get(url, params=kwargs, headers=td_headers(method))
    else:  # elif method.lower() == 'post':
        response = requests.post(url, json=kwargs, headers=td_headers(method))
    if not response.ok:
        response.raise_for_status()
    return response.json() if response.ok else None

def bt_init(email='', password=''):
    data = {'AppInfo': {'AccountType': 0, 'AppType': 0},
        'Device': {'DeviceName': 'Unknown', 'DeviceOSInfo': 'Unknown',
            "DeviceUUID": bt_deviceuuid},
        "EmailAddress": email,
        "Password": password
    }
  
def td_headers(method='post'):
    headers = {'Authorization': 'Bearer {}'.format(keybox.todoist.key)}
    if method.lower() == 'post':
        headers['Content-Type'] = 'application/json'
        headers['X-Request-Id'] = str(uuid.uuid4())
    return headers
