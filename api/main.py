import mysql.connector as conn
from mysql.connector import Error

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

    def check_connection(self):
        """Check if the connection to the MySQL server is successful."""
        try:
            connection = conn.connect(**self.config)
            if connection.is_connected():
                connection.close()
                return True
        except conn.InterfaceError as err:
            print(f"Interface Error: {err}")
        except conn.DatabaseError as err:
            print(f"Database Error: {err}")
        except conn.OperationalError as err:
            print(f"Operational Error: {err}")
        except conn.IntegrityError as err:
            print(f"Integrity Error: {err}")
        except conn.InternalError as err:
            print(f"Internal Error: {err}")
        except conn.ProgrammingError as err:
            print(f"Programming Error: {err}")
        except conn.NotSupportedError as err:
            print(f"Not Supported Error: {err}")
        except Error as err:
            print(f"General Error: {err}")
        return False

    def execute_query(self, query):
        """Execute a MySQL query with exception handling."""
        try:
            connection = conn.connect(**self.config)
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            connection.commit()
            cursor.close()
            connection.close()
            return results
        except conn.InterfaceError as err:
            print(f"Interface Error: {err}")
        except conn.DatabaseError as err:
            print(f"Database Error: {err}")
        except conn.OperationalError as err:
            print(f"Operational Error: {err}")
        except conn.IntegrityError as err:
            print(f"Integrity Error: {err}")
        except conn.InternalError as err:
            print(f"Internal Error: {err}")
        except conn.ProgrammingError as err:
            print(f"Programming Error: {err}")
        except conn.NotSupportedError as err:
            print(f"Not Supported Error: {err}")
        except Error as err:
            print(f"General Error: {err}")
        return None