import unittest
import json
from models import storage
from models.state import State
from api.v1.app import app
from api.v1.views.states import *


class TestStates(unittest.TestCase):
    """Test cases for the states route"""

    def setUp(self):
        """Sets up the client for testing"""
        self.app = app.test_client()
        self.app.testing = True

    def test_get_states(self):
        """Tests for a 200 status code"""
        response = self.app.get('/api/v1/states')
        self.assertEqual(response.status_code, 200)

    def test_get_state(self):
        """Tests for a specific state"""
        state = State(name="California")
        state.save()
        response = self.app.get(f'/api/v1/states/{state.id}')
        self.assertEqual(response.status_code, 200)

    def test_delete_state(self):
        """Tests state deletion"""
        state = State(name="Nevada")
        state.save()
        response = self.app.delete(f'/api/v1/states/{state.id}')
        self.assertEqual(response.status_code, 200)

    def test_create_state(self):
        """Tests state creation"""
        response = self.app.post('/api/v1/states', data=json.dumps(
                                {"name": "Oregon"}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_update_state(self):
        """Tests state update"""
        state = State(name="Washington")
        state.save()
        response = self.app.put(f'/api/v1/states/{state.id}', data=json.dumps(
                                {"name": "New Washington"}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
