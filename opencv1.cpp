#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
using namespace std;

int main() {

    Mat img = imread("1.jpg");//读取图像

    if (img.empty()) {//检查是否读取成功

        cout << "错误：无法加载图像，请检查路径是否正确。" << endl;

        return -1;

    }

    Mat gray_img;

    cvtColor(img, gray_img, COLOR_BGR2GRAY);//转换为灰度图

    imshow("TTT", gray_img);

    while(true){//按q键关闭窗口

        int key=waitKey(0);

        if(key=='q'){

            break;

        }
    }

    destroyAllWindows();

    return 0;
}