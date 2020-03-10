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
    print(api_key)
    result = save_measurement(api_key, data)
    print('Done!')

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

def save_measurement(api_key: str, data: dict):
    print('Would have save this to the server:')
    print(data)

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