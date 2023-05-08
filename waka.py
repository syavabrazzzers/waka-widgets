import requests
import base64


class AuthError(Exception):

    def __str__(self):
        return 'API key is not correct'


class Wakatime:
    def __init__(self, api_key: str):
        self.key = base64.b64encode(api_key.encode('ascii')).decode('ascii')
        self.base_url = 'https://wakatime.com'
        self.headers = {
            'Authorization': f'Basic {self.key}'
        }
        self.stats = self.user_stats()

    def user_stats(self):
        data = requests.request('get', f'{self.base_url}/api/v1/users/current/stats/last_7_days', headers=self.headers)
        if data.status_code == 401:
            raise AuthError
        return data.json()
