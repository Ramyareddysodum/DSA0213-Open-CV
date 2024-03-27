import cv2

path = r"C:\CV pic\kitty.png"
src = cv2.imread(path)

window_name = 'Image'

# Rotate the image by 90 degrees clockwise
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow(window_name, image)
cv2.waitKey(0)
