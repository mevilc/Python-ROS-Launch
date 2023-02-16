import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Trigger


class Service(Node):
    def __init__(self):
        super().__init__('service')
        self.srv = self.create_service(Trigger, 'my_service', self.callback)
        self.publisher_ = self.create_publisher(Int32, 'my_service', 10)
        self.i = 0
        self.publish_msg()

    def publish_msg(self):
        msg = Int32()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info('%s' % msg.data)
        self.i += 1

    def callback(self, request, response):
        response.success = True
        response.message = 'Node B status: Trigger Recieved from Node A!'
        return response


def main(args=None):
    rclpy.init(args=args)
    serv = Service()
    rclpy.spin(serv)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
