# Speech-to-Text Notes Application

## Project Overview

The Speech-to-Text Notes Application is a Python desktop application that converts spoken words into written text. Users can record their speech, view the recognized text, and save their notes as text files.

## Features

* Speech recognition through a microphone.
* Conversion of speech into text.
* Graphical user interface.
* Save recognized text as a file.
* Clear the text area.
* Error handling for common speech recognition problems.

## Technologies Used

* Python
* SpeechRecognition
* PyAudio
* Tkinter
* Git
* GitHub

## Installation

### 1. Clone the Repository

Clone this repository to your computer.

### 2. Create a Virtual Environment

```
python -m venv venv
```

Activate the environment on Windows PowerShell:

```
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```
python -m pip install -r requirements.txt
```

### 4. Run the Application

```
python app.py
```

## Requirements

* Python
* A working microphone
* An internet connection for online speech recognition

## How to Use

1. Run the application.
2. Click Start Recording.
3. Speak into the microphone.
4. Review the converted text.
5. Click Save Notes to save your text.
6. Click Clear Notes to clear the text area.

## Limitations

The current version uses an online speech recognition service. Recognition accuracy depends on audio quality, pronunciation, background noise, and internet connectivity.

## Future Enhancements

* Multiple language support.
* Offline speech recognition.
* Automatic timestamps.
* Search and organize saved notes.
* Export notes to PDF.

## Author

HariniPriya
