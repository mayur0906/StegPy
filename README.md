# Image Steganography Tool in Python

This program was written to complete an assignment in the Information Security - 2 (CSE 5381) course at the University of Texas at Arlington.
This program is used to demonstrate Steganography, which is the practice of concealing a file, message, image, or video within another file, message, image, or video. [Click here to know more](https://en.wikipedia.org/wiki/Steganography).

This program can conceal text within an image.

### Running the Program:

1. Ensure source image is in same directory as python files. Source image can be GIF or PNG only.
2. Ensure PIL library is installed for python.
3. Run [encode.py](https://github.com/mayur0906/StegPy/blob/master/encode.py) to create image with hidden data.
4. Run [decode.py](https://github.com/mayur0906/StegPy/blob/master/decode.py) to extract hidden data.

### Using [encode.py](https://github.com/mayur0906/StegPy/blob/master/encode.py):

1. Open source file in your favorite text editor.
2. Look for comment "Enter the image to be used as a carrier here."
3. Right below that, enter the file name of carrier.
4. Look for comment "Enter the message to be hidden here."
5. Right below that, enter the file name of result.
6. When running the python file, enter the secret message.
7. Look at current working directory after program execution. You will get your modified image with hidden text.

### Using [decode.py](https://github.com/mayur0906/StegPy/blob/master/decode.py):

1. Open source file in your favorite text editor.
2. Look for comment "Enter file name of image with hidden text here".
3. Right below that, enter the file name of image with hidden text.
4. When running the python file, secret message in image will be displayed.
