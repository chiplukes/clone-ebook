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

Install this application using `pip`:
```bash
git clone git+https://github.com/chiplukes/clone-ebook
cd clone-ebook
python -m venv .venv
source venv/bin/activate

```

## Usage

Now install the dependencies and test dependencies:
```bash
python -m pip install -e .
```

Running main application
```bash
python main.py
```
``

## Development

For using pre-commit hooks:
```bash
pre-commit install
```
