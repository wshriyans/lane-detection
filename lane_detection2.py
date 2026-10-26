import cv2
import numpy as np

# STEP 1: Load the road image
image = cv2.imread('road3.jpg')
if image is None:
    raise FileNotFoundError("Could not load 'road2.jpg'. Check the file name and path.")

# STEP 2: HSV color filtering
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Yellow lane lines (OpenCV hue range is 0-179; yellow sits around 20-35)
lower_yellow = np.array([18, 94, 140])
upper_yellow = np.array([35, 255, 255])
mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

# White lane lines (low saturation, high brightness)
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 40, 255])
mask_white = cv2.inRange(hsv_image, lower_white, upper_white)

color_mask = cv2.bitwise_or(mask_yellow, mask_white)
filtered_image = cv2.bitwise_and(image, image, mask=color_mask)

# STEP 3: Convert to grayscale, then blur
gray = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray, (5, 5), 0)

# STEP 4: Canny edge detection
edges = cv2.Canny(blurred_image, 50, 150)

# STEP 5: Region of Interest (trapezoid, scales with image size)
height, width = edges.shape
polygons = np.array([[
    (int(width * 0.05), height),
    (int(width * 0.95), height),
    (int(width * 0.55), int(height * 0.6)),
    (int(width * 0.45), int(height * 0.6)),
]], dtype=np.int32)   # fillPoly requires int32

roi_mask = np.zeros_like(edges)
cv2.fillPoly(roi_mask, polygons, 255)
masked_edges = cv2.bitwise_and(edges, roi_mask)

# STEP 6: Hough transform to turn edge pixels into line segments
lines = cv2.HoughLinesP(
    masked_edges,
    rho=1,
    theta=np.pi / 180,
    threshold=30,
    minLineLength=40,
    maxLineGap=100,
)

line_image = np.zeros_like(image)
if lines is not None:
    for x1, y1, x2, y2 in lines.reshape(-1, 4):
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 5)

result = cv2.addWeighted(image, 0.8, line_image, 1, 1)

# Save outputs for your GitHub README
cv2.imwrite('extracted_edges.jpg', masked_edges)
cv2.imwrite('extracted_lanes.jpg', result)

cv2.imshow("Edges in ROI", masked_edges)
cv2.imshow("Final Lane Lines", result)
cv2.waitKey(0)
cv2.destroyAllWindows()