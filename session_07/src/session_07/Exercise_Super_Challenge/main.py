import sqlite3

class User:
    def __init__(self, username, email, password):
        """
        Initializes a User object with the provided username, email, and password.
        """
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        """
        Provides a string representation of the User object for easier display.
        """
        return f"User(username={self.username}, email={self.email}, password={self.password})"


class DatabaseManager:
    def __init__(self, db_name):
        """
        Initializes the DatabaseManager with the database name.
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """
        Opens the connection to the SQLite database and creates the 'users' table if not exists.
        """
        # Connect to the SQLite database
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        # Create the 'users' table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                user TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')

        # Commit the transaction to ensure the table is created
        self.conn.commit()

        return self  # Return the DatabaseManager object itself so methods can be called on it

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the connection to the SQLite database when the context is exited.
        """
        if self.conn:
            self.conn.close()
            print(f"Connection to {self.db_name} closed.")

    def add_user(self, user):
        """
        Adds a new user to the database, using INSERT OR IGNORE to prevent duplicates.
        """
        with self as db:
            # Insert user data into the 'users' table
            db.cursor.execute('''
                INSERT OR IGNORE INTO users (user, email, password)
                VALUES (?, ?, ?)
            ''', (user.username, user.email, user.password))

            # Commit the transaction to save the changes
            db.conn.commit()

    def get_all_users(self):
        """
        Retrieves all users from the database.
        """
        with self as db:
            db.cursor.execute('SELECT * FROM users')
            return db.cursor.fetchall()


# Example usage:
if __name__ == "__main__":
    db_name = 'user_data.db'

    # Creating instances of User
    user1 = User('john_doe', 'john@example.com', 'password123')
    user2 = User('alice_smith', 'alice@example.com', 'password321')
    user3 = User('bob_jones', 'bob@example.com', 'mypassword123')

    # Using DatabaseManager to add users and retrieve all users
    with DatabaseManager(db_name) as db_manager:
        db_manager.add_user(user1)
        db_manager.add_user(user2)
        db_manager.add_user(user3)

    print("User data inserted successfully.")

    # Query the table to check if the data is inserted
    with DatabaseManager(db_name) as db_manager:
        users = db_manager.get_all_users()
        for user in users:
            print(user)  # Prints (id, user, email, password) for each user