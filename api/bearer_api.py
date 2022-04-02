import time
import json
import requests
from bs4 import BeautifulSoup

class Bearer:

    REDDIT_URL = "https://www.reddit.com"
    LOGIN_URL = REDDIT_URL + "/login"
    INITIAL_HEADERS = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded",
        "origin": REDDIT_URL,
        "user-agent": "Cliplace/0.1"
    }

    def __init__(self):
        self.client = requests.session()
        self.client.headers.update(self.INITIAL_HEADERS)
        print('\n===')

    def fetch_token(self, username, password):

        self.username = username
        print("> Obtaining CSRF token...")
        r = self.client.get(self.LOGIN_URL)

        time.sleep(1)

        login_get_soup = BeautifulSoup(r.content, "html.parser")
        csrf_token = login_get_soup.find("input", {"name": "csrf_token"})["value"]
        print("Logging in...")

        r = self.client.post(
            self.LOGIN_URL,
            data={"username": username,"password": password, "dest": self.REDDIT_URL, "csrf_token": csrf_token}
        )

        time.sleep(1)

        if r.status_code != 200:
            print("> X Authorization failed!")
            return ""
        else:
            print("> V Authorization successful!")

        print("> Obtaining access token...")

        r = self.client.get(self.REDDIT_URL)
        data_str = BeautifulSoup(r.content, features="html.parser").find("script", {"id": "data"}).contents[0][len("window.__r = "):-1]

        data = json.loads(data_str)

        print(">>> Logged in as " + username + "\n")

        token = data["user"]["session"]["accessToken"]
        return token

