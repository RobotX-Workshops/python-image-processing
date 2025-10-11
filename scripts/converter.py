#!/usr/bin/env python3
"""
Image to Grayscale Converter

This script converts a color image to grayscale and saves the result.
Usage: python converter.py <input_image_path> [output_image_path]
"""

import sys
import os
import cv2


def convert_to_grayscale(input_path, output_path=None):
    """
    Convert an image to grayscale and save it.
    
    Args:
        input_path (str): Path to the input image
        output_path (str, optional): Path for the output image. 
                                     If None, generates a default name.
    
    Returns:
        bool: True if successful, False otherwise
    """
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return False
    
    # Load the image
    image = cv2.imread(input_path)
    
    if image is None:
        print(f"Error: Could not load image from '{input_path}'.")
        print("Supported formats: JPG, PNG, BMP, TIFF, etc.")
        return False
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Generate output path if not provided
    if output_path is None:
        base_name, ext = os.path.splitext(input_path)
        output_path = f"{base_name}_grayscale{ext}"
    
    # Save the grayscale image
    success = cv2.imwrite(output_path, gray_image)
    
    if success:
        print(f"Successfully converted '{input_path}' to grayscale.")
        print(f"Saved as: '{output_path}'")
        return True
    else:
        print(f"Error: Could not save image to '{output_path}'.")
        return False


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python converter.py <input_image_path> [output_image_path]")
        print("\nExample:")
        print("  python converter.py image.jpg")
        print("  python converter.py image.jpg output.jpg")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Convert the image
    success = convert_to_grayscale(input_path, output_path)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
