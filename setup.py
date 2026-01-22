"""
Setup file for cimpai.com MkDocs plugins.
This allows local plugins to be discovered by MkDocs.
"""

from setuptools import setup

setup(
    name="cimpai-mkdocs-plugins",
    version="0.1.0",
    py_modules=["mkdocs_plugin"],
    entry_points={
        "mkdocs.plugins": [
            "markdown_preprocessor = mkdocs_plugin:MarkdownPreprocessorPlugin",
        ]
    },
)

