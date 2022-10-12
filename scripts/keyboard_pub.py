import rclpy
from get_key_pressed import execute
from rclpy.node import Node
from std_msgs.msg import String

class KeyboardPublisher(Node):
    def __init__(self, key):
        super().__init__("keyboard_pub_node")
        self.pub = self.create_publisher(String, "keyboard_pub_topic", 10)
        self.timer = self.create_timer(2, self.publish_keyboard)
        self.key = key
        
    def publish_keyboard(self):
        msg = String()
        msg.data = self.key
        self.pub.publish(msg)

def main():
    key = execute()
    rclpy.init()
    key_pub = KeyboardPublisher(key)

    print("Publisher Node Running...")
    
    try:
        rclpy.spin(key_pub)
    except KeyboardInterrupt:
        key_pub.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()