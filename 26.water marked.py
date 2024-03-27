import cv2

# Read the original image
original_image = cv2.imread('C:\\CV pic\\kitty.png')

# Read the watermark image (ensure it has an alpha channel for transparency)
watermark_image = cv2.imread('C:\\CV pic\\wall.png', cv2.IMREAD_UNCHANGED)

# Resize the watermark image to fit into the original image
watermark_resized = cv2.resize(watermark_image, (original_image.shape[1], original_image.shape[0]))

# Extract the alpha channel from the resized watermark image
alpha = watermark_resized[:, :, 3] / 255.0

# Blend the watermark onto the original image
for c in range(3):
    original_image[:, :, c] = original_image[:, :, c] * (1.0 - alpha) + watermark_resized[:, :, c] * alpha

# Save or display the resulting image
cv2.imwrite('watermarked_image.jpg', original_image)
cv2.imshow('Watermarked Image', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

