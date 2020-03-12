from typing import Optional
import requests
import datetime

base_url = 'https://treasured-kind-mongoose.anvil.app/_/api/'

# This def return the current api_key
def authenticate(email, password) -> Optional[str]:
    url = base_url + 'authorize'
    body = {
        "email": email,
        "password": password
    }

    resp = requests.post(url, json=body)
    if not resp.status_code == 200:
        return None
    return resp.json().get('api_key')

def save_measurement(api_key: str, email: str, rate: int, weight: int, recorded: datetime.date):
    url = base_url + 'add_measurement'
    data = {
        "email": email,
        "api_key": api_key,
        "rate": rate,
        "weight": weight,
        "recorded": recorded.isoformat().split('T')[0]
    }

    resp = requests.post(url, json=data)
    print('Server response', resp.text)
    return resp.status_code == 200