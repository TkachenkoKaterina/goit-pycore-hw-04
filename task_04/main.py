from colorama import init, Fore, Style, Back

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return f"{Back.GREEN}Contact added.{Style.RESET_ALL}"
    except ValueError:
        return f"{Back.YELLOW}Invalid command format. Use 'add <імя> <телефон>'.{Style.RESET_ALL}"

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f"{Back.GREEN}Contact changed.{Style.RESET_ALL}"
        else:
            return f"{Back.RED}Contact not found.{Style.RESET_ALL}"
    except ValueError:
        return f"{Back.YELLOW}Invalid command format. Use 'change <імя> <новий_телефон>'.{Style.RESET_ALL}"
    
def get_phone_by_username(args, contacts):
    try:
        if len(args) != 1:
            return f"{Back.YELLOW}Invalid command format. Use 'phone <імя>'.{Style.RESET_ALL}"
        
        name = args[0]
        if name in contacts:
            return f"{Back.GREEN}Номер телефону {name}: {contacts[name]}{Style.RESET_ALL}"
        else:
            return f"{Back.RED}Contact not found.{Style.RESET_ALL}"
    except IndexError:
        return f"{Back.YELLOW}Invalid command format. Use 'phone <імя>'.{Style.RESET_ALL}"
    
def get_all_phones(contacts):
    if len(contacts) == 0:
        return f"{Back.RED}Книга контактів порожня.{Style.RESET_ALL}"
    else:
        return f"{Back.GREEN}Всі контакти: {contacts}{Style.RESET_ALL}"

def main():
    contacts = {}
    print(f"{Fore.GREEN}Welcome to the assistant bot!{Style.RESET_ALL}")
    while True:
        user_input = input(f"{Fore.CYAN}Enter a command: {Style.RESET_ALL}")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Fore.MAGENTA}Good bye!{Style.RESET_ALL}")
            break
        elif command == "hello":
            print(f"{Fore.GREEN}How can I help you?{Style.RESET_ALL}")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone_by_username(args, contacts))
        elif command == "all":
            print(get_all_phones(contacts))
        else:
            print(f"{Fore.RED}Invalid command.{Style.RESET_ALL} Choose from: {Back.LIGHTMAGENTA_EX}hello, add, change, phone, all, close, exit{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
