import mysql.connector


class ConnectDatabase:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect_database(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return "Connected!"
        except Exception as e:
            return f"Connection not found!! {e}"
        finally:
            if 'conn' in locals() and conn:
                conn.close()
                print("Connection closed")
    
    def get_product():

