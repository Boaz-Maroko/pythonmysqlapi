from api.main import Server

# Step 1: Create a configuration dictionary
config = {
    "user": "new_user",
    "password": "new_password",
    "host": "localhost",
    "database": "pydatabase"
}

# Step 2: Initialize the Server class
server = Server(config)

# Step 3: Check the connection
if server.check_connection():
    print("Connection successful!")
else:
    print("Connection failed!")

# Step 4: Execute a query
query = "SELECT * FROM your_table"
results = server.execute_query(query)
if results is not None:
    for row in results:
        print(row)
else:
    print("Query execution failed!")