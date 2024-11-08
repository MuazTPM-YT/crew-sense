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

## Installation

To get started with this project, clone the repository and install the required dependencies.

### Step 1: Clone the repository

```bash
git clone https://github.com/MuazTPM-YT/crew-sense.git

To start the application, run:
python main.py
