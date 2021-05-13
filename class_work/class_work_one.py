# @Time : 2021-05-13 9:53 
# @Author : Seven
# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
'''
作业１：请用MATLAB或其它语言编写相关程序，输入一幅灰度图像。
　　　　（１）按比例降低整幅图像灰度；
　　　　（２）对降低灰度后的图像进行直方图均衡化处理；
　　　　（３）在同一个窗口输出显示原始图像和２种结果图像。
'''

# 统计各灰度值的像素个数
def histogram(image):
    (row, col) = image.shape
    hist = [0] * 256
    for i in range(row):
        for j in range(col):
            hist[image[i, j]] += 1
    return hist


# 全局灰度线性变换
def global_linear_transmation(img):  # 将灰度范围设为0~255
    maxV = img.max()
    minV = img.min()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = ((img[i, j] - minV) * 255) / (maxV - minV)
    return img

#图像加载函数
def showimg(i,name,img,color):
    plt.subplot(2,2,i)
    plt.title(name)
    plt.imshow(img,color)
    plt.xticks([])
    plt.yticks([])

if __name__ == '__main__':

    image0 = cv2.imread("test_picture/test2.jpg",1)
    showimg(1,'original image',image0,None)
    image1 = cv2.imread("test_picture/test2.jpg",0)
    image2 = global_linear_transmation(image1)
    showimg(3,'gray image',image2,"gray")
    # 统计变换后图像的各灰度值像素的个数
    image_hist1 = histogram(image2)

    plt.subplot(2, 2, 4)
    plt.title('histogram image')
    plt.plot(image_hist1)
    plt.show()
