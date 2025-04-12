from shapedec import ShapeDetector
import imutils
import cv2
import os

image = cv2.imread('img.jpg')
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
#print ("\123 = {}",thresh)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# find contours in the thresholded image and initialize the
# shape detector
cv2.imshow('image1', thresh)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

#список фигур
figure_triangle=0
figure_square=0
figure_rectangle=0
figure_pentagon=0
figure_hexagon=0
figure_circle=0

for c in cnts:
    # compute the center of the contour, then detect the    name of the
    # shape using only the contour
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    shape = sd.detect(c)
    #print("\nfigure - {}".format(shape))    # вывод фигуры

    #считаю фигуры
    if shape=="triangle":
        figure_triangle+=1
    if shape=="square":
        figure_square+=1
    if shape=="rectangle":
        figure_rectangle+=1
    if shape=="pentagon":
        figure_pentagon+=1
    if shape=="hexagon":
        figure_hexagon+=1
    if shape=="circle":
        figure_circle+=1

    # multiply the contour (x, y)-coordinates
    # then draw the contours and the name of the shape on the
    image
    cv2.drawContours(image, [c], -1, (255, 0, 0), 2)
    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(image, shape, (cX, cY),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5, (0, 0, 0), 2)
    # show the output image
cv2.imshow("Image", image)
#print("\n Objects in the image: \n triangle = {} \n square = {} \n rectangle = {} \n pentagon = {} \n hexagon = {} \n circle = {} ".format(figure_triangle,
                                                                                                                                           figure_square, figure_rectangle,
                                                                                                                                           figure_pentagon, figure_hexagon, figure_circle))

cv2.waitKey(0)