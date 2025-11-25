#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>  
using namespace cv;
using namespace std;

int main() {
   
    Mat img = imread("1.jpg");//读取图像

    if (img.empty()) {//检查是否读取成功

        cout << "错误：无法读取图像" << endl;

        return -1;

    }
    
    Mat M = img.clone();//创建图像的深拷贝，避免修改原始图像数据
    
    Mat gray;

    cvtColor(img, gray, COLOR_BGR2GRAY);//转换为灰度图像
    
    Mat X, Y;
    
    threshold(gray, X, 0, 255, THRESH_BINARY_INV | THRESH_OTSU);//图像二值化
    
    Mat N = getStructuringElement(MORPH_RECT, Size(3, 3));//创建膨胀核
    
    dilate(X, Y, N, Point(-1, -1), 2);//对二值图像进行膨胀操作
    
    vector<vector<Point>> contours;//存储轮廓点

    vector<Vec4i> hierarchy;//存储轮廓层级关系
    
    findContours(Y, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);//查找轮廓
    
    drawContours(M, contours, -1, Scalar(0, 0, 255), 2);//在原图上用红色绘制所有轮廓
    
    namedWindow("TTT", WINDOW_NORMAL);

    imshow("TTT", M);
    
    while(true) {//按q键关闭窗口

        int key = waitKey(0);

        if(key == 'q') {

            break;

        }
    }

    destroyAllWindows();

    return 0;
}