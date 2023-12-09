import cv2

######## READING IMAGE ########
# Syntax: cv2.imread(path, flag)
# Parameters:
# path: A string representing the path of the image to be read.
# flag: It specifies the way in which image should be read. Itâs default value is cv2.IMREAD_COLOR
# Return Value: This method returns an image that is loaded from the specified file.
image = cv2.imread('image.jpg',0)

# resizing image and showing
image = cv2.resize(image, None, fx=0.3, fy=0.3, interpolation = cv2.INTER_LINEAR)
cv2.imshow('Original', image)

# getting dimensions
height, width = image.shape


######## SOBEL EDGE DETECTION ########
# Extract Sobel Edges X and Y
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
cv2.waitKey(0)

# Show Sobel-X (Horizontal Edges)
cv2.imshow('Sobel X', sobel_x)
cv2.waitKey(0)

# Show Sobel-Y (Vertical Edges)
cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey(0)

# Combining Sobel-X and Sobel-Y edges with OR and Show the image
sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('sobel_OR', sobel_OR)
cv2.waitKey(0)
####################################

######## LAPLACIAN EDGE DETECTION ########
laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)
####################################

######## CANNY EDGE DETECTION ########
canny = cv2.Canny(image, 60, 120)
cv2.imshow('Canny', canny)
cv2.waitKey(0)
####################################

## In Canny, we need to provide two values: threshold1 and threshold2. Any gradient value larger than threshold2
# is considered to be an edge. Any value below threshold1 is considered not to be an edge. 
# Values in between threshold1 and threshold2 are either classiï¬ed as edges or non-edges based on how their 
# intensities are âconnectedâ. In this case, any gradient values below 60 are considered non-edges
# whereas any values above 120 are considered edges.


# Canny Edge Detection uses gradient values as thresholds


# Destroy all output windows
cv2.destroyAllWindows()
