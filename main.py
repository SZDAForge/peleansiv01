
from asciimatics.widgets import Frame, Layout, Button, Label, TextBox, Divider
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError
import sys


class AAFSR1:
    """AAFSR1 System (simplified for TUI integration)."""
    def __init__(self):
        self.char_map = []
        self.color_map = []

    def load(self, file_path: str) -> bool:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                header = f.readline().strip()
                if header != "AAFSR1|COMBINED":
                    raise ValueError(f"Invalid file header: {header}")

                self.char_map = []
                self.color_map = []
                for line in f:
                    if line.strip() == "":
                        continue
                    char_row, color_row = line.split("|")
                    self.char_map.append(list(char_row))
                    self.color_map.append(color_row.split())
            return True
        except Exception as e:
            print(f"Error loading file: {e}")
            return False

    def save(self, file_path: str) -> bool:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("AAFSR1|COMBINED\n")
                for char_row, color_row in zip(self.char_map, self.color_map):
                    f.write("".join(char_row) + "|" + " ".join(color_row) + "\n")
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False

    def render(self) -> str:
        try:
            output = []
            for y in range(len(self.char_map)):
                line = ""
                for x in range(len(self.char_map[0])):
                    char = self.char_map[y][x]
                    color = self.color_map[y][x]
                    fg = int(color[:2], 16)
                    bg = int(color[2:], 16)
                    line += f"\033[38;5;{fg}m\033[48;5;{bg}m{char}"
                output.append(line + "\033[0m")
            return "\n".join(output)
        except Exception as e:
            print(f"Error rendering art: {e}")
            return ""

    @staticmethod
    def example():
        art = AAFSR1()
        art.char_map = [
            "   ____   ",
            "  /    \\  ",
            " / CGA  \\ ",
            " \\      / ",
            "  \\____/  "
        ]
        art.color_map = [
            "00 4B 4B 4B 00".split(),
            "00 35 00 35 00".split(),
            "00 C7 C7 C7 00".split(),
            "00 35 00 35 00".split(),
            "00 4B 4B 4B 00".split()
        ]
        return art

class AAFSRApp(Frame):
    def __init__(self, screen):
        super(AAFSRApp, self).__init__(screen,
                                       screen.height,
                                       screen.width,
                                       has_border=True,
                                       title="AAFSR TUI Editor")
        self.aafsr = AAFSR1()
        self.log = TextBox(5, as_string=True)
        self.log.disabled = True

        # Layout
        layout = Layout([1, 1, 1])
        self.add_layout(layout)

        layout.add_widget(Button("Load File", self._load_file), column=0)
        layout.add_widget(Button("Save File", self._save_file), column=1)
        layout.add_widget(Button("Render", self._render_file), column=2)
        layout.add_widget(Divider())

        layout.add_widget(Label("Character Map:"))
        self.char_map_editor = TextBox(10, as_string=True)
        layout.add_widget(self.char_map_editor, column=0)

        layout.add_widget(Label("Color Map:"))
        self.color_map_editor = TextBox(10, as_string=True)
        layout.add_widget(self.color_map_editor, column=1)

        layout.add_widget(Label("Rendered Output:"))
        self.rendered_output = TextBox(10, as_string=True)
        self.rendered_output.disabled = True
        layout.add_widget(self.rendered_output, column=2)

        log_layout = Layout([1])
        self.add_layout(log_layout)
        log_layout.add_widget(Label("Log:"))
        log_layout.add_widget(self.log)

        self.fix()

    def _load_file(self):
        self._add_log("Load File button pressed.")
        file_path = "example.aafsr"
        if self.aafsr.load(file_path):
            self.char_map_editor.value = "\n".join("".join(row) for row in self.aafsr.char_map)
            self.color_map_editor.value = "\n".join(" ".join(row) for row in self.aafsr.color_map)
            self._add_log(f"Loaded file: {file_path}")
        else:
            self._add_log(f"Failed to load file: {file_path}")
        self.fix()  # Refresh frame

    def _save_file(self):
        self._add_log("Save File button pressed.")
        file_path = "output.aafsr"
        self.aafsr.char_map = [list(row) for row in self.char_map_editor.value.splitlines()]
        self.aafsr.color_map = [row.split() for row in self.color_map_editor.value.splitlines()]
        if self.aafsr.save(file_path):
            self._add_log(f"Saved file: {file_path}")
        else:
            self._add_log(f"Failed to save file: {file_path}")
        self.fix()  # Refresh frame

    def _render_file(self):
        self._add_log("Render button pressed.")
        self.aafsr.char_map = [list(row) for row in self.char_map_editor.value.splitlines()]
        self.aafsr.color_map = [row.split() for row in self.color_map_editor.value.splitlines()]
        rendered = self.aafsr.render()
        self.rendered_output.value = rendered
        self.fix()  # Refresh frame to update rendered output
        self._add_log("Rendered output updated.")

    def _add_log(self, message):
        current_log = self.log.value or ""
        self.log.value = current_log + f"{message}\n"
        self.fix()  # Refresh frame to show log updates

def cli_app(screen):
    app = AAFSRApp(screen)
    scene = Scene([app], -1)
    screen.play([scene])


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(cli_app)
            break
        except ResizeScreenError:
            pass
