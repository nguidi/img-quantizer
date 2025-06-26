import matplotlib.pyplot as plt
import numpy as np
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

print(f"Image Details:")
print(f"- Dimensions: {width}x{height}")
print(f"- Total Pixels: {total_pixels}")

# Extract and count colors
pixels = list(img_rgb.getdata())
color_counter = Counter(pixels)
most_common_colors = color_counter.most_common(4)

data = []
colors = []

print("\nTop 4 Colors:")
for idx, (rgb, count) in enumerate(most_common_colors, start=1):
    hex_code = rgb_to_hex(rgb)
    percentage = (count / total_pixels) * 100
    print(f"{idx}. RGB: {rgb}, HEX: {hex_code}, Pixels: {count}, Percentage: {percentage:.2f}%")
    data.append([hex_code, rgb[0], rgb[1], rgb[2], '', total_pixels, count, round(percentage, 2)])
    colors.append(hex_code)

data.append(['', '', '', '', '', '', '', ''])
colors.append('#ffffff')

# Calculate the mean color
mean_rgb = tuple(
    sum(c[i] * count for c, count in color_counter.items()) // total_pixels
    for i in range(3)
)
mean_hex = rgb_to_hex(mean_rgb)


print("\nMean Color:")
print(f"- RGB: {mean_rgb}")
print(f"- HEX: {mean_hex}")

data.append([mean_hex, mean_rgb[0], mean_rgb[1], mean_rgb[2], '', '', '', ''])
colors.append(mean_hex)

headers = ['HEX', 'R', 'G', 'B', '', 'PXtot', 'PXparz', 'px%']

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 4), gridspec_kw={'width_ratios': [1, 1, 2]})
ax1.imshow(img)
ax1.axis('off')
ax2.imshow(img_quantized)
ax2.axis('off')



table = ax3.table(cellText=data, colLabels=headers, loc='center',
                  cellColours=[[color] * 8 for color in colors])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 1.5)

for k, cell in table._cells.items():
    cell.set_edgecolor('none')
    cell.get_text().set_horizontalalignment('left')
    cell.get_text().set_weight('bold')
    if k[0] == 0:  # Header row
        cell.get_text().set_fontsize(11)
    if cell.get_text().get_text() == '':
        cell.set_facecolor('white')
        cell._width = cell._height  # Make empty cells square
    else:
        hex_color = cell.get_facecolor()
        # Convert hex color to RGB values
        r = int(hex_color[0] * 255)
        g = int(hex_color[1] * 255)
        b = int(hex_color[2] * 255)
        # Calculate brightness using perceived luminance formula
        brightness = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        cell.get_text().set_color('white' if brightness < 0.7 else 'black')

ax3.axis('off')

# Get table height in inches
table_height = ax3.get_position().height * fig.get_figheight()

# Adjust images to match table height while maintaining aspect ratio
for ax, img in [(ax1, img), (ax2, img_quantized)]:
    ax_pos = ax.get_position()
    aspect = img.size[0] / img.size[1]
    new_width = table_height * aspect
    ax.set_position([ax_pos.x0, ax_pos.y0, new_width / fig.get_figwidth(), table_height / fig.get_figheight()])

plt.show()
plt.savefig('outout/stats.png')
