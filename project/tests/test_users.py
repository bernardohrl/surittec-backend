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
                '/post_user',
                data=json.dumps({
                    'username': 'bernardohrl',
                    'email': 'bernardohrl@gmail.com',
                    'password': 'senha'
                }),
                content_type='application/json',
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('bernardohrl was added!', data['message'])


    def test_add_user_invalid_json(self):
        with self.client:
            response = self.client.post(
                '/post_user',
                data=json.dumps({}),
                content_type='application/json',
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])


    def test_add_user_invalid_json_keys(self):
        with self.client:
            response = self.client.post(
                '/post_user',
                data=json.dumps({
                    'username': 'bernardohrl',
                    'email': 'bernardohrl@gmail.com'
                }),
                content_type='application/json',
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])


    def test_add_user_duplicate_username(self):
        with self.client:
            self.client.post(
                '/post_user',
                data=json.dumps({
                    'username': 'bernardohrl',
                    'email': 'bernardohrl2@gmail.com',
                    'password': 'senha'
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/post_user',
                data=json.dumps({
                    'username': 'bernardohrl',
                    'email': 'bernardohrl3@gmail.com',
                    'password': 'senha'
                }),
                content_type='application/json',
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Sorry. That username already exists.', data['message'])



if __name__ == '__main__':
    unittest.main()
