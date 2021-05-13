# @Time : 2021-05-13 11:08 
# @Author : Seven
# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
from skimage import data

img = cv2.imread("/test_picture/test1.tif")

img = data.astronaut(img)


plt.figure()

plt.subplot(2,2,1)
plt.title("origin image")
plt.imshow(img)
plt.show()


