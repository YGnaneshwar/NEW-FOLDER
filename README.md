# File Organizer

A Python utility to automatically organize files in a directory by their file type extensions.

## Features

- GUI-based file organization
- Automatic categorization by file extension
- Support for multiple file types (txt, jpg, pdf, and more)
- Default "other" category for unknown file types
- Cross-platform compatibility

## Project Structure

```
file-organizer/
├── main.py                  # Application entry point
├── requirements.txt         # Project dependencies
├── README.md               # Project documentation
├── file_organizer/         # Main package
│   ├── __init__.py
│   ├── organizer.py        # Core organizing logic
│   └── gui.py              # GUI interface
├── tests/                  # Test suite
│   ├── __init__.py
│   └── test_organizer.py
└── .github/
    └── workflows/
        └── ci.yml          # GitHub Actions CI pipeline
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd file-organizer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

This will launch the GUI where you can:
1. Browse and select a directory
2. Click "Organize Files" to automatically sort files by type

## Testing

Run the test suite:
```bash
pytest tests/ -v
```

Run tests with coverage:
```bash
pytest tests/ --cov=file_organizer
```

## Supported File Types

- **Text Files**: `.txt`
- **Images**: `.jpg`, `.jpeg`, `.png`
- **Documents**: `.pdf`
- **Other**: Any unrecognized extension

## File Mapping

Files are organized into the following subdirectories:
- `text_files/` - Text documents
- `image_files/` - Image files
- `pdf_files/` - PDF documents
- `other_files/` - Files with unknown extensions

## CI/CD

This project uses GitHub Actions for continuous integration. The CI pipeline:
- Tests on Python 3.9, 3.10, and 3.11
- Runs pytest with coverage reporting
- Uploads coverage to Codecov

## License

MIT

## Contributing

Feel free to submit issues and enhancement requests!
