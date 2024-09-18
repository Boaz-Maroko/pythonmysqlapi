import mysql.connector as conn


class Server:
    def __doc__(self):
        """
        a class representing the server object. This is similar to the
        MYSQL server running locally on your machine or anywhere else
        """

    def __init__(self, config: dict) -> None:
        """ Has the parameter config which is the configuration of the mysql server"""

        self.config = config

    def __str__(self):
        """Should return the host of the server when called as a string"""
        host = self.config['host']
        return host
    

        