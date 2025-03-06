# Dictionary to store contacts (name: phone)
contacts = {}

def main():
    """Main function to run the assistant bot with a command loop"""
    print("Welcome to the assistant bot!")
    # Dictionary mapping command names to their handler functions
    commands = {
        "hello": greet,
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "close": goodbye,
        "exit": goodbye
    }
    # Main program loop
    while True: 
        user_input = input("Enter a command: ")
        try:
            # Parse the user input into command and arguments
            cmd, *args = parse_input(user_input)
            if cmd in commands:
                # Execute the command and print the result
                print(commands[cmd](*args))
                # Exit the program if command is "close" or "exit"
                if cmd == "close" or cmd == "exit":
                    break
            else:
                print("Invalid command.", "Available commands: ", ", ".join(commands.keys()))
        except Exception as e:
            print(f"Error: {e}")


def input_error(ValueErrorMessage="Give me name and phone please.", IndexErrorMessage="Give me name and phone please.", KeyErrorMessage="Please enter a valid key"):
    """Decorator to handle input errors with different messages for different errors"""
    def input_error_closure(func):
        """Closure to handle input errors"""
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return ValueErrorMessage
            except KeyError:
                return KeyErrorMessage
            except IndexError:
                return IndexErrorMessage

        return inner
    return input_error_closure


def parse_input(input):
    """Parse user input into command and arguments"""
    cmd, *args = input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error(ValueErrorMessage="Give me name and phone please.")
def add_contact(*args):
    """Add a new contact to the contacts dictionary"""
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    else:
        contacts[name] = phone
        return "Contact added."

@input_error(ValueErrorMessage="Give me name and phone please.")
def change_contact(*args):
    """Update an existing contact's phone number"""
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    else:
        contacts[name] = phone
        return "Contact updated."

@input_error(ValueErrorMessage="Give me name please.", IndexErrorMessage="Give me name please.")
def show_phone(*args):
    """Show the phone number for a specific contact"""
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    else:
        return contacts[name]


def show_all():
    """Show all contacts in the address book"""
    return "\n".join([f"{name} - {phone}" for name, phone in contacts.items()])


def greet():
    """Return a greeting message"""
    return "How can I help you?"


def goodbye():
    """Return a farewell message"""
    return "Goodbye!"
    

if __name__ == "__main__":
    main()