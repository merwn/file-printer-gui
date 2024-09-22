# File Printer GUI

A versatile and user-friendly Python application for printing various file types with advanced features and both GUI and command-line interfaces.

## Features

- Graphical User Interface (GUI) for easy file selection and printing
- Command-line interface for batch processing and automation
- Support for multiple file types: PDF, GIF, JPG, PNG, and DOCX
- Batch printing capabilities
- Print queue management
- Custom printer selection
- Adjustable print settings (copies, page range)
- Logging for better troubleshooting
- Configuration file for default settings
- Error handling and recovery

## Requirements

- Python 3.6+
- Windows OS (due to win32print dependency)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Tekzom/file-printer-gui.git
   cd file-printer-gui
   ```

2. Install the required dependencies:
   ```
   pip install pillow python-docx2pdf pywin32
   ```

3. Create a `config.ini` file in the project directory with your default settings:
   ```ini
   [DEFAULT]
   file_path = C:\path\to\your\default\file.pdf
   ```

## Usage

### GUI Mode

To launch the graphical interface, simply run the script without any arguments:

```
python file_printer.py
```

The GUI allows you to:
- Select files for printing
- Choose a printer
- Set the number of copies
- Specify a page range
- View the print queue

### Command-line Mode

For batch processing or automation, use the command-line interface:

```
python file_printer.py [FILES] [OPTIONS]
```

Options:
- `--printer`: Specify the printer to use
- `--copies`: Set the number of copies (default: 1)
- `--page-range`: Specify the page range to print

Example:
```
python file_printer.py file1.pdf file2.docx --printer "HP Printer" --copies 2 --page-range 1-5
```

## Contributing

Contributions to the File Printer GUI project are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the creators and maintainers of the libraries used in this project.
- Inspired by the need for a versatile and user-friendly printing solution.
