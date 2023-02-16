import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Trigger


class Client(Node):
    def __init__(self):
        super().__init__('client')
        self.client = self.create_client(Trigger, 'my_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service unavailable')
        self.req = Trigger.Request()

    def send_request(self):
        #self.req.data = bool(sys.argv[1])
        self.future = self.client.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)
    cli = Client()
    cli.send_request()

    while rclpy.ok():
        rclpy.spin_once(cli)
        if cli.future.done():
            try:
                response = cli.future.result()
            except Exception as e:
                cli.get_logger().info('Service call failed %r' % (e,))
            else:
                cli.get_logger().info('%s' % (response.message))
            break

    cli.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
