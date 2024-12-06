# demo.py
import os
from colorama import init, Fore, Style

init()  # Initialize colorama for Windows compatibility


class ASCIIArt:
    def __init__(self):
        # Windows-compatible color setup
        self.colors = {
            'RED': Fore.RED,
            'GREEN': Fore.GREEN,
            'BLUE': Fore.BLUE,
            'YELLOW': Fore.YELLOW,
            'MAGENTA': Fore.MAGENTA,
            'CYAN': Fore.CYAN,
            'WHITE': Fore.WHITE,
            'RESET': Style.RESET_ALL
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_heart(self):
        heart = [
            "  ♥♥♥   ♥♥♥  ",
            " ♥♥♥♥♥ ♥♥♥♥♥ ",
            " ♥♥♥♥♥♥♥♥♥♥♥ ",
            "  ♥♥♥♥♥♥♥♥♥  ",
            "   ♥♥♥♥♥♥♥   ",
            "    ♥♥♥♥♥    ",
            "     ♥♥♥     ",
            "      ♥      "
        ]

        print("\n=== Colorful Heart Demo ===")
        for line in heart:
            colored_line = ""
            for char in line:
                if char == "♥":
                    colored_line += f"{Fore.RED}{char}{Style.RESET_ALL}"
                else:
                    colored_line += char
            print(colored_line)

    def draw_rainbow(self):
        rainbow_colors = [
            Fore.RED,
            Fore.YELLOW,
            Fore.GREEN,
            Fore.CYAN,
            Fore.BLUE,
            Fore.MAGENTA
        ]

        print("\n=== Rainbow Pattern ===")
        for color in rainbow_colors:
            print(f"{color}{'█' * 40}{Style.RESET_ALL}")

    def draw_pixel_art(self):
        print("\n=== Pixel Art Demo ===")
        pixel_art = [
            "    ██████    ",
            "  ██      ██  ",
            "██  ██  ██  ██",
            "██    ██    ██",
            "██  ██  ██  ██",
            "  ██      ██  ",
            "    ██████    "
        ]

        colors = [Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        for i, line in enumerate(pixel_art):
            color = colors[i % len(colors)]
            print(f"{color}{line}{Style.RESET_ALL}")


def main():
    art = ASCIIArt()
    art.clear_screen()

    print("╔════════════════════════════╗")
    print("║ ASCII Art File System Demo  ║")
    print("╚════════════════════════════╝")

    # Draw all demos
    art.draw_heart()
    art.draw_rainbow()
    art.draw_pixel_art()

    print("\nPress Enter to exit...", end='')
    input()


if __name__ == "__main__":
    main()