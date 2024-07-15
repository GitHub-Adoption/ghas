# sql injection vulnerability

def connect_to_database():
    username = "admin"  # Hardcoded credentials
    password = "password123"  # Hardcoded credentials
    print(f"Connecting to the database with username={username} and password={password}")

if __name__ == "__main__":
    connect_to_database()
