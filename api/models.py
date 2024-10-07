from server import Server
from configuration import DB_NAME


class Database:
    # class attributes



    def __doc__():
        """represents the database instances in the server"""
    
    def __init__(self, name: str = DB_NAME):
        server = Server()
        self.name = name #The name of the created database
        self.connection = server.connection()


    def create_database(self):
        """when called creates a database"""

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(
                        f"""
            CREATE DATABASE {self.name} DEFAULT CHARACTER SET 'utf8'"""
                    )
                print(f"The Database: {self.name} was created successfully")
            except Exception as e:
                print(f"The program encountered the following errors {e}")
    
    def create_table(self, name: str = 'table'):
        with self.connection.cursor() as cursor:
            try:

                cursor.execute(
                    f"""
USE {self.name}
"""
                )
                cursor.execute(
                    f"""
CREATE TABLE {name} (name VARCHAR(20)), age INT"""
                )
            except Exception as e:
                if e == None:
                    print(f"Database table created successfully")
                else:
                    print(f"The following errors were encountered: {e}")

        
    def commit(self):
        """When called it finally saves the database object to the server
        This is a security feature to ensure that you only save to the database
        when you are sure."""
        self.create_database()
        self.create_table()


my_db = Database("somedb56556")
my_db.create_table('sometbname')
my_db.commit()



