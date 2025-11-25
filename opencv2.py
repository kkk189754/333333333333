import cv2
import numpy as np

img = cv2.imread("1.jpg")

if img is None:#检查是否读取成功

    print("错误：无法读取图像")

    exit()

black = img.copy()#创建图像的深拷贝，避免修改原始图像数据

white = cv2.inRange(img, np.array([200,200,200]), np.array([255,255,255]))#创建白色区域的掩码

black[white > 0] = [0, 0, 0]#将白色区域设置为黑色

cv2.imshow("Black Background Result", black)

key = cv2.waitKey(0)#等待用户按键，参数0表示无限等待，直到用户按下任意键

if key == ord('s'):  #如果按下's'键

    cv2.imwrite('/home/abctfd/tu/3.jpg',black)#保存

    print("图片已保存: /home/abctfd/tu/3.jpg")

else:  #如果按下其他键

    print("图像未保存。")