import rclpy
from rclpy.node import Node

from roboy_simulation_msgs.msg import Tendon
from roboy_simulation_msgs.msg import JointState


class TendonStateSubscriber(Node):

    def __init__(self):
        super().__init__('tendon_state_subscriber')
        self.subscription = self.create_subscription(
            Tendon,
            'tendon_state',
            self.listener_callback)
        self.subscription1 = self.create_subscription(
            JointState,
            'joint_state',
            self.listener_callback1)
        self.subscription  # prevent unused variable warning
        self.subscription1

    def listener_callback(self, msg):
        self.get_logger().info('Tendon length of %s is %s ' % (msg.name[0], str(msg.l[0])) )
    def listener_callback1(self, msg):
        self.get_logger().info('Joint angle in radian of %s is %s ' % (msg.names[0], str(msg.q[0])) )

def main(args=None):
    rclpy.init(args=args)

    tendon_subscriber = TendonStateSubscriber()



    rclpy.spin(tendon_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
