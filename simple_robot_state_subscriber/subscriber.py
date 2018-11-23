import rclpy
from rclpy.node import Node

from roboy_simulation_msgs.msg import Tendon


class TendonStateSubscriber(Node):

    def __init__(self):
        super().__init__('tendon_state_subscriber')
        self.subscription = self.create_subscription(
            Tendon,
            'tendon_state',
            self.listener_callback)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Tendon length of %s is %s ' % (msg.name[0], str(msg.l[0])) )


def main(args=None):
    rclpy.init(args=args)

    tendon_subscriber = TendonStateSubscriber()

    rclpy.spin(tendon_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
