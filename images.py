import numpy as np
import cv2
#import matplotlib.pyplot as plt

imgobj = cv2.imread('test.jpg')
imgobj = cv2.cvtColor(imgobj, cv2.COLOR_BGR2GRAY)

#dim = (320,240)
#resized = cv2.resize(imgobj, dim, interpolation = cv2.INTER_AREA)

#cv2.rectangle(resized, (50,50),(150,150),(0,0,255),2)
cv2.namedWindow("image")


cv2.imshow("image",imgobj)
cv2.waitKey(0)
cv2.destroyAllWindows()
