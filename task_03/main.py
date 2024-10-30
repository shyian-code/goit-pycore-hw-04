import os
import sys
from colorama import Fore, Style, init

# Ініціалізуємо colorama
init(autoreset=True)

def display_directory_structure(path, level=0):
    # Перевірка, чи шлях є директорією
    if not os.path.isdir(path):
        print("Вказаний шлях не є директорією або не існує.")
        return

    # Отримуємо ім'я кореневої директорії
    root_name = os.path.basename(path)

    # Виводимо кореневу директорію
    print(" " * (level * 2) + f"{Fore.BLUE}{root_name}")

    # Рекурсивно проходимо по директорії та її вмісту
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            # Виводимо піддиректорії в синьому кольорі
            print(" " * ((level + 1) * 2) + f"{Fore.BLUE}📂 {item}")
            # Рекурсивно викликаємо функцію для вкладеної директорії
            display_directory_structure(item_path, level + 2)
        else:
            # Виводимо файли в жовтому кольорі
            print(" " * ((level + 1) * 2) + f"{Fore.GREEN}📜 {item}")

if __name__ == "__main__":
    # Отримуємо шлях до директорії з аргументу командного рядка
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії.")
        sys.exit(1)

    path = sys.argv[1]
    display_directory_structure(path)
