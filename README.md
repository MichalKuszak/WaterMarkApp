# WaterMarkApp

**WaterMarkApp** is a lightweight desktop GUI application that allows users to quickly add customizable watermarks to images. The application provides an intuitive interface built with `Tkinter` and enhanced with `ttkbootstrap`.

## Features

- Drag & Drop support for images
- Custom watermark text input
- Font and size selection
- Dark and light themes
- Image preview before saving
- Automatic filename handling to avoid overwriting

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MichalKuszak/WaterMarkApp.git
   cd WaterMarkApp
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Requirements

- Python 3.8+
- `ttkbootstrap`
- `Pillow`
- `tkinterdnd2`

Install dependencies individually if needed:

```bash
pip install ttkbootstrap pillow tkinterdnd2
```

## Running the App

After installing the dependencies, run:

```bash
python main.py
```

## Project Structure

```
.
├── main.py               # Entry point
├── assets/               # Contains default images or assets
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## License

This project is open-source and available under the [MIT License](LICENSE).
