import cv2
import numpy as np

# Read the image using cv2.imread
a = cv2.imread("C:\\CV pic\\kitty.png")

# Convert the image to grayscale
a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# Define Laplacian kernels
laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)
high_boost_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=np.float32)

# Perform convolution with Laplacian kernel
a1 = cv2.filter2D(a_gray, -1, laplacian_kernel)

# Perform convolution with High-boost kernel
a3 = cv2.filter2D(a_gray, -1, high_boost_kernel)

# Convert the result to uint8 (required for displaying images with OpenCV)
a2 = np.uint8(a1)
a4 = np.uint8(a3)

# Display the Laplacian result
cv2.imshow("Laplacian Result", a2)

# Display the High-boost result
cv2.imshow("High-boost Result", a4)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
