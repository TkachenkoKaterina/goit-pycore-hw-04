import sys
from pathlib import Path
from colorama import init, Fore, Style, Back

print(sys.argv)
def print_directory_structure(path, indent=''):
    for item in sorted(path.iterdir()):
        print("item: ", item)
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
            print_directory_structure(item, indent + '  ')
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

def main():
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(f"{Back.YELLOW}Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.")
        sys.exit(1)

    path_str = sys.argv[1]
    path = Path(path_str)

    if not path.exists():
        print(f"{Back.RED}Шлях {path} не існує.")
        sys.exit(1)
    if not path.is_dir():
        print(f"{Back.MAGENTA}Шлях {path} не веде до директорії.")
        sys.exit(1)

    print_directory_structure(path)

if __name__ == "__main__":
    main()
