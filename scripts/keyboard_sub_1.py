import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class keyboardSubscriber(Node):
    def __init__(self):
        super().__init__("keyboard_sub_node")
        self.sub = self.create_subscription(String, "keyboard_pub_topic",
                                            self.subscriber_callback, 10)

    def subscriber_callback(self, msg):
        print("Received: " + msg.data)



def main():
    rclpy.init()

    keyboard_sub = keyboardSubscriber()

    print("Waiting for data to be publisher over topic...")

    try:
        rclpy.spin(keyboard_sub)
    except KeyboardInterrupt:
        keyboard_sub.destroy_node()
        rclpy.shutdown()



if __name__ == '__main__':
    main()
