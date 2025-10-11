"""
Grayscale Image Converter

This script converts a color image to grayscale using OpenCV.

Usage:
    python grayscale_converter.py <input_image_path> <output_image_path>

Example:
    python grayscale_converter.py ../data/sample.jpg ../data/sample_gray.jpg

Arguments:
    input_image_path: Path to the input color image
    output_image_path: Path where the grayscale image will be saved
"""

import cv2
import sys
import os


def convert_to_grayscale(input_path, output_path):
    """
    Convert an image to grayscale and save it.
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path where the grayscale image will be saved
    
    Returns:
        bool: True if successful, False otherwise
    """
    # Load the input image
    image = cv2.imread(input_path)
    
    # Check if image was loaded successfully
    if image is None:
        print(f"Error: Could not load image from '{input_path}'")
        print("Please check if the file exists and is a valid image format.")
        return False
    
    print(f"Loaded image: {input_path}")
    print(f"Image dimensions: {image.shape[1]}x{image.shape[0]} pixels")
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    
    # Save the grayscale image
    success = cv2.imwrite(output_path, gray_image)
    
    if success:
        print(f"Grayscale image saved successfully to: {output_path}")
        return True
    else:
        print(f"Error: Could not save image to '{output_path}'")
        return False


def main():
    """Main function to handle command-line arguments and execute conversion."""
    # Check if correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Error: Invalid number of arguments")
        print("\nUsage:")
        print("    python grayscale_converter.py <input_image_path> <output_image_path>")
        print("\nExample:")
        print("    python grayscale_converter.py ../data/sample.jpg ../data/sample_gray.jpg")
        sys.exit(1)
    
    # Get command-line arguments
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist")
        sys.exit(1)
    
    # Convert the image to grayscale
    success = convert_to_grayscale(input_path, output_path)
    
    # Exit with appropriate status code
    if success:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
