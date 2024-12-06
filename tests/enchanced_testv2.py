# enhanced_demo.py
import os
import time
from colorama import init, Fore, Back, Style

init()


class ASCIIArtSystem:
    def __init__(self):
        self.colors = {
            'RED': Fore.RED,
            'GREEN': Fore.GREEN,
            'BLUE': Fore.BLUE,
            'YELLOW': Fore.YELLOW,
            'MAGENTA': Fore.MAGENTA,
            'CYAN': Fore.CYAN
        }

    def animate_loading(self):
        frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        print("\n=== Loading Animation ===")
        for _ in range(20):
            for frame in frames:
                print(f"\r{Fore.CYAN}{frame} Processing...{Style.RESET_ALL}", end='')
                time.sleep(0.1)
        print("\nComplete!")

    def draw_folder_structure(self):
        print(f"\n{Fore.YELLOW}=== File System Visualization ==={Style.RESET_ALL}")
        structure = [
            "📁 Project",
            "├─📁 src",
            "│ ├─📄 main.py",
            "│ ├─📁 utils",
            "│ │ └─📄 helpers.py",
            "│ └─📁 assets",
            "├─📁 docs",
            "└─📁 tests"
        ]
        for line in structure:
            print(f"{Fore.GREEN}{line}{Style.RESET_ALL}")

    def draw_animated_box(self):
        print(f"\n{Fore.CYAN}=== Animated Box ==={Style.RESET_ALL}")
        box = [
            "┌───────────┐",
            "│           │",
            "│           │",
            "└───────────┘"
        ]

        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        for color in colors:
            os.system('cls' if os.name == 'nt' else 'clear')
            for line in box:
                print(f"{color}{line}{Style.RESET_ALL}")
            time.sleep(0.5)


def main():
    art_system = ASCIIArtSystem()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.CYAN}╔══════════════════════════════╗")
        print(f"║  ASCII Art File System Studio  ║")
        print(f"╚══════════════════════════════╝{Style.RESET_ALL}")

        print("\nSelect a demo:")
        print(f"{Fore.GREEN}1. Loading Animation")
        print("2. File System Tree")
        print("3. Animated Box")
        print(f"4. Exit{Style.RESET_ALL}")

        choice = input(f"\n{Fore.YELLOW}Enter your choice (1-4): {Style.RESET_ALL}")

        if choice == '1':
            art_system.animate_loading()
        elif choice == '2':
            art_system.draw_folder_structure()
        elif choice == '3':
            art_system.draw_animated_box()
        elif choice == '4':
            print(f"\n{Fore.CYAN}Thanks for using ASCII Art File System Studio!{Style.RESET_ALL}")
            break

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()