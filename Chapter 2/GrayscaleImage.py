# A grayscale digital image is a two-dimensional raster image in which the picture elements, or pixels, store a single value representing a shade of gray that
# varies from black to white. In a discrete grayscale image, the shades of gray are represented by integer values in the range [0 . . . 255], where 0 is black and 255
# is white. We can define the Grayscale Image ADT for storing and manipulating discrete grayscale digital images. Given the description of the operations,
# provide a complete implementation of the ADT using a 2-D array.

# GrayscaleImage( nrows, ncols ): Creates a new instance that consists of nrows and ncols of pixels each set to an initial value of 0.

# width(): Returns the width of the image.

# height(): Returns the height of the image.

# clear( value ): Clears the entire image by setting each pixel to the given intensity value. The intensity value will be clamped to 0 or 255 if it is less
# than 0 or greater than 255, respectively.

# getitem ( row, col ): Returns the intensity level of the given pixel. The pixel coordinates must be within the valid range.

# setitem ( row, col, value ): Sets the intensity level of the given pixel to the given value. The pixel coordinates must be within the valid range.
#     The intensity value is clamped to 0 or 255 if it is outside the valid range.

class GrayscaleImage:
    def __init__(self, nrows, ncols):
        """
        Creates a new instance that consists of nrows and ncols of pixels each set to an initial value of 0.

        :param nrows: number of rows
        :param ncols: number of columns
        """
        self.nrows = nrows
        self.ncols = ncols
        self.image = [[0 for i in range(ncols)] for j in range(nrows)]

    def width(self):
        """
        Returns the width of the image.
        """
        return self.ncols
    
    def height(self):
        """
        Returns the height of the image.
        """
        return self.nrows
    
    def clear(self, value):
        """
        Clears the entire image by setting each pixel to the given intensity value. The intensity value will be clamped to 0 or 255 if it is less than 0 or greater

        :param value: intensity value
        """
        if value < 0:
            value = 0
        elif value > 255:
            value = 255

        for i in range(self.nrows):
            for j in range(self.ncols):
                self.image[i][j] = value
    
    def getitem(self, row, col):
        """
        Returns the intensity level of the given pixel. The pixel coordinates must be within the valid range.
        """
        return self.image[row][col]
    
    def setitem(self, row, col, value):
        """
        Sets the intensity level of the given pixel to the given value. The pixel coordinates must be within the valid range.
        """
        self.image[row][col] = value

    def __str__(self):
        # Convert each row to a string and join them with newline characters
        return '\n'.join([' '.join(map(str, row)) for row in self.image])
    
    def __repr__(self):
        # Similar to __str__, but ensuring it's unambiguous representation
        return f"GrayscaleImage(\n{self.__str__()}\n)"
    
    def __eq__(self, other):
        return self.image == other.image
    
    def __ne__(self, other):
        return self.image != other.image
    
# Test Code
if __name__ == "__main__":
    print("Creating a new GrayscaleImage instance with 3 rows and 4 columns:")
    img = GrayscaleImage(3, 4)
    print(img)  # Display the initial state of the image
    img.clear(100)
    print("\nClearing the image with intensity value 100:")
    img.clear(100)
    print(img)  # Display the image after clearing

    print("\nSetting individual pixels:")
    img.setitem(1, 2, 50)  # Set pixel at (1, 2) to intensity 50
    print(img)  # Display the image after setting individual pixels

    print(f"\nWidth of the image: {img.width()}")  # Display the width of the image
    print(f"Height of the image: {img.height()}")  # Display the height of the image

    print("\nGetting pixel intensity:")
    print(f"Intensity at (1, 2): {img.getitem(1, 2)}")  # Display the intensity at (1, 2)

    img.setitem(1, 2, 50)
    
    print("\nComparing images:")
    another_img = GrayscaleImage(3, 4)
    another_img.clear(100)  # Make another_img identical to img
    print(f"Are img and another_img equal? {'Yes' if img == another_img else 'No'}")  # Should print 'Yes'
    another_img.setitem(1, 2, 50)  # Change one pixel in another_img
    print(f"Are img and another_img equal? {'Yes' if img == another_img else 'No'}")  # Should print 'No'
