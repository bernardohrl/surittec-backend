import json
import unittest
from project import db
from project.api.models import User
from project.tests.base import BaseTestCase


class TestPostUserService(BaseTestCase):

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


    def test_post_user_invalid_json(self):
        with self.client:
            response = self.client.post(
                '/post_user',
                data=json.dumps({}),
                content_type='application/json',
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])


    def test_post_user_invalid_json_keys(self):
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


    def test_post_user_duplicate_username(self):
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



class TestGetUserService(BaseTestCase):

    def test_get_user(self):
        user = User(username='bernardohrl', email='bernardohrl@gmail.com', password="senha")
        db.session.add(user)
        db.session.commit()
        
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 200)
            self.assertIn('bernardohrl', data['username'])
            self.assertIn('bernardohrl@gmail.com', data['email'])


    def test_get_user_no_id(self):
        with self.client:
            response = self.client.get('/users/alkdjasldk')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist.', data['message'])


    def test_get_user_incorrect_id(self):
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist.', data['message'])


if __name__ == '__main__':
    unittest.main()
