import cv2

# Create a black image
img = np.zeros((500, 500, 3), dtype="uint8")

# Draw a rectangle
cv2.rectangle(img, (100, 100), (400, 400), (0, 255, 0), 3)

# Show image
cv2.imshow("Test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
