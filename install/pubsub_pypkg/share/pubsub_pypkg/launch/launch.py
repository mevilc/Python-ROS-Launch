from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package="pubsub_pypkg",
            executable='Server',
            output='screen',
        ),
        Node(
            package="pubsub_pypkg",
            executable='Client',
            output='screen',
        ),
    ])
