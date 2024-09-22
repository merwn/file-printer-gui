import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from file_printer import print_file, get_printers

def main():
    # Get available printers
    printers = get_printers()
    print("Available printers:", printers)

    # Print a PDF file
    pdf_file = "path/to/your/file.pdf"
    if os.path.exists(pdf_file):
        result = print_file(pdf_file, printers[0])
        if result:
            print(f"Successfully sent {pdf_file} to printer {printers[0]}")
        else:
            print(f"Failed to print {pdf_file}")
    else:
        print(f"File not found: {pdf_file}")

    # Print an image file
    image_file = "path/to/your/image.jpg"
    if os.path.exists(image_file):
        result = print_file(image_file, printers[0])
        if result:
            print(f"Successfully sent {image_file} to printer {printers[0]}")
        else:
            print(f"Failed to print {image_file}")
    else:
        print(f"File not found: {image_file}")

if __name__ == "__main__":
    main()
