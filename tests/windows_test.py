# windows_test.py
import os
import sys
from ctypes import windll


def setup_windows_terminal():
    # Enable Windows ANSI support
    kernel32 = windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


def test_display_methods():
    print("\n=== Windows Terminal Compatibility Test ===\n")

    # Method 1: CMD Style
    os.system("color")  # Enable color processing
    os.system("echo [31mTest RED using CMD[0m")

    # Method 2: PowerShell Style
    print("\n=== PowerShell Style ===")
    print("$host.ui.RawUI.ForegroundColor = 'Red'")

    # Method 3: Direct Windows API
    print("\n=== Direct Windows Characters ===")
    print("█ ▀ ▄ ■ □ ▢ ▣ ▤ ▥ ▦ ▧ ▨ ▩ ▪ ▫ ▬ ▭ ▮ ▯")

    # Method 4: Simple ASCII
    print("\n=== Basic ASCII ===")
    print("+---+")
    print("| * |")
    print("+---+")

    return True


def display_capability_info():
    print("\nTerminal Capability Info:")
    print(f"Python: {sys.version}")
    print(f"Terminal: {os.environ.get('TERM', 'Unknown')}")
    print(f"Platform: {sys.platform}")
    print(f"Output Encoding: {sys.stdout.encoding}")


if __name__ == "__main__":
    try:
        setup_windows_terminal()
        test_display_methods()
        display_capability_info()

        print("\nInteractive Test:")
        print("Do you see:")
        print("1. Basic ASCII characters? [Y/N]")
        print("2. Block characters (█)? [Y/N]")
        print("3. Any colors? [Y/N]")

    except Exception as e:
        print(f"Error: {e}")