import cv2

# Load the image
image = cv2.imread("C:\\CV pic\\kitty.png")

# Define the region of interest (ROI) where you want to move the image
x_offset = 100  # X coordinate of the top-left corner of the ROI
y_offset = 50   # Y coordinate of the top-left corner of the ROI

# Define the width and height of the region of interest (ROI)
roi_width = 200  # Width of the ROI
roi_height = 150 # Height of the ROI

# Extract the ROI
roi = image[y_offset:y_offset+roi_height, x_offset:x_offset+roi_width]

# Define the new position where you want to move the ROI
new_x = 300     # New X coordinate of the top-left corner of the moved ROI
new_y = 200     # New Y coordinate of the top-left corner of the moved ROI

# Update the original image with the moved ROI
image[new_y:new_y+roi_height, new_x:new_x+roi_width] = roi

# Display the updated image
cv2.imshow("Moved Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
