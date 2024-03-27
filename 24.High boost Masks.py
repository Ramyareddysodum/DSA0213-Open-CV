import cv2
import numpy as np

# Read the image
img = cv2.imread("C:\\CV pic\\kitty.png")

# Apply Gaussian blur to the image to reduce noise
blurred_img = cv2.GaussianBlur(img, (3, 3), 0)

# Create a Laplacian kernel for edge detection
laplacian_kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=np.float32)

# Apply Laplacian filter to the image
laplacian = cv2.filter2D(blurred_img, -1, laplacian_kernel)

# Set the boost factor
k = 1.5  # You can adjust this parameter for different levels of sharpening

# Calculate the high-boost filtered image
sharpened_img = img + k * laplacian

# Clip values to ensure they are within [0, 255]
sharpened_img = np.clip(sharpened_img, 0, 255)

# Convert to uint8 (required for displaying images with OpenCV)
sharpened_img = np.uint8(sharpened_img)

# Display the original and sharpened images
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
