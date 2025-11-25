import cv2
import numpy as np

img_gray=cv2.imread('1.jpg',0)#转换为灰度图

if img_gray is None:#检查是否读取成功

    print("错误：无法读取图像")

    exit()

cv2.imshow('TTT',img_gray)#显示图片

key = cv2.waitKey(0)#等待用户按键，参数0表示无限等待，直到用户按下任意键

if key == ord('s'):  #如果按下's'键

    cv2.imwrite('/home/abctfd/tu/2.jpg',img_gray)#保存

    print("灰度图已保存: /home/abctfd/tu/2.jpg")

else:  #如果按下其他键

    print("图像未保存。")

cv2.destroyAllWindows()
