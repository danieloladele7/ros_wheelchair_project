import sys
import termios
import tty # teletype writer

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__("keyboard_pub_node")
        self.pub = self.create_publisher(String, "keyboard_pub_topic", 10)
        self.timer = self.create_timer(0.2, self.publish_keyboard)
        self.settings = self.saveTerminalSettings()
        
    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def saveTerminalSettings(self):
        return termios.tcgetattr(sys.stdin)

    def restoreTerminalSettings(self):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)

    def publish_keyboard(self):
        msg = String()
        msg.data = self.getKey()
        if msg.data == "X":
            quit()
        self.pub.publish(msg)
        self.restoreTerminalSettings()


def main():
    rclpy.init()
    key_pub = KeyboardPublisher()

    print("Publisher Node Running...")
    
    try:
        rclpy.spin(key_pub)
    except KeyboardInterrupt:
        key_pub.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()