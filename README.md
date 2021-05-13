# Class_demo
作业１：请用MATLAB或其它语言编写相关程序，输入一幅灰度图像。  
　　　　（１）按比例降低整幅图像灰度；  
　　　　（２）对降低灰度后的图像进行直方图均衡化处理；  
　　　　（３）在同一个窗口输出显示原始图像和２种结果图像。  
作业2：请用MATLAB或其它语言编写相关程序，输入一幅灰度图像，分别采用邻域平均法、均值滤波法、中值滤波法对图像进行平滑去噪，在同一个窗口输出显示原始图像和３种结果图像。  
作业３：请用MATLAB或其它语言编写相关程序，输入一幅灰度图像，分别采用梯度算子、拉普拉斯算子、Sobel算子、Prewitt算子对图像进行锐化，在同一个窗口输出显示原始图像和４种结果图像。


#Soluiton
工程目录基于python完成主要使用opencv，numpy，matlab函数库完成


##install
使用前需修改原始图像路径
```
git clone https://github.com/sevnxiaolu/Class_demo.git
cd Cla_demo
python class_work(one/two/three)
```

*函数库安装
```
pip install -r requirements.txt
```

#其他
因opencv与matlab函数库中图像读取格式问题可能会造成原始图像色差出现异常



