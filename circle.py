import cv2 as cv
import numpy as np

h = 0
s = 0
v = 0
windowName = "HSV Color Picker"

def main():
    cv.namedWindow(windowName)
    cv.createTrackbar("First", windowName, 0, 360, first_trackbar)
    cv.createTrackbar("Second", windowName, 0, 255, second_trackbar)
    cv.createTrackbar("Third", windowName, 0, 255, third_trackbar)
    render()
    cv.waitKey()
    cv.destroyAllWindows()

def render():
    colors = np.zeros((500, 500, 3), np.uint8)
    cv.cvtColor(colors, cv.COLOR_BGR2HSV)
    radius = 100
    colors = cv.circle(colors, (250, 250), radius, (h, s, v), -1)
    print(h,s,v)
    cv.imshow(windowName, colors)


def first_trackbar(val):
    global h
    h = val
    render()

def second_trackbar(val):
    global s
    s = val
    render()

def third_trackbar(val):
    global v
    v = val
    render()

if __name__ == "__main__": main()
