import json
import unittest
from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    def test_hello_world(self):
        response = self.client.get('/')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('world', data['hello'])

    def test_post_user(self):
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'bernardo',
                    'email': 'bernardohrl@gmail.com',
                    'password': 'senha'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('bernardohrl was added!', data['message'])


if __name__ == '__main__':
    unittest.main()
