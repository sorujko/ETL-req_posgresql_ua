import psycopg2
import json

def get_db_connection():
    """Establishes a connection to the database and returns the connection object."""
    try:
        # Load credentials from JSON file
        with open("credentials.json", "r") as file:
            credentials = json.load(file)

        # Extract credentials
        DB_HOST = credentials["host"]
        DB_PORT = credentials["port"]
        DB_NAME = credentials["database"]
        DB_USER = credentials["user"]
        DB_PASSWORD = credentials["password"]

        # Establish connection
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Connection successful!")
        return connection

    except Exception as e:
        print(f"An error occurred: {e}")
        return None