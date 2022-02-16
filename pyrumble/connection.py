import json
import httpx
from .exceptions import ClientException, NotFoundException, AuthorizationException, ServerException


class Connection:
    def __init__(self, base_url, api_key, headers=None):
        self.base_url = base_url
        self.api_key = api_key
        if headers is not None:
            self.headers = {
                "Authorization": f"Bearer {api_key}",
                **headers
            }
        else:
            self.headers = {"Authorization": f"Bearer {api_key}"}

    def __request(self, method, url, data=None, headers=None, **kwargs):
        headers = self.parse_headers(headers)
        url = self.base_url + url

        if method == "GET":
            response = httpx.get(url, headers=headers, params=kwargs)

        elif method == "POST":
            if data is None:
                raise ClientException("data kwarg cannot be none when posting")
            response = httpx.post(url, json=data, headers=self.headers, params=kwargs)

        elif method == "PUT":
            if data is None:
                raise ClientException("data kwarg cannot be none when putting")
            response = httpx.put(url, json=data, headers=self.headers, params=kwargs)

        elif method == "PATCH":
            if data is None:
                raise ClientException("data kwarg cannot be none when patching")
            response = httpx.patch(url, json=data, headers=self.headers, params=kwargs)

        elif method == "DELETE":
            if data is None:
                raise ClientException("data kwarg cannot be none when posting")
            response = httpx.delete(url, headers=self.headers, params=kwargs)
        else:
            raise ClientException("Only GET, POST, PUT, PATCH and DELETE methods allowed when making a request")

        if 200 >= response.status_code <= 300:
            return response.json()
        else:
            self.parse_error(response)

    def get(self, url, headers=None, **kwargs):
        headers = self.parse_headers(headers)
        return self.__request("GET", url, headers=headers, **kwargs)

    def post(self, url, data, headers=None, **kwargs):
        url = self.base_url + url
        headers = self.parse_headers(headers)
        return httpx.post(url, headers=headers, json=data, params=kwargs)

    def patch(self, url, data, headers=None, **kwargs):
        url = self.base_url + url
        headers = self.parse_headers(headers)
        return httpx.patch(url, headers=headers, json=data, params=kwargs)

    def put(self, url, data, headers=None, **kwargs):
        url = self.base_url + url
        headers = self.parse_headers(headers)
        return httpx.put(url, headers=headers, json=data, params=kwargs)

    def delete(self, url, headers=None, **kwargs):
        url = self.base_url + url
        headers = self.parse_headers(headers)
        return httpx.post(url, headers=headers, params=kwargs)

    def parse_headers(self, headers):
        if headers is not None and isinstance(headers, dict):
            return {**headers, **self.headers}
        return self.headers

    @staticmethod
    def parse_error(response: httpx._models.Response):
        status_code = response.status_code
        try:
            error_msg = json.loads(response.content)
        except json.JSONDecodeError:
            error_msg = response

        if status_code == 404:
            raise NotFoundException(error_msg)
        if status_code == 401:
            raise AuthorizationException(error_msg)
        elif status_code == 403:
            raise AuthorizationException(error_msg)
        elif 400 >= status_code <= 499:
            raise ClientException(error_msg)
        elif status_code >= 500:
            raise ServerException(error_msg)
