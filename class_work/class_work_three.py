# @Time : 2021-05-13 12:49 
# @Author : Seven
# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np
'''
作业３：请用MATLAB或其它语言编写相关程序，输入一幅灰度图像
分别采用梯度算子、拉普拉斯算子、Sobel算子、Prewitt算子对图像进行锐化
在同一个窗口输出显示原始图像和４种结果图像。
'''
#图像加载函数
def showimg(i,name,img,color):
    plt.subplot(2,3,i)
    plt.title(name)
    plt.imshow(img,color)
    plt.xticks([])
    plt.yticks([])

#梯度算子
def gradient_img(img):
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
    kernely = np.array([[0, -1], [1, 0]], dtype=int)
    x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
    y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)
    # 转转成uint8
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    result = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    return result

#拉普拉斯算子
def laplace_img(img):
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dst = cv2.Laplacian(grayImage, cv2.CV_16S, ksize=3)
    result = cv2.convertScaleAbs(dst)
    return result

#sobel算子
def sobel_img(img):
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x = cv2.Sobel(grayImage, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(grayImage, cv2.CV_16S, 0, 1)
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    result = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    return result

#prewitt算子
def prewitt_img(img):
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
    x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
    y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)
    # 转转成uint8
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    result = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    return result




if __name__ == '__main__':
    img = cv2.imread('test_picture/test4.jpg')
    showimg(1,'original image',img,None)
    img1 = gradient_img(img)
    showimg(3,'gradient image',img1,"gray")
    img2 = laplace_img(img)
    showimg(4,'laplace image',img2,"gray")
    img3 = sobel_img(img)
    showimg(5, 'sobel image', img3, "gray")
    img4 = prewitt_img(img)
    showimg(6, 'prewitt image', img4, "gray")
    plt.show()