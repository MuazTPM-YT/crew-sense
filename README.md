# Automated Braille Conversion Tool

This project is an **Automated Braille Conversion Tool** that allows users to convert text into braille, text-to-speech, and PDF-to-braille. The application has a modern UI built with **PySide6** (Qt6 for Python) and includes various features to assist in accessibility for visually impaired individuals.

### Features:
- **Text to Braille**: Converts typed text into braille.
- **Text to Speech**: Converts typed text into speech using **pyttsx3** for text-to-speech functionality.
- **PDF to Braille**: Allows users to convert PDF documents into braille.
- **Modern UI**: The user interface is built with Qt Designer and styled with CSS for a modern, user-friendly experience.

---

## File Structure

- `main.py`: The main entry point to run the application, handling the integration of different components.
- `texttobrail.py`: Contains the logic for converting text and PDFs to braille, utilizing the `fitz` library for PDF parsing and processing.
- `interface.py`: Handles UI animation and interaction, with support for button hover effects and transitions.
- `texttospeech.py`: Implements the text-to-speech conversion using the `pyttsx3` library and handles the UI elements related to text-to-speech.

---

Image Text Recognition with Tesseract and OpenCV
This project demonstrates how to use pytesseract and opencv-python for Optical Character Recognition (OCR), allowing text extraction from images.

Prerequisites
Python 3.x (Ensure Python is installed on your machine)
Installation
Step 1: Clone the Repository (If applicable)
If this is part of a repository, clone it:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Step 2: Install Tesseract OCR
Windows: Download the installer from Tesseract's GitHub.

macOS: Use Homebrew to install Tesseract:

bash
Copy code
brew install tesseract
Linux: Install via apt:

bash
Copy code
sudo apt update
sudo apt install tesseract-ocr
Step 3: Set Up the Python Environment
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows:

bash
Copy code
venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
Step 4: Install Python Dependencies
In this project, pytesseract and opencv-python are used. Add these to your requirements.txt file:

text
Copy code
pytesseract
opencv-python
To install all dependencies listed in requirements.txt, run:

bash
Copy code
pip install -r requirements.txt
