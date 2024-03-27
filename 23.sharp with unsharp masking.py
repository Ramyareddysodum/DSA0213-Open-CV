
import cv2
import numpy as np

# Load the image
image = cv2.imread("C:\\CV pic\\kitty.png")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(gray, (0, 0), 1.5)

# Calculate the unsharp mask
unsharp_mask = cv2.addWeighted(gray, 1.5, blurred, -0.5, 0)

# Display the original and sharpened images
cv2.imshow('Original', gray)
cv2.imshow('Sharpened', unsharp_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
