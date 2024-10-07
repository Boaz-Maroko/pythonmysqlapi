from unittest import TestCase
import mysql.connector as conn
from api.main import Server
import subprocess

# A function that will be used to create server instances

# Create a server instance

def create_server_instances():
    server_instance = Server()
    return server_instance





class ServerTests(TestCase)
    # I try to make the test names as simple as possible

    def test_server_name(self):
        server = create_server_instances()
        server
    
    def test_server_start(self):
        server = create_server_instances()
        self.assertEqual(True, server.start())
    
    def test_whether_the_server_is_running(self):
        server = Server().start()
        # start_server = server.start()
        self.assertIs(True, server)

    def test_server_stopped(self):
        server = create_server_instances()
        self.assertIs(True, server.stop())
