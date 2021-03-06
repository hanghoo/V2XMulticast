# -*- coding: utf-8 -*-
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np
from matplotlib import pyplot as plt


img0 = cv2.imread("tadpoles.jpg")
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gray, (9,9), 0) #高斯模糊，X,Y 方向的Ksiez分别为9和9

params = cv2.SimpleBlobDetector_Params()
#斑点检测的可选参数
#params.minThreshold= 10 #亮度最小阈值控制
#params.maxThreshold = 255 #亮度最大阈值控制
params.thresholdStep = 9 #亮度阈值的步长控制，越小检测出来的斑点越多

params.filterByColor = True #颜色控制
params.blobColor = 0 #只检测黑色斑点
#params.blobColor = 255 #只检测白色色斑点

params.filterByArea = True #像素面积大小控制
params.minArea = 20
#params.maxArea=2000

#params.filterByCircularity = True #圆度控制，圆度的定义是（4π×面积）/（周长的平方）
#params.minCircularity = 0.3

#params.filterByConvexity =True #凸度控制，凸性的定义是（斑点的面积/斑点凸包的面积
#params.minConvexity = 1.0

#params.filterByInertia = True# 惯性率控制
#params.minInertiaRatio = 0.2#圆形的惯性率等于1，惯性率越接近1，圆度越高

detector = cv2.SimpleBlobDetector_create(params)#创建斑点检测器
keypoints = detector.detect(gauss) #在哪个图上检测斑点
print("共检测出%d个斑点" %len(keypoints))

#在原图上画出检测到的斑点
im_with_keypoints=cv2.drawKeypoints(img0, keypoints, np.array([]), (0, 0, 255),
                                    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
print("斑点中心坐标为：")
for (x,y) in keypoints[0].convert(keypoints):
    print(x,",", y)
    cv2.circle(im_with_keypoints, (x,y), 1, (255,255,255), 1) #以白色标记处斑点中心（以斑点中心为中心画圆）

#绘出检测结果图
plt.subplot(1,1,1)
plt.imshow(cv2.cvtColor(im_with_keypoints, cv2.COLOR_BGR2RGB))
plt.title("OpenCV 斑点检测\n之小蝌蚪找妈妈",fontSize =16, color="b")
plt.show()