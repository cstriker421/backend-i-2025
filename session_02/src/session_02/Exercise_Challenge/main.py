class UserRegistrationSystem:
    def __init__(self):
        self.users = []

    def register_user(self, *args, **kwargs):
        """
        Registers a user with dynamic details using *args and **kwargs.
        
        *args: Variable length arguments like (name, email)
        **kwargs: Keyword arguments for additional details like (age, address)
        """
        if len(args) < 2:
            return "Please provide at least a name and an email address."
        
        # Creates a user dictionary with basic details from args
        user = {
            'name': args[0],
            'email': args[1]
        }

        # Adds additional details from kwargs
        for key, value in kwargs.items():
            user[key] = value
        
        # Adds the user to the list using list comprehension
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
