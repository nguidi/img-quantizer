# Image Color Quantization and Analysis

This Python script processes an input image to reduce its colors to four and conducts an analysis of the resulting image. The analysis includes identifying the most common colors, their percentages, and the mean color of the image.

## Features

- Converts the input image to **four major colors** using quantization.
- Outputs the processed image with reduced colors.
- Extracts image metadata such as dimensions, total pixels, and format.
- Displays the **top 4 colors** in RGB and HEX format with their occurrence percentages.
- Calculates and shows the **mean color** of the image in both RGB and HEX formats.

---

## Requirements

To run this script, ensure the following dependencies are installed:

- Python 3.7 or higher
- Required libraries:
  - `Pillow` (`pip install pillow`)

---

## Getting Started

Follow the steps below to run the script:

### 1. Install Dependencies

If you don't already have `Pillow` installed, use the following command:

    bash pip install pillow

### 2. Run the Script

Execute the script using the command line by providing the input image and specifying the output image file:

    bash python script_name.py <input_image> <output_image>


Replace:
- `<input_image>` with the path to the image file you want to process.
- `<output_image>` with the path where the resulting image should be saved.

### Example
    
    bash python script_name.py input.jpg output.jpg


---

## Outputs

### 1. Processed Image
The output image will have its colors reduced to **four major colors** and saved to the specified location.

### 2. Analysis in the Console
The script will print the following details to the terminal:
- **Image Details**:
  - Dimensions (Width x Height)
  - Total Pixels
  - Format of the image
- **Top 4 Colors**:
  - The most common RGB and HEX colors, along with their count and percentage in the image.
- **Mean Color**:
  - The overall mean color of the image in RGB and HEX.

---

## Example Output

If the input image is `input.jpg`, the console output may look like this:

```
Image Details:
- Dimensions: 800x600
  - Total Pixels: 480000
  - Format: JPEG

Top 4 Colors:
1. RGB: (202, 44, 33), HEX: #ca2c21, Pixels: 120000, Percentage: 25.00%
   2. RGB: (33, 44, 202), HEX: #212cca, Pixels: 120000, Percentage: 25.00%
   3. RGB: (44, 202, 33), HEX: #2cca21, Pixels: 120000, Percentage: 25.00%
   4. RGB: (33, 33, 33), HEX: #212121, Pixels: 120000, Percentage: 25.00%

Mean Color:
- RGB: (78, 81, 125)
  - HEX: #4e517d
```

---

## How it Works

1. **Image Loading**:
   The input image is loaded using the `Pillow` library.

2. **Quantization**:
   The image is reduced to four main colors using the `quantize()` function.

3. **Color Analysis**:
   The pixel data is extracted and analyzed using the `collections.Counter` module to identify the most common colors.

4. **Mean Color Calculation**:
   The script calculates the average color intensity for the entire image.

5. **Image Saving**:
   The processed image is saved to the user-specified path.

---

## Function Documentation

### rgb_to_hex(rgb)

Converts an RGB tuple (e.g., `(255, 0, 0)`) to its hexadecimal color code (e.g., `#ff0000`).

- **Parameters**: 
  - `rgb` (tuple): A tuple of integers representing the Red, Green, and Blue components.
- **Returns**: 
  - Hexadecimal string of the color.

---

## Limitations

- Quantization reduces the image to only four key colors, which may result in some loss of detail.
- Processing very large images may take substantial time.

---

## License

This script is open-source and available for free use. Modify as needed to suit your requirements!