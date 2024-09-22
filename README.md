# File Printer GUI

A simple, user-friendly Python GUI application for printing PDF and GIF files to the default printer.

## Features

- Minimalist and intuitive interface
- Supports printing PDF and GIF files
- Uses system default printer
- Pre-set file path for quick printing
- File browser for easy selection

## Requirements

- Python 3.x
- PyWin32
- Pillow (PIL)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/tekzom/file-printer-gui.git
   ```

2. Navigate to the project directory:
   ```
   cd file-printer-gui
   ```

3. Install the required packages:
   ```
   pip install pywin32 pillow
   ```

## Usage

1. Run the script:
   ```
   python file_printer.py
   ```

2. The GUI will open, showing the pre-set file path and default printer.

3. To print the pre-set file, click the "PRINT" button.

4. To print a different file:
   - Click "Browse" to select a PDF or GIF file
   - Click "PRINT" to send the selected file to the printer

## Customization

To change the default file path, modify the `DEFAULT_FILE_PATH` variable in the script.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/tekzom/file-printer-gui/issues) if you want to contribute.
