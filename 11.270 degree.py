import cv2 
path = "C:\\CV pic\\kitty.png" 
src = cv2.imread(path) 
window_name = 'Image' 
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE) 
cv2.imshow(window_name, image) 
cv2.waitKey(0) 
