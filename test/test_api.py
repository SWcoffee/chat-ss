import json
import unittest

from fastapi.testclient import TestClient
from app import app
from test.fake_data import fake_data


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_add_token(self):
        data = {
            "email": "comm@mail.com",
            "accessToken": "123123",
            "refreshCookie": "123123"
        }

        response = self.client.post("/addsession", json=data, headers={"authkey": "test"})
        print(response.json())
        assert response.status_code == 200

    def test_get_token(self):
        data = {
            "email": "comm@mail.com"
        }
        response = self.client.post("/getsession", data=data, headers={"authkey": "test"})
        print(response.json())
        assert response.status_code == 200

    def test_refresh_token(self):
        data = {
             "email": "comm@mail.com",
            "refreshCookie": "HSrNeRn9FoflV-dDhDFfsbrolsW1-f6m0gGInxPt8c3Ye"
        }
        response = self.client.post("/refreshsession", data=data, headers={"authkey": "test"})
        print(response.json())
        assert response.status_code == 200



if __name__ == '__main__':
    unittest.main()
