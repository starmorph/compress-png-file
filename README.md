# Compress PNG File

This Python script uses the Pillow library to compress a PNG image for websites, with customizable output size and quality.

## Requirements

- Python 3
- Pillow library (`pip install pillow`)

## Usage

```
compress_image(image_path, output_path, output_size, quality=85)
```

## Parameters
image_path: the path to the input PNG image
output_path: the path to the output image
output_size: the desired output size of the image, in pixels
quality: the image quality, as a percentage (default is 85)

Example
```
compress_image('input.png', 'output.png', 128)
This example will compress and resize the input image to 128x128 pixels, and save it to the output file.
```

## How it Works
The script opens the input image using the Image.open method from the Pillow library.
It resizes the image using the resize method, with the LANCZOS resampling method for high quality resizing.
It compresses the image using the save method, with the quality and optimize parameters to ensure optimal image compression for the web.
It saves the output image to the specified file path.

## Notes
This script only works for PNG images. To compress other image file types, you can modify the script to include the appropriate file types in the endswith method.
The quality parameter determines the image quality, as a percentage. A lower value will result in a smaller file size but lower quality image, while a higher value will result in a larger file size but higher quality image.
The optimize parameter ensures that the image file is optimized for the web. It is recommended to leave this parameter as True for best results.

## Additional Resources
Pillow documentation

