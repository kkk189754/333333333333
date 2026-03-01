import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64MultiArray  #导入消息类型
import random

class Nums(Node):

    def __init__(self, node_name):  #添加node_name参数

        super().__init__(node_name)  #调用父类的初始化函数，传入节点名称

        #创建并声明订阅者，传入订阅类型,话题名字，回调函数（接收消息调用的函数）,队列大小（服务质量设置）

        self.sub_num = self.create_subscription(Int64MultiArray,'calculator',self.calculate_callback,10)#继承Node创建订阅者的功能

    def calculate_callback(self,msg):

        sum = msg.data[0]+msg.data[1]#接收的相加

        self.get_logger().info(f'{sum}')#打印结果

def main(args=None):

    rclpy.init(args=args)
    
    #创建节点，传入节点名称

    node = Nums('subscriber')  #''节点名称
    
    rclpy.spin(node)  #保持节点运行,ctrl+c结束运行
    
    rclpy.shutdown()  #关闭rclpy

if __name__ == '__main__':
    main()