import datetime
import requests

base_url = 'https://treasured-kind-mongoose.anvil.app/_/api/'

def main():
    auth_data = get_auth_data()
    api_key = authenticate(auth_data)
    if not api_key:
        print('Invaid login')
        return


    data = get_user_data()
    #print(api_key)
    result = save_measurement(api_key, auth_data.get('email'), data)
    if result:
        print('Done!')
    else:
        print('Could not save measurement.')

def authenticate(data: dict):
    email = data.get('email')
    password = data.get('password')
    url = base_url + 'authorize'
    body = {
        "email": email,
        "password": password
    }

    resp = requests.post(url, json=body)
    if not resp.status_code == 200:
        return None
    return resp.json().get('api_key')

def get_user_data() -> dict:
    print('Enter your measurment: ')
    weight = int(input('Weight in punds: '))
    rate = int(input('Resting heart rate: '))
    recorded = datetime.date.today().isoformat()

    return {
        "weight": weight,
        "rate": rate,
        "recorded": recorded
    }

def save_measurement(api_key: str, email: str, data: dict):
    url = base_url + 'add_measurement'
    auth = {
        "email": email,
        "api_key": api_key
    }

    data.update(auth)

    resp = requests.post(url, json=data)
    print('Server response', resp.text)
    return resp.status_code == 200


def get_auth_data() -> dict:
    # Get information from the user asking email and password
    email = input('What is your email: ')
    password = input('What is your password: ')
    print()

    return {
        "email": email,
        "password": password,
    }



if __name__ == '__main__':
    main()