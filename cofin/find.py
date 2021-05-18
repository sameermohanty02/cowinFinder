import requests
import json
import requests
import beepy as beep
import hashlib
import time
from datetime import datetime, timedelta
from . import bearer
from cofin import getdata

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
actual = datetime.today()
filename = 'states.csv'


def find_w_dist():
    print("\n Find Vaccine slots by Districts")
    num_days = 7
    print("\n Find Vaccine slots by Districts")
    age = input(">> Please enter the age: ")
    dist = input(">> Please enter the District Name: ").capitalize()
    data = getdata.get_dataobj(filename,dist)
    if data is not None:
        dist_id = data[2]
    else:
        print(f"No dist found with the name {dist}")
        return
    list_format = [actual + timedelta(days=i) for i in range(num_days)]
    actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]
    print(">> Starting search for Covid vaccine slots!")
    while True:
        counter = 0
        for given_date in actual_dates:

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(
                dist_id, given_date)
            response = requests.get(URL, headers=headers)
            if response.ok:
                response_to_json = response.json()
                if response_to_json['sessions']:
                    for center in response_to_json['sessions']:
                        if int(age) >= center['min_age_limit']:
                            if (center['available_capacity_dose1'] > 0 or center['available_capacity_dose2'] > 0):
                                beep.beep(sound="ping")
                                center_dict = {'Name': center['name'],
                                               'Available Capacity': center['available_capacity'],
                                               'Date': center['date'], \
                                               'Address': center['address'], 'Pincode': center['pincode']}
                                print("=" * 25)
                                for key, val in center_dict.items():
                                    print(str(key) + ' : ' + str(val))
                                print("=" * 25)
                        else:
                            pass
            else:
                print("No Response!")

        if (counter == 0):
            print("No Vaccination slot avaliable!")
        else:
            print("Search Completed!")

        dt = datetime.now() + timedelta(minutes=3)

        while datetime.now() < dt:
            time.sleep(1)


def find_w_pin():
    num_days = 7
    print("\n Find Vaccine slots by Pincode")
    age = input(">> Please enter the age: ")
    pin_code = input(">> Please enter the Pin code. Add ',' if you are entering multiple pin codes: ")
    pin_code_list = [pin.strip() for pin in pin_code.split(',')]
    list_format = [actual + timedelta(days=i) for i in range(num_days)]
    actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]
    while True:
        counter = 0

        for pinCode in pin_code_list:
            print(f"Finding Vaccine Slots for {pinCode}")
            for given_date in actual_dates:
                URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format( \
                    pinCode, given_date)

                result = requests.get(URL, headers=headers)
                if result.ok:
                    response_json = result.json()
                    if response_json["centers"]:
                        for center in response_json["centers"]:
                            for session in center["sessions"]:
                                if (session["min_age_limit"] <= int(age) and session["available_capacity_dose1"] > 0 or
                                        session["available_capacity_dose2"] > 0):
                                    beep.beep(sound="ping")
                                    center_dict = {'Name': center['name'],
                                                   'Available Capacity': center['available_capacity'],
                                                   'Date': center['date'], \
                                                   'Address': center['address'], 'Pincode': center['pincode']}
                                    print("=" * 25)
                                    for key, val in center_dict.items():
                                        print(str(key) + ' : ' + str(val))
                                    print("=" * 25)
                                else:
                                    pass
                    else:
                        pass
                else:
                    print("No Reponse")
            if (counter == 0):
                print("No Vaccination slot avaliable!")
            else:
                print("Search Completed!")

            dt = datetime.now() + timedelta(minutes=3)

            while datetime.now() < dt:
                time.sleep(1)


def find_ben():
    mobile = input("Enter your Mobile number: ")
    payload = {'mobile': mobile,
               'secret': 'U2FsdGVkX18WKV2t3YK5hRx2lRFGQMnexpIay86tP/fsALe5jpgfoXmD9negroO2kAJhiHg+Z27t18UQ5S+lSw=='}
    try:
        response = requests.post('https://cdn-api.co-vin.in/api/v2/auth/generateMobileOTP', data=json.dumps(payload),
                                 headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("An Http Error occurred while connecting to API " + str(errh))
    except requests.exceptions.ConnectionError as errc:
        print("An Error Connecting to the API occurred:")
    except requests.exceptions.Timeout as errt:
        print("A Timeout Error occurred while connecting to API")
    except requests.exceptions.RequestException as err:
        print("An Unknown Error occurred while connecting API")
    transaction_id = response.json()['txnId']
    otp = input("Enter the otp you received: ")
    otp_sha = hashlib.sha256(otp.encode()).hexdigest()
    payload_confirm = {'txnId': transaction_id, 'otp': otp_sha}
    try:
        response = requests.post('https://cdn-api.co-vin.in/api/v2/auth/validateMobileOtp',
                                 data=json.dumps(payload_confirm), headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("An Http Error occurred while connecting to API " + str(errh))
    except requests.exceptions.ConnectionError as errc:
        print("An Error Connecting to the API occurred:")
    except requests.exceptions.Timeout as errt:
        print("A Timeout Error occurred while connecting to API")
    except requests.exceptions.RequestException as err:
        print("An Unknown Error occurred while connecting API")
    myToken = response.json()['token']
    try:
        response = requests.get(
            f'https://cdn-api.co-vin.in/api/v2/appointment/beneficiaries', auth=bearer.BearerAuth(myToken),
            headers=headers
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("An Http Error occurred while connecting to API " + str(errh))
    except requests.exceptions.ConnectionError as errc:
        print("An Error Connecting to the API occurred:")
    except requests.exceptions.Timeout as errt:
        print("A Timeout Error occurred while coannecting to API")
    except requests.exceptions.RequestException as err:
        print("An Unknown Error occurred while connecting API")

    if response.ok:
        response_json = response.json()
        if response_json['beneficiaries']:
            for beneficiary in response_json['beneficiaries']:
                print("="*25)
                print("Name: "+beneficiary['name'])
                print("Beneficiary reference id: "+beneficiary['beneficiary_reference_id'])
                print("Beneficiary vaccination status: ")
                print("Beneficiary photo ID type: "+beneficiary['photo_id_type'])
                print("Beneficiary appointment details: ")
                for i in beneficiary['appointments']:
                    print(i)
                print("Beneficiary photo ID: "+beneficiary['photo_id_number'])


