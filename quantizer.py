from PIL import Image
from collections import Counter
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Convert an image to four colors.')
parser.add_argument('input', help='Input image file')
parser.add_argument('output', help='Output image file')
args = parser.parse_args()

# Open the input image
img = Image.open(args.input)

# Reduce the image to four colors
img_quantized = img.quantize(colors=4)

# Convert back to RGB mode
img_rgb = img_quantized.convert('RGB')

# Save the output image
img_rgb.save(args.output)

# Function to convert RGB to HEX
def rgb_to_hex(rgb):
    """
    Converts an RGB tuple to a hexadecimal color string.

    This function takes a tuple representing the Red, Green, and Blue (RGB) values
    and converts it to a string representing the color in hexadecimal format.
    The values in the RGB tuple must be integers between 0 and 255 inclusive.

    :param rgb: A tuple containing three integer values representing the red, green,
        and blue components of the color.
    :return: A string representing the hexadecimal color equivalent of the provided
        RGB tuple.
    """
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

# Image details
width, height = img_rgb.size
total_pixels = width * height
image_format = img_rgb.format or "N/A"  # Since img_rgb was converted, format might be N/A

print(f"Image Details:")
print(f"- Dimensions: {width}x{height}")
print(f"- Total Pixels: {total_pixels}")
print(f"- Format: {image_format}")

# Extract and count colors
pixels = list(img_rgb.getdata())
color_counter = Counter(pixels)
most_common_colors = color_counter.most_common(4)

print("\nTop 4 Colors:")
for idx, (rgb, count) in enumerate(most_common_colors, start=1):
    hex_code = rgb_to_hex(rgb)
    percentage = (count / total_pixels) * 100
    print(f"{idx}. RGB: {rgb}, HEX: {hex_code}, Pixels: {count}, Percentage: {percentage:.2f}%")

# Calculate the mean color
mean_rgb = tuple(
    sum(c[i] * count for c, count in color_counter.items()) // total_pixels
    for i in range(3)
)
mean_hex = rgb_to_hex(mean_rgb)

print("\nMean Color:")
print(f"- RGB: {mean_rgb}")
print(f"- HEX: {mean_hex}")

