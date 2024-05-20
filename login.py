# User credentials
username = "admin"
password = "password123"

def login():
    # Ask user for username and password
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    # Check if username and password match
    if input_username == username and input_password == password:
        print("Login successful!")
        return True
    else:
        print("Incorrect username or password. Please try again.")
        return False

# Main program
def main():
    print("Welcome to the login system!")
    # Keep asking for login until successful
    while not login():
        pass
    # Code after successful login can go here
    print("You are now logged in.")

if __name__ == "__main__":
    main()
