import cv2
import numpy as np

img = cv2.imread("1.jpg")

if img is None:#检查是否读取成功

    print("错误：无法读取图像")

    exit()

h, w = img.shape[:2]#获取图像尺寸

center = (w // 2, h // 2)#计算旋转中心点

M = cv2.getRotationMatrix2D(center, 45, 1.0)#计算旋转矩阵

x_img = cv2.warpAffine(img, M, (w, h))#旋转

cv2.imshow("TTT", x_img)

key = cv2.waitKey(0)#等待用户按键，参数0表示无限等待，直到用户按下任意键

if key == ord('s'):  #如果按下's'键

    cv2.imwrite('/home/abctfd/tu/6.jpg',x_img)#保存

    print("灰度图已保存: /home/abctfd/tu/6.jpg")

else:  #如果按下其他键

    print("图像未保存。")