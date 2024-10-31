# main.py

from contact_bot_manager import add_contact, change_contact, show_phone, show_all

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                print(add_contact(args[0], args[1]))
            else:
                print("Invalid format. Use: add [name] [phone]")
        elif command == "change":
            if len(args) == 2:
                print(change_contact(args[0], args[1]))
            else:
                print("Invalid format. Use: change [name] [new_phone]")
        elif command == "phone":
            if len(args) == 1:
                print(show_phone(args[0]))
            else:
                print("Invalid format. Use: phone [name]")
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
