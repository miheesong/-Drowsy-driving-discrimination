import cv2
import numpy as np
def His_(frame) :
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)
    return equ
