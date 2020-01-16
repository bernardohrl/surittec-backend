import json
import unittest
from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    def test_hello_world(self):
        response = self.client.get('/')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('world', data['hello'])


if __name__ == '__main__':
    unittest.main()