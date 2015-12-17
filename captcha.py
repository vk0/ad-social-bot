import requests
import base64


class CaptchaSolver:
    def __init__(self):
        self.__key = '9fa8de6f0e99f84494419ac163c1fa78'
        self.__solve_url = 'http://2captcha.com/in.php'
        self.__get_url = 'http://2captcha.com/res.php'

    def solve(self, captcha_url):
        solve_params = {
            'key': self.__key,
            'method': 'base64',
            'body': self.__encode_captcha(captcha_url),
        }
        try:
            solve_response = requests.post(self.__solve_url, data=solve_params).content
            success, solved_captcha_id = solve_response.decode('utf-8').split('|')
            if success != 'OK':
                return False, None
            get_params = {
                'key': self.__key,
                'action': 'get',
                'id': solved_captcha_id,
            }
            while True:
                get_response = requests.get(self.__get_url, params=get_params).content
                if get_response != b'CAPCHA_NOT_READY':
                    break
            success, solved_captcha = get_response.decode('utf-8').split('|')
            if success != 'OK':
                return False, None
            return True, solved_captcha
        except:
            return False, None

    def __encode_captcha(self, captcha_url):
        return base64.b64encode(requests.get(captcha_url).content)
