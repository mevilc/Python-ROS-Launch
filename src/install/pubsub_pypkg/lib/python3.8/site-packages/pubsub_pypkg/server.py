import rclpy
from rclpy import Node
from std_msgs.msg import Int32
from std_srvs.srv import Trigger


class Service(Node):
    def __init__(self):
        super.__init__('service')
        self.srv = self.create_service(Trigger, 'my_service', self.callback)

    def callback(self, request, response):
        response.success = True
        response.message = 'Recieved Trigger'
        return response


def main(args=None):
    rclpy.init(args=args)
    serv = Service()
    rclpy.spin(serv)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
