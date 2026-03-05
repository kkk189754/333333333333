import launch#导入ros2launch文件的核心库
import launch_ros#ros相关的launch功能
from ament_index_python.packages import get_package_share_directory#获取功能包的共享目录路径
import os#Python的系统库，用于路径操作

def generate_launch_description():

    #获取默认的urdf的路径

    urdf_package_path=get_package_share_directory('display')#传入功能包名字

    default_urdf_path = os.path.join(urdf_package_path,'urdf','dog.urdf')#传入urdf目录下的文件名

    #拼接urdf文件的完整路径

    with open(default_urdf_path,'r') as file:#open以只读打开urdf文件

        robot_description_content=file.read()#读取文件全部内容并存入变量

    #创建robot_state_publisher节点

    action_robot_state_publisher = launch_ros.actions.Node(

        package='robot_state_publisher',#使用robot_state_publisher功能包

        executable='robot_state_publisher',#运行该包的可执行文件

        parameters=[{'robot_description':robot_description_content}]#将urdf内容作为参数传递给节点

    )

    #创建joint_state_publisher节点，负责发布机器人关节状态（如果有可动关节）

    action_joint_state_publisher = launch_ros.actions.Node(

        package='joint_state_publisher',

        executable='joint_state_publisher',

    )

    #创建rviz2节点，打开rviz

    action_rviz_node=launch_ros.actions.Node(

        package='rviz2',

        executable='rviz2',

    )

    #返回启动描述，告诉ros按这个顺序启动这三个节点

    return launch.LaunchDescription([

        action_robot_state_publisher,

        action_joint_state_publisher,

        action_rviz_node,
    ])