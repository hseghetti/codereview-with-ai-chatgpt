import unittest
import json
from unittest.mock import patch
import os
from main import app


class TestPostJson(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('openai.ChatCompletion.create')
    def test_post_json(self, mock_create):

        mock_create.return_value = {'choices': [{'message': {'content': 'Mocked response'}}]}

        data = {
            'commit_message': 'Test commit message',
            'commit_description': 'Test commit description',
            'commit_code_changes': 'Test commit code changes',
            'files_changed': 'Test files changed'
        }
        response = self.app.post('/post', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)


if __name__ == '__main__':
    os.environ['OPENAI_API_KEY'] = 'sk-XXXXXXX'
    unittest.main()
