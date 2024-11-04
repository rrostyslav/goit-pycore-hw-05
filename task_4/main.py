def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact doesn't exist."
        except IndexError:
            return "Enter all required arguments."

    return inner


contacts = {}


@input_error
def add_contact(args):
    if len(args) < 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def get_phone(name):
    return f"{name}: {contacts[name]}"


@input_error
def show_all_contacts():
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) if contacts else "No contacts found."


def main():
    while True:
        command = input("Enter a command: ").strip()

        if command == "add":
            args = input("Enter the argument for the command\n").strip().split()
            print(add_contact(args))
        elif command == "phone":
            args = input("Enter the argument for the command\n").strip().split()
            if args:
                print(get_phone(args[0]))
            else:
                print("Enter the name of the contact.")
        elif command == "all":
            print(show_all_contacts())
        elif command.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
