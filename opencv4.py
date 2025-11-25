import cv2
import numpy as np

img = cv2.imread("1.jpg")

if img is None:#检查是否读取成功

    print("错误：无法读取图像")

    exit()

m_img = img.copy()#创建图像的深拷贝，避免修改原始图像数据

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#转换为灰度图像

_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)#图像二值化

kernel = np.ones((3,3), np.uint8)#创建膨胀核

dilated = cv2.dilate(binary, kernel, iterations=2)#对二值图像进行膨胀操作

contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# 查找轮廓

cv2.drawContours(m_img, contours, -1, (0, 0, 255), 2)#绘制轮廓

cv2.imshow("TTT", m_img)

key = cv2.waitKey(0)#等待用户按键，参数0表示无限等待，直到用户按下任意键

if key == ord('s'):  #如果按下's'键

    cv2.imwrite('/home/abctfd/tu/5.jpg',m_img)#保存

    print("灰度图已保存: /home/abctfd/tu/5.jpg")

else:  #如果按下其他键

    print("图像未保存。")