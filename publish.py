import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64MultiArray  #导入消息类型
import random

class Nump(Node):

    def __init__(self, node_name):  #添加node_name参数

        super().__init__(node_name)  #调用父类的初始化函数，传入节点名称
        
        #创建并声明发布者，传入话题类型，话题名字，队列大小(服务质量设置)

        self.pub_num = self.create_publisher(Int64MultiArray, 'calculator', 10)#继承Node创建发布者的功能

        self.timer_period = 3

        #传入周期（几秒调用一次函数，也就是几秒发布一次），定时回调函数（先定义一个函数）

        self.timer = self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):

        msg = Int64MultiArray()  #对Int64类实例化

        msg.data = [random.randint(0, 99),random.randint(0, 999)]#随机取数字
        
        #发布消息

        self.pub_num.publish(msg)  #使用publish方法
        
        #打印日志

        self.get_logger().info(f'发布了两个数字：{msg.data[0],msg.data[1]}')

def main(args=None):

    rclpy.init(args=args)
    
    #创建节点，传入节点名称

    node = Nump('publisher')  #''节点名称
    
    rclpy.spin(node)  #保持节点运行,ctrl+c结束运行
    
    rclpy.shutdown()  #关闭rclpy

if __name__ == '__main__':
    main()