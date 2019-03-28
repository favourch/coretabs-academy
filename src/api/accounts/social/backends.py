import requests
from rest_framework.exceptions import ParseError

# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry


# def retry_request():
#     session = requests.Session()
#     retry = Retry(
#         total=3,
#         read=3,
#         connect=3,
#         backoff_factor=0.3,
#         status_forcelist=(500, 502, 504),
#     )
#     adapter = HTTPAdapter(max_retries=retry)
#     session.mount('http://', adapter)
#     session.mount('https://', adapter)
#     return session

class BaseAPI:
    def request_data(self, access_token, *args, **kwargs):
        response = requests.get(url=self.API_URL, params={'access_token': access_token})

        if response.status_code == 401:
            raise ParseError('bad access token')

        data = response.json()
        return data


class GithubAPI(BaseAPI):
    name = 'github'
    API_URL = 'https://api.github.com/user'

    def get_clean_data(self, access_token):
        data = self.request_data(access_token)

        cleaned_data = {
            'uid': data['id'],
            'username': data['login'],
            'email': data['email'],
            'name': data['name'],
            'avatar_url': data['avatar_url'],
        }

        return cleaned_data


class GoogleAPI(BaseAPI):
    name = 'google'
    API_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'

    def get_clean_data(self, access_token):
        data = self.request_data(access_token)

        cleaned_data = {
            'uid': data['sub'],
            'username': data['email'].split('@', 1)[0],
            'email': data['email'],
            'name': data['name'],
            'avatar_url': data['picture'],
        }

        return cleaned_data
