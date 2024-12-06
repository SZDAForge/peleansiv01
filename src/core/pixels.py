# src/core/pixels.py
from dataclasses import dataclass


@dataclass
class Pixel:
    char: str
    color: str  # ANSI color code
    opacity: float = 1.0

    # ANSI color constants
    COLORS = {
        'BLACK': '\033[30m',
        'RED': '\033[31m',
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m',
        'MAGENTA': '\033[35m',
        'CYAN': '\033[36m',
        'WHITE': '\033[37m',
        'RESET': '\033[0m',
        # Bright versions
        'BRIGHT_RED': '\033[91m',
        'BRIGHT_GREEN': '\033[92m',
        'BRIGHT_YELLOW': '\033[93m',
        'BRIGHT_BLUE': '\033[94m',
        'BRIGHT_MAGENTA': '\033[95m',
        'BRIGHT_CYAN': '\033[96m',
        'BRIGHT_WHITE': '\033[97m',
    }

    def __post_init__(self):
        self.opacity = max(0.0, min(1.0, self.opacity))
        self.char = str(self.char)[0] if self.char else ' '
        if self.color not in self.COLORS:
            self.color = 'WHITE'

    def to_string(self) -> str:
        return f"{self.COLORS[self.color]}{self.char}{self.COLORS['RESET']}"

    @classmethod
    def create_colored(cls, char: str, color_name: str) -> 'Pixel':
        """Create a pixel with a predefined color name"""
        return cls(char, color_name)


# Example usage:
def demo():
    """Demonstrate pixel capabilities"""
    # Create a heart in different colors
    heart = [
        "  ♥♥  ♥♥  ",
        " ♥♥♥♥♥♥♥ ",
        " ♥♥♥♥♥♥♥ ",
        "  ♥♥♥♥♥  ",
        "   ♥♥♥   ",
        "    ♥    "
    ]

    colors = ['RED', 'BRIGHT_RED', 'MAGENTA', 'BRIGHT_MAGENTA']
    color_idx = 0

    print("\nColored Heart Demo:")
    print("==================")

    for line in heart:
        for char in line:
            if char == '♥':
                pixel = Pixel.create_colored(char, colors[color_idx % len(colors)])
                print(pixel.to_string(), end='')
            else:
                print(char, end='')
        print()
        color_idx += 1


if __name__ == "__main__":
    demo()