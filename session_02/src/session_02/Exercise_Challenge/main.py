class UserRegistrationSystem:
    def __init__(self):
        self.users = []

    def register_user(self, *args, **kwargs):
        if len(args) < 2:
            return "Please provide at least a name and an email address."
        
        user = {
            'name': args[0],
            'email': args[1]
        }

        for key, value in kwargs.items():
            user[key] = value

        self.users.append(user)
        return f"User {args[0]} registered successfully."

    def list_users(self):
        """Returns a list of all registered users."""
        return [user for user in self.users]

    def filter_users(self, **kwargs):
        """Filters users based on provided keyword arguments."""
        return [
            user for user in self.users
            if all(user.get(key) == value for key, value in kwargs.items())
        ]

# Example usage provided by ChatGPT
if __name__ == "__main__":
    system = UserRegistrationSystem()

    print(system.register_user("John Doe", "john.doe@example.com", age=25, address="123 Main St"))      # User John Doe registered successfully.
    print(system.register_user("Jane Smith", "jane.smith@example.com", age=30, address="456 Elm St"))   # User Jane Smith registered successfully.
    print(system.register_user("Alice Brown", "alice.brown@example.com", age=22))                       # User Alice Brown registered successfully.

    print("\nAll users:")
    for user in system.list_users():
        print(user)     # All users printed with name, email, age, and address correctly

    print("\nUsers aged 25:")
    for user in system.filter_users(age=25):
        print(user)     # {'name': 'John Doe', 'email': 'john.doe@example.com', 'age': 25, 'address': '123 Main St'}
