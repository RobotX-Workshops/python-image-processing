# python-image-processing
A reusable template for RobotX Workshops image processing projects using Python and OpenCV.

## Overview
This workshop provides a hands-on introduction to image processing using Python. You'll learn how to load, manipulate, and display images using popular libraries like OpenCV, NumPy, and Matplotlib.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/RobotX-Workshops/python-image-processing.git
cd python-image-processing
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

### Project Structure
```
python-image-processing/
├── data/           # Sample images and datasets
├── notebooks/      # Jupyter notebooks for interactive learning
├── scripts/        # Python scripts for image processing tasks
└── requirements.txt
```

## Getting Started

### Running Notebooks
Launch Jupyter Notebook to explore the interactive tutorials:
```bash
jupyter notebook
```

Navigate to the `notebooks/` folder and open `01_intro.ipynb` to get started with basic image processing operations.

### Using Scripts
The `scripts/` folder contains utility scripts for common image processing tasks.

Example - Convert an image to grayscale:
```bash
python scripts/converter.py path/to/your/image.jpg
```

## Workshop Contents

### Notebooks
- **01_intro.ipynb**: Introduction to loading, converting to grayscale, and displaying images

### Scripts
- **converter.py**: Command-line tool to convert images to grayscale

## Dependencies
- **numpy**: Numerical computing library for array operations
- **opencv-python**: Computer vision library for image processing
- **matplotlib**: Plotting library for displaying images

## License
MIT License - see LICENSE file for details
