import datetime
import svc

def main():
    auth_data = get_auth_data()
    api_key = svc.authenticate(auth_data)
    if not api_key:
        print('Invaid login')
        return


    data = get_user_data()
    print(api_key)
    result = svc.save_measurement(api_key, auth_data.get('email'), data)
    if result:
        print('Done!')
    else:
        print('Could not save measurement.')

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