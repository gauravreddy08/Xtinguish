import streamlit as st
import cv2
import numpy as np

def get_pixel_count(img):
    img = cv2.imread(img)
    rimg = cv2.resize(img, (1000, 600))
    blur = cv2.GaussianBlur(rimg, (15, 15), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    rgb = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

    lower = np.array([0, 100, 111], dtype='uint8')
    upper = np.array([70, 250, 255], dtype='uint8')

    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(rgb, rgb, mask=mask)
    count = cv2.countNonZero(mask)

    return count

def find_intensity(count, time):
    if (time == 'Night'):
        if count >= 150000:
            return "High Intensity"
        elif count <= 1000:
            return "Low Intensity"
        else:
            return "Medium Intensity"
    else:
        if count >= 80000:
            return "High Intensity"
        elif count <= 20000:
            return "Low Intensity"
        else:
            return "Medium Intensity"

