import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import yaml

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('vesc_ackermann'),
        'config',
        'config.yaml'
    )
    config2 = os.path.join(
        get_package_share_directory('vesc_ackermann'),
        'config',
        'config2.yaml'
    )
    return LaunchDescription([
        Node(
            package='vesc_ackermann',
            executable='ackermann_manager_node',
            name='ackermann_manager_node',
            output='screen',
            parameters=[
                # yaml.safe_load(open(_DEFAULT_PARAMS_FILE, 'r')),
                config,
            ]
        )
    ])
