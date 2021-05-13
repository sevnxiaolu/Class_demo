# @Time : 2021-05-13 12:41 
# @Author : Seven
# -*- coding:utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
'''
作业2：请用MATLAB或其它语言编写相关程序
输入一幅灰度图像，分别采用邻域平均法、均值滤波法、中值滤波法对图像进行平滑去噪
在同一个窗口输出显示原始图像和３种结果图像。

'''


'''
均值滤波: 均值滤波是指任意一点的像素值，都是周围N*M个像素值的均值
result = cv2.blur(图像, 核大小)，其中核大小是以(宽度, 高度)
'''
def mean_value(img):
    source = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    # 均值滤波
    result = cv2.blur(source, (5, 5))
    return result

'''
中值滤波:  在使用邻域平均法去噪的同时也使得边界变得模糊
而中值滤波是非线性的图像处理方法，在去噪的同时可以兼顾到边界信息的保留
使用CV函数中cv2.medianBlur实现
'''
def median_value(img):
    #中值滤波
    result = cv2.medianBlur(img, 5)
    return result

'''
即把当前图像 和它周围8个像素的灰度值相加，然后将求得的平均值（除以9）作为该点的像素值
原始图像需要转化灰度图进行灰度值计算
后期未做图像色彩还原
'''
def neighborhood_value(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 加上椒盐噪声
    param = 20
    # 灰阶范围
    w = img.shape[1]
    h = img.shape[0]
    newimg = np.array(img)

    # 噪声点数量
    noisecount = 100000
    for k in range(0, noisecount):
        xi = int(np.random.uniform(0, newimg.shape[1]))
        xj = int(np.random.uniform(0, newimg.shape[0]))
        newimg[xj, xi] = 255

    # 邻域平均法去噪
    # 脉冲响应函数，核函数
    # 图像四个边的像素处理
    lbimg = np.zeros((h + 2, w + 2), np.float32)
    tmpimg = np.zeros((h + 2, w + 2))
    myh = h + 2
    myw = w + 2
    tmpimg[1:myh - 1, 1:myw - 1] = newimg[0:myh, 0:myw]

    # 用领域平均法的（设半径为2）脉冲响应函数
    a = 1 / 8.0
    kernel = a * np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    for y in range(1, myh - 1):
        for x in range(1, myw - 1):
            lbimg[y, x] = np.sum(kernel * tmpimg[y - 1:y + 2, x - 1:x + 2])
    resultimg = np.array(lbimg[1:myh - 1, 1:myw - 1], np.uint8)
    result = cv2.cvtColor(resultimg,cv2.COLOR_BGR2RGB)
    return result


#图像加载函数
def showimg(i,name,img):
    plt.subplot(2,2,i)
    plt.title(name)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])

if __name__ == '__main__':
    img = cv2.imread("test_picture/test1.jpg")
    showimg(1,'original image',img)
    img1 = mean_value(img)
    showimg(2,'mean_img',img1)
    img2 = median_value(img)
    showimg(3,'median image',img2)
    img3 = neighborhood_value(img)
    showimg(4,'neighborhood image',img3)
    plt.show()



