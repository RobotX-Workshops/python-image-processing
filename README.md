# Python Image Processing

A reusable template for RobotX Workshops image processing projects using Python and OpenCV.

## Requirements

- **Python**: Version 3.9 or higher
- **Operating System**: Windows, macOS, or Linux
- **Camera**: USB webcam or built-in camera (recommended for hands-on exercises)

## Getting Started

Choose one of the following setup methods:

### Option 1: Using Dev Container (Recommended) 🐳

**Best for**: Consistent environment across all machines, no local Python setup needed.

**Prerequisites**: 
- [VS Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

**Setup Steps**:
1. **Clone this repository**:
   ```bash
   git clone https://github.com/RobotX-Workshops/python-image-processing.git
   cd python-image-processing
   ```

2. **Open in VS Code**:
   ```bash
   code .
   ```

3. **Reopen in Container**:
   - VS Code will show a popup asking to "Reopen in Container"
   - Click **"Reopen in Container"**
   - OR use Command Palette (`Ctrl+Shift+P`) → "Dev Containers: Reopen in Container"

4. **Wait for setup**: The container will automatically:
   - Install Python 3.12
   - Install all dependencies from `requirements.txt`
   - Set up the development environment

5. **Start coding!** 🎉 Everything is ready to go!

---

### Option 2: Local Virtual Environment 🐍

**Best for**: Working on your own machine, have Python already installed.

**Prerequisites**: Python 3.9 or higher installed locally

**Setup Steps**:
1. **Check Python version**:
   ```bash
   python --version
   # Should show 3.9 or higher
   ```

2. **Clone this repository**:
   ```bash
   git clone https://github.com/RobotX-Workshops/python-image-processing.git
   cd python-image-processing
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Start Jupyter or VS Code**:
   ```bash
   # Option A: Start Jupyter Notebook
   jupyter notebook
   
   # Option B: Open in VS Code
   code .
   ```

---

## Verifying Your Setup

After completing either setup method, verify everything works:

1. **Test OpenCV installation**:
   ```python
   import cv2
   print(f"OpenCV version: {cv2.__version__}")
   ```

2. **Test camera access** (if you have a camera):
   ```python
   import cv2
   cap = cv2.VideoCapture(0)
   print(f"Camera available: {cap.isOpened()}")
   cap.release()
   ```

3. **Run the intro notebook**:
   - Open `notebooks/01_intro_to_opencv.ipynb`
   - Execute all cells to ensure everything works

## Project Structure

The template is organized into the following directories:

- **`data/`**: Store your input images and datasets here. This is where you should place sample images for processing and experimentation.

- **`notebooks/`**: Contains Jupyter notebooks for interactive learning and experimentation. Start with the introductory notebooks to learn the basics of image processing with OpenCV.

- **`scripts/`**: Contains standalone Python scripts for image processing tasks. These scripts can be run from the command line and are useful for batch processing or automation.
