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
    
    int h = img.rows;//获取图像尺寸

    int w = img.cols;//获取图像尺寸
    
    Point2f center(w/2.0f,h/2.0f);//计算旋转中心点
    
    Mat M = getRotationMatrix2D(center,45,1.0);//计算45度旋转的变换矩阵
    
    Mat X_img;

    warpAffine(img,X_img,M,img.size());//旋转
    
    namedWindow("TTT",WINDOW_NORMAL);

    imshow("TTT",X_img);
    
    while(true){//按q键关闭窗口

        int key = waitKey(0);

        if(key == 'q'){

            break;

        }
    }

    destroyAllWindows();

    return 0;
}