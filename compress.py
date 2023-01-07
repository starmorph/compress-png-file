import os
from PIL import Image

def compress_image(image_path, output_path, output_size, quality=85):
    """
    Compress a PNG image to an optimal size for websites.

    Parameters:
    - image_path: the path to the input image
    - output_path: the path to the output image
    - output_size: the desired output size of the image, in pixels
    - quality: the image quality, as a percentage (default is 85)
    """
    # Open the image
    with Image.open(image_path) as img:
        # Resize the image
        img = img.resize((output_size, output_size), resample=Image.LANCZOS)
        # Compress the image
        img.save(output_path, quality=quality, optimize=True)

# Example usage
compress_image('input.png', 'output.png', 128)
