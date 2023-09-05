import cv2

# Pass parameter 0 in VideoCapture(0) to access webcam. 
# Create an infinite while loop to display each frame of the webcam's video continuously
cap = cv2.VideoCapture(0)

while True:
    
    # Reading ( cap. read() ) from a VideoCapture returns a tuple (return value, image) . 
    # With the first item you check wether the reading was successful, and 
    # if it was then you proceed to use the returned image
    ret, frame = cap.read()
    
    frame = cv2.resize(frame, None, fx=1, fy=1, interpolation = cv2.INTER_LINEAR)
    
    # flip image so that it's more mirror like
    frame = cv2.flip(frame, 1)
    
    
    # Using Canny Edge Detection
    canny = cv2.Canny(frame, 50, 120)
    cv2.imshow('Canny', canny)
    
    ######### Can use other edge detection algorithm in same way ########
    
#     laplacian = cv2.Laplacian(frame, cv2.CV_64F)
#     cv2.imshow('Laplacian', laplacian)
    
    # Extract Sobel Edges
#     sobel_x = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=11)
#     sobel_y = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=11)
    
#     cv2.imshow('sobel_x', sobel_x)
#     cv2.imshow('sobel_y', sobel_y)
    
#     sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
#     cv2.imshow('sobel_OR', sobel_OR)
    
    
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cv2.destroyAllWindows()