"""
Tests for the core functionality of the Jupyter TOC Generator.
"""

import pytest
from ..core import _extract_headers, _generate_numbered_toc, generate_toc
import nbformat
import tempfile
import os


def test_extract_headers():
    """Test header extraction from markdown content."""
    content = """
    # Main Title
    Some text here
    ## Subtitle
    More text
    ### Section
    Even more text
    """
    
    headers = _extract_headers(content)
    assert len(headers) == 3
    assert headers[0] == (1, "Main Title")
    assert headers[1] == (2, "Subtitle")
    assert headers[2] == (3, "Section")


def test_generate_numbered_toc():
    """Test generation of numbered table of contents with hyperlinks."""
    headers = [
        (1, "Introduction"),
        (2, "Background"),
        (2, "Purpose"),
        (1, "Methodology"),
        (2, "Data Collection"),
    ]
    
    toc = _generate_numbered_toc(headers)
    expected = """# Table of Contents

1. [Introduction](#introduction)
    1.1. [Background](#background)
    1.2. [Purpose](#purpose)
2. [Methodology](#methodology)
    2.1. [Data Collection](#data-collection)"""
    
    assert toc == expected


def test_generate_toc():
    """Test full table of contents generation from a notebook."""
    # Create a temporary notebook
    nb = nbformat.v4.new_notebook()
    
    # Add markdown cells with headers
    md_cell1 = nbformat.v4.new_markdown_cell("""
    # Main Title
    Some text here
    ## Subtitle
    More text
    """)
    
    md_cell2 = nbformat.v4.new_markdown_cell("""
    ### Section
    Even more text
    """)
    
    nb.cells = [md_cell1, md_cell2]
    
    # Save notebook to temporary file
    with tempfile.NamedTemporaryFile(suffix='.ipynb', delete=False) as f:
        nbformat.write(nb, f)
        notebook_path = f.name
    
    try:
        # Generate TOC
        toc = generate_toc(notebook_path)
        
        # Verify content
        assert "# Table of Contents" in toc
        assert "1. [Main Title](#main-title)" in toc
        assert "    1.1. [Subtitle](#subtitle)" in toc
        assert "        1.1.1. [Section](#section)" in toc
        
    finally:
        # Clean up
        os.unlink(notebook_path) 