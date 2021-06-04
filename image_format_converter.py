import cv2 as cv
import sys
try:
    img = cv.imread(cv.samples.findFile("800px-Ada_Lovelace_portrait.jpg"))
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("starry_night.png", img)
except:
    print("error!")