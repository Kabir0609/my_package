from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_descrption():
    return LaunchDescription([ 
        Node(
            package='demo_nodes_cpp',
            executable='talker'
        )
    ])