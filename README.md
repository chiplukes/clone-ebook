# clone-ebook

[![Changelog](https://img.shields.io/github/v/release/chiplukes/clone-ebook?include_prereleases&label=changelog)](https://github.com/chiplukes/clone-ebook/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/chiplukes/python-example-package/blob/main/LICENSE)


This application uses OCR to create a backup of an ebook that you own from the screen on your PC.


Currently a work in progress!

## Prerequisites

### Tesseract OCR

You will need to install Tesseract OCR.  See instructions here:

https://tesseract-ocr.github.io/tessdoc/Installation.html

### Pandoc

You will need to install Pandoc.

https://pandoc.org/installing.html

## Installation

### Using uv (recommended)

First, install uv if you haven't already:
```bash
# On Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then clone and set up the project:
```bash
git clone https://github.com/chiplukes/clone-ebook
cd clone-ebook
uv sync
```

### Using pip (alternative)

```bash
git clone https://github.com/chiplukes/clone-ebook
cd clone-ebook
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
pip install -e .
```

## Usage

Running main application:
```bash
# With uv
uv run python main.py

# Or if venv is activated
python main.py
```

### Convert existing PDF to markdown

To convert an existing PDF file directly to markdown (skips screen capture):
```bash
uv run python main.py --input_pdf "path/to/your/book.pdf"
```

## Development

Install development dependencies:
```bash
uv sync --extra dev
```

For using pre-commit hooks:
```bash
uv run pre-commit install
```
