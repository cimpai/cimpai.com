#!/usr/bin/env python3
"""
Preprocessor for Markdown files to fix list formatting.

Adds blank lines before lists that immediately follow text ending with ':'.
This ensures proper list rendering in MkDocs.
"""

import re
import sys
from pathlib import Path


def fix_list_formatting(content: str) -> str:
    """
    Fix markdown list formatting by adding blank lines before lists
    that immediately follow text ending with ':'.
    """
    # Pattern: text ending with ':' followed immediately by a list item
    # Match: line ending with ':' (possibly with bold/italic), followed by newline and list item
    pattern = r'([^\n]+:)\n([-*+]\s)'
    
    def add_blank_line(match):
        text_before = match.group(1)
        list_marker = match.group(2)
        return f'{text_before}\n\n{list_marker}'
    
    # Replace pattern with added blank line
    fixed = re.sub(pattern, add_blank_line, content)
    
    return fixed


def process_file(file_path: Path) -> bool:
    """Process a single markdown file. Returns True if file was modified."""
    try:
        original_content = file_path.read_text(encoding='utf-8')
        fixed_content = fix_list_formatting(original_content)
        
        if original_content != fixed_content:
            file_path.write_text(fixed_content, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return False


def is_submodule_file(file_path: Path, base_dir: Path) -> bool:
    """
    Check if a file is inside a git submodule directory.
    Submodules are read-only and should not be modified.
    
    Submodules are located at:
    - docs/docs (cimp repository)
    - docs/practices (cimp-practices repository)
    """
    try:
        # Get relative path from base directory
        rel_path = file_path.relative_to(base_dir)
        parts = rel_path.parts
        
        # Check if file is in a submodule directory
        # Submodules are at: docs/docs and docs/practices
        if len(parts) >= 2:
            # If path starts with docs/docs or docs/practices, it's in a submodule
            if parts[0] == 'docs' and parts[1] in ('docs', 'practices'):
                return True
        
        return False
    except ValueError:
        # File is not relative to base_dir, check absolute path
        path_str = str(file_path)
        # Check if path contains docs/docs/ or docs/practices/ as submodule roots
        if '/docs/docs/' in path_str:
            # Extract the part after docs/docs/ to see if it's actually in the submodule
            idx = path_str.find('/docs/docs/')
            if idx != -1:
                return True
        if '/docs/practices/' in path_str:
            idx = path_str.find('/docs/practices/')
            if idx != -1:
                return True
        return False


def process_directory(directory: Path, exclude_dirs=None) -> int:
    """
    Process all markdown files in a directory recursively.
    Returns the number of files modified.
    """
    if exclude_dirs is None:
        exclude_dirs = {'.git', 'site', '__pycache__', '.venv', 'venv'}
    
    # Get the base directory (project root)
    base_dir = Path(__file__).parent.parent
    
    modified_count = 0
    
    for md_file in directory.rglob('*.md'):
        # Skip files in excluded directories
        if any(excluded in md_file.parts for excluded in exclude_dirs):
            continue
        
        # Skip submodule directories (read-only)
        if is_submodule_file(md_file, base_dir):
            continue
        
        if process_file(md_file):
            modified_count += 1
            print(f"Fixed: {md_file}")
    
    return modified_count


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
    else:
        # Default to docs directory
        target = Path(__file__).parent.parent / 'docs'
    
    if not target.exists():
        print(f"Error: {target} does not exist", file=sys.stderr)
        sys.exit(1)
    
    if target.is_file():
        # Process single file
        if process_file(target):
            print(f"Fixed: {target}")
        else:
            print(f"No changes needed: {target}")
    else:
        # Process directory
        modified = process_directory(target)
        if modified > 0:
            print(f"\nProcessed {modified} file(s)")
        else:
            print("No files needed fixing")


if __name__ == '__main__':
    main()

