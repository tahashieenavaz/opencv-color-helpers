import cv2 as cv
import numpy as np
from sys import argv
from utils import copy

def main():
    location = argv[1]
    image = cv.imread(location)

    cv.namedWindow("Picker")
    cv.setMouseCallback("Picker", click, image)
    cv.imshow("Picker", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def click(event, x, y, flags, image):
    if event != cv.EVENT_LBUTTONDOWN:
        return False

    color = image[y][x]
    copy(f"hsv({color[0]}, {color[1]}, {color[2]})")

if __name__ == "__main__": main()
