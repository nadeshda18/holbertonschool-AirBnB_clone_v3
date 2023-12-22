import unittest
from flask import Flask
from flask_cors import CORS
from api.v1.app import app


class TestApp(unittest.TestCase):
    """Test cases for the app"""

    def setUp(self):
        """Sets up the client for testing"""
        self.app = app.test_client()
        self.app.testing = True

    def test_app_creation(self):
        """Tests if the app is created successfully"""
        self.assertIsInstance(app, Flask)


class TestCORS(unittest.TestCase):
    """Test cases for CORS"""

    def setUp(self):
        """Sets up the client for testing"""
        self.app = app.test_client()
        self.app.testing = True

    def test_cors_headers(self):
        """Tests if CORS headers are set"""
        response = self.app.get('/')
        self.assertIn('Access-Control-Allow-Origin', response.headers)


if __name__ == "__main__":
    unittest.main()
