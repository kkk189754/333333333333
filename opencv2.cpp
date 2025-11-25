#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
using namespace std;

int main() {

    Mat img = imread("1.jpg");//读取图像

    if (img.empty()) {//检查是否读取成功

        cout << "错误：无法读取图像" << endl;

        return -1;
        
    }
    
    Mat black = img.clone();//创建图像的深拷贝，避免修改原始图像数据
    
    Mat white;//创建掩码对象
   
    inRange(img,Scalar(200,200,200),Scalar(255,255,255),white);//创建白色区域的掩码
    
    black.setTo(Scalar(0,0,0),white);//将白色区域设置为黑色
    
    namedWindow("TTT",WINDOW_NORMAL);
    
    imshow("TTT",black);

    while(true){//按q键关闭窗口

        int key = waitKey(0);

        if(key == 'q'){

            break;

        }
    }

    destroyAllWindows();

    return 0;
}