# core.py
# =======
"""
Core ASCII File System Designer
=============================

Main component handling file system visualization and processing.

Flow:
    Input → Validate → Process → Apply Effects → Render

Example structure:
    root/
    ├── folder1/
    │   ├── file1.txt
    │   └── file2.txt
    └── folder2/
        └── file3.txt

ASCII representation:
    ╔═══════╗
    ║ root  ║
    ╠═══════╣
    ║folder1║ ──── [file1.txt]
    ║       ║ ──── [file2.txt]
    ╠═══════╣
    ║folder2║ ──── [file3.txt]
    ╚═══════╝
"""

import os
from typing import Dict, List, Optional
from .templates import TemplateManager
from .effects import EffectProcessor
from .validator import StructureValidator


class ASCIIFileSystemDesigner:
    def __init__(self):
        """Initialize the ASCII File System Designer with components"""
        self.template_mgr = TemplateManager()
        self.effect_processor = EffectProcessor()
        self.validator = StructureValidator()

        # Design configurations
        self.config = {
            'max_depth': 10,
            'indent': 2,
            'line_chars': {
                'vertical': '│',
                'horizontal': '─',
                'corner': '└',
                'branch': '├'
            },
            'decorators': {
                'folder': '▶',
                'file': '▷',
                'link': '↷'
            }
        }

    def process_directory(self, path: str, template: str = 'default') -> Dict:
        """
        Process directory and create ASCII representation

        Args:
            path: Directory path to process
            template: Template name to apply

        Returns:
            Dictionary containing processed structure

        Example:
            {
                'structure': [...],  # ASCII lines
                'metadata': {...},   # Additional info
                'effects': [...]     # Applied effects
            }
        """
        # Validate input path
        if not os.path.exists(path):
            raise FileNotFoundError(f"Path not found: {path}")

        # Load template
        template_data = self.template_mgr.get_template(template)

        # Process structure
        structure = []
        metadata = {}

        try:
            # Walk directory
            for root, dirs, files in os.walk(path):
                depth = root[len(path):].count(os.sep)
                if depth > self.config['max_depth']:
                    continue

                # Add directory entry
                indent = ' ' * depth * self.config['indent']
                structure.append(self._format_directory(
                    os.path.basename(root),
                    template_data,
                    indent
                ))

                # Add files
                for file in files:
                    structure.append(self._format_file(
                        file,
                        template_data,
                        indent + ' ' * self.config['indent']
                    ))

            # Apply effects
            processed = self.effect_processor.apply_effects(
                structure,
                template_data.get('effects', [])
            )

            return {
                'structure': processed,
                'metadata': metadata,
                'template': template_data
            }

        except Exception as e:
            raise ProcessingError(f"Error processing directory: {str(e)}")

    def _format_directory(self, name: str, template: Dict, indent: str) -> str:
        """Format directory entry with template"""
        decorator = template.get('decorators', {}).get('folder',
                                                       self.config['decorators']['folder'])
        return f"{indent}{self.config['line_chars']['branch']}" \
               f"{self.config['line_chars']['horizontal']}" \
               f"{decorator} {name}/"

    def _format_file(self, name: str, template: Dict, indent: str) -> str:
        """Format file entry with template"""
        decorator = template.get('decorators', {}).get('file',
                                                       self.config['decorators']['file'])
        return f"{indent}{self.config['line_chars']['corner']}" \
               f"{self.config['line_chars']['horizontal']}" \
               f"{decorator} {name}"

    def render(self, structure: Dict, output: Optional[str] = None) -> None:
        """
        Render processed structure

        Args:
            structure: Processed structure dictionary
            output: Optional output file path
        """
        rendered = '\n'.join(structure['structure'])

        if output:
            with open(output, 'w') as f:
                f.write(rendered)
        else:
            print(rendered)


class ProcessingError(Exception):
    """Custom exception for processing errors"""
    pass

