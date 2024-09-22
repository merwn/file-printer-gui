from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="file-printer-gui",
    version="0.1.0",
    author="Tekzom",
    author_email="Tekzom@example.com",
    description="A versatile GUI and CLI tool for printing various file types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tekzom/file-printer-gui",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pillow>=8.3.2",
        "python-docx2pdf>=0.1.7",
        "pywin32>=301",
    ],
    entry_points={
        "console_scripts": [
            "file-printer=file_printer:main",
        ],
    },
)
