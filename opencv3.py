import cv2
import numpy as np

img = cv2.imread("1.jpg")

if img is None:#检查是否读取成功

    print("错误：无法读取图像")

    exit()

b,g,r = cv2.split(img)#分离BGR通道

zeros = np.zeros_like(b)#创建与通道相同大小的全零矩阵

red= cv2.merge([zeros, zeros, r])#创建只显示红色通道的图像

green= cv2.merge([zeros, g, zeros])#创建只显示绿色通道的图像

blue = cv2.merge([b, zeros, zeros])#创建只显示蓝色通道的图像

cv2.imshow("TTTB", red)

cv2.imshow("TTTG", green)

cv2.imshow("TTTR", blue)

key = cv2.waitKey(0)#等待用户按键，参数0表示无限等待，直到用户按下任意键

if key == ord('s'):  #如果按下's'键

    cv2.imwrite('/home/abctfd/tu/4(1).jpg',red)#保存

    cv2.imwrite('/home/abctfd/tu/4(2).jpg',green)#保存

    cv2.imwrite('/home/abctfd/tu/4(3).jpg',blue)#保存


    print("图片已保存: /home/abctfd/tu/4(1).jpg")      

    print("图片已保存: /home/abctfd/tu/4(2).jpg")

    print("图片已保存: /home/abctfd/tu/4(3).jpg")

else:  #如果按下其他键

    print("图像未保存。")