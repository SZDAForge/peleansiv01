"""
colors.py - Core color handling functionality
Manages ANSI colors and color blending operations
"""
from dataclasses import dataclass
from typing import Tuple, Optional


class ANSIColors:
    """ANSI color code constants for terminal output"""
    # Foreground Colors (Text)
    FG = {
        'BLACK': '\033[30m',
        'RED': '\033[31m',
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m',
        'MAGENTA': '\033[35m',
        'CYAN': '\033[36m',
        'WHITE': '\033[37m'
    }

    # Background Colors
    BG = {
        'BLACK': '\033[40m',
        'RED': '\033[41m',
        'GREEN': '\033[42m',
        'YELLOW': '\033[43m',
        'BLUE': '\033[44m',
        'MAGENTA': '\033[45m',
        'CYAN': '\033[46m',
        'WHITE': '\033[47m'
    }

    RESET = '\033[0m'


@dataclass
class RGBColor:
    r: int
    g: int
    b: int

    def __post_init__(self):
        self.r = max(0, min(255, self.r))
        self.g = max(0, min(255, self.g))
        self.b = max(0, min(255, self.b))

    def blend_with(self, other: 'RGBColor', factor: float) -> 'RGBColor':
        return RGBColor(
            int(self.r * (1 - factor) + other.r * factor),
            int(self.g * (1 - factor) + other.g * factor),
            int(self.b * (1 - factor) + other.b * factor)
        )

    def blend(self, other: 'RGBColor', alpha: float) -> 'RGBColor':
        """
        Blend two colors using alpha compositing

        Args:
            other: The color to blend with
            alpha: Blend factor (0.0 - 1.0)

        Returns:
            New RGBColor with blended values

        Example:
            >>> color1 = RGBColor(255, 0, 0)  # Red
            >>> color2 = RGBColor(0, 0, 255)  # Blue
            >>> blended = color1.blend(color2, 0.5)  # Purple
        """
        return RGBColor(
            r=int(self.r * (1 - alpha) + other.r * alpha),
            g=int(self.g * (1 - alpha) + other.g * alpha),
            b=int(self.b * (1 - alpha) + other.b * alpha)
        )

    def to_ansi(self) -> str:
        """
        Convert RGB color to nearest ANSI color code

        Returns:
            ANSI color code string
        """
        # Simple conversion - can be made more sophisticated
        max_component = max(self.r, self.g, self.b)
        if max_component < 85:
            return ANSIColors.FG['BLACK']
        if self.r == max_component:
            return ANSIColors.FG['RED']
        if self.g == max_component:
            return ANSIColors.FG['GREEN']
        return ANSIColors.FG['BLUE']


class ColorManager:
    """Handles color operations and conversions"""

    @staticmethod
    def create_gradient(start: RGBColor, end: RGBColor, steps: int) -> list[RGBColor]:
        """
        Create a gradient between two colors

        Example:
            >>> gradient = ColorManager.create_gradient(
            ...     RGBColor(255, 0, 0),  # Red
            ...     RGBColor(0, 0, 255),  # Blue
            ...     5
            ... )
        """
        colors = []
        for i in range(steps):
            alpha = i / (steps - 1)
            colors.append(start.blend(end, alpha))
        return colors

    @staticmethod
    def get_complementary(color: RGBColor) -> RGBColor:
        """Get the complementary color"""
        return RGBColor(
            255 - color.r,
            255 - color.g,
            255 - color.b
        )