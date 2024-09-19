from unittest import TestCase
import mysql.connector as conn
from api.main import Server

class ServerTests(TestCase):
    def test_server_callables(self):
        config = {
            "user": "pycode",
            "password": "your password",
            "host": "localhost",
        }
        server = Server(config)

        self.assertEqual(str(server), 'localhost')
        
        

