"""
MkDocs plugin to preprocess markdown files before rendering.

Automatically fixes list formatting by adding blank lines before lists.
This plugin is loaded directly by MkDocs.
"""

import re
from mkdocs.plugins import BasePlugin


class MarkdownPreprocessorPlugin(BasePlugin):
    """Plugin to preprocess markdown files for proper list formatting."""
    
    def on_page_markdown(self, markdown, page, config, files):
        """
        Process markdown content before rendering.
        This runs for each page automatically.
        """
        # Pattern: text ending with ':' followed immediately by a list item
        # Match: line ending with ':' (possibly with bold/italic), followed by newline and list item
        pattern = r'([^\n]+:)\n([-*+]\s)'
        
        def add_blank_line(match):
            text_before = match.group(1)
            list_marker = match.group(2)
            return f'{text_before}\n\n{list_marker}'
        
        # Fix list formatting
        fixed_markdown = re.sub(pattern, add_blank_line, markdown)
        
        return fixed_markdown

