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
    
    Mat channels[3];

    split(img, channels);//分离BGR通道
    
    Mat zeros = Mat::zeros(img.size(),CV_8UC1);//创建全零矩阵
    
    Mat blue_img, green_img,red_img;//创建单通道图像
    
    Mat red[] = {zeros,zeros,channels[2]};//红色通道图像

    merge(red,3,red_img);
    
    Mat green[] = {zeros,channels[1],zeros}; //绿色通道图像

    merge(green,3,green_img);
    
    Mat blue[] = {channels[0],zeros,zeros}; //蓝色通道图像

    merge(blue,3,blue_img);
    
    namedWindow("T",WINDOW_NORMAL);

    namedWindow("TT",WINDOW_NORMAL);

    namedWindow("TTT",WINDOW_NORMAL);
    
    imshow("T",blue_img);

    imshow("TT",green_img);

    imshow("TTT",red_img);
    
    while(true){//按q键关闭窗口

        int key = waitKey(0);

        if(key == 'q'){

            break;

        }
    }

    destroyAllWindows();

    return 0;
    
}