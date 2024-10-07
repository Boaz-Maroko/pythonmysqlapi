import mysql.connector as conn
import platform
import subprocess
from configuration import DATABASE


class Server:

    def __doc__(self):
        """
        a class representing the server object. This is similar to the
        MYSQL server running locally on your machine or anywhere else
        """

    def __init__(self) -> None:
        """ Has the parameter config which is the configuration of the mysql server"""
        self.start()

        self.os = platform.system()

    def __str__(self):
        """Should return the host of the server when called as a string"""
        server_process = self.start()
        return server_process
        
    def is_running(self):
        if self.os == "Linux":
            cmd_output = subprocess.run(['systemctl', 'status', 'mysql'], encoding="utf-8", capture_output=True)
            if 'active (running)' in cmd_output.stdout:
                return True
            elif 'inactive (dead)' in cmd_output.stdout:
                return False
        
    def start(self):
        """Checks whether the server is running and if not
        start the local server"""
        if self.is_running == False:
            if platform.system() == "Linux":
                result = subprocess.run(['systemctl', 'start', 'mysql'], encoding=("utf-8"), capture_output=True)
                if self.is_running():
                    return True
            else:
                result = subprocess.run(['net', 'start', 'mysql'], capture_output=True, encoding=True)
                if self.is_running():
                    return True
        else:
            return True
        
    
    def stop(self):
        """ checks whether the server is running and if, shuts it down"""
        if self.is_running:
            if platform.system() == "Linux":
                result = subprocess.run(['systemctl', 'stop', 'mysql'], encoding=("utf-8"), capture_output=True)

                return True if self.is_running() == False else False
            else:
                result = subprocess.run(['net', 'stop', 'mysql'], capture_output=True, encoding=True)
    
                return True if self.is_running() == False else False
    

    def connection(self):
        """ 
            Create a connection to the database using the configuration that 
            is specified in the configuration
        """
        self.start()
        connection = conn.connect(**DATABASE)
        return connection