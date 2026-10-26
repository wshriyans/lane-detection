# Lane Line Extractor using OpenCV

## About the project

This project uses OpenCV to find lane markings in a static road image. It uses color filtering, edge detection and a region of interest to focus on the road. The detected line segments are drawn in red on the original image.

## Requirements

- Python 3
- OpenCV
- NumPy
- A road image named `road3.jpg`

## How to run it

1. Put `lane_detector.py` and your road image (`road3.jpg`) in the same folder.
2. Install the required libraries:

   ```bash
   pip install opencv-python numpy
   ```

3. Run the script:

   ```bash
   python lane_detector.py
   ```

4. The script saves two output images in the same folder:
   - `extracted_edges.jpg` — edge pixels inside the road region of interest.
   - `extracted_lanes.jpg` — the original image with detected lane segments drawn in red.

The script also opens two windows. Press a key while a window is active to close the display.

## Processing steps

1. **Load image:** Reads `road3.jpg`.
2. **HSV color filtering:** Keeps pixels that match the yellow and white color ranges.
3. **Gaussian blur:** Reduces small details and noise before edge detection.
4. **Canny edge detection:** Finds strong edges in the filtered image.
5. **ROI masking:** Keeps edges in a trapezoid-shaped area where the road is expected.
6. **Hough transform:** Finds line segments from the remaining edge pixels and draws them on the image.

## Results

Run the script first so that the two output image files are created. Then commit those files along with this README to show your results on GitHub.

### Edges inside the ROI

![Edges inside the ROI](extracted_edges.jpg)

### Detected lane lines

![Detected lane lines](extracted_lanes.jpg)

## Notes

- Use a road image named exactly `road3.jpg`, and keep it in the same folder as the script.
- The script's error message mentions `road2.jpg`, while the image it loads is `road3.jpg`. The code has been kept as supplied for this assignment.
- Results depend on the road image and lighting conditions.
