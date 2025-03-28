# Jupyter Notebook Table of Contents Generator

A Python library that automatically generates a table of contents for Jupyter notebooks by scanning markdown cells for headers.

## Features

- Scans Jupyter notebooks for markdown cells
- Identifies headers (H1, H2, H3) using "#", "##", and "###" syntax
- Generates a formatted table of contents with proper indentation
- Supports numbered sections
- Easy to integrate into existing notebooks
- Automatic notebook detection
- Hyperlinks to sections

## Installation

```bash
pip install jupyter-notebook-toc
```

## Usage

```python
import jupyter_notebook_toc.core as toc_gen

# Generate TOC from the current notebook
toc = toc_gen.generate_toc()
print(toc)

# Or specify a notebook file
toc = toc_gen.generate_toc("path/to/your/notebook.ipynb")
print(toc)

# Or save it to a file
with open("table_of_contents.md", "w") as f:
    f.write(toc)
```

## Command Line Usage

```bash
# Generate TOC from current notebook
jupyter-toc

# Generate TOC from specific notebook
jupyter-toc path/to/your/notebook.ipynb

# Save TOC to file
jupyter-toc -o table_of_contents.md
```

## Example Output

```markdown
# Table of Contents

1. [Introduction](#introduction)
    1.1. [Background](#background)
    1.2. [Purpose](#purpose)
2. [Methodology](#methodology)
    2.1. [Data Collection](#data-collection)
    2.2. [Analysis](#analysis)
3. [Results](#results)
    3.1. [Findings](#findings)
    3.2. [Discussion](#discussion)
```

## Development

To set up the development environment:

1. Clone the repository
2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
3. Run tests:
   ```bash
   pytest
   ```

## License

MIT License - see LICENSE file for details 