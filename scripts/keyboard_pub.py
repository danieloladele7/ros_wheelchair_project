import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import sys

if sys.platform == 'win32':
    import msvcrt
else:
    import termios
    # terminal control function. Build for UNIX
    import tty # teletype writer

class keyboardPublisher(Node):
    def __init__(self):
        super().__init__("keyboard_pub_node")
        self.pub = self.create_publisher(String, "keyboard_pub_topic", 10)
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.publish_keyboard)
        settings = self.saveTerminalSettings()

    def getKey(settings):
        if sys.platform == 'win32':
            # getwch() returns a string on Windows
            key = msvcrt.getwch()
        else:
            tty.setraw(sys.stdin.fileno())
            key = sys.stdin.read(1)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

    def saveTerminalSettings():
        if sys.platform == 'win32':
            return None
        return termios.tcgetattr(sys.stdin)

    def restoreTerminalSettings(old_settings):
        if sys.platform == 'win32':
            return
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    def execute(key):
        print('You pressed {} on the keyboard'.format(key))

    def publish_keyboard(self):
        msg = String()
        msg.data = self.execute()
        self.pub.publish(msg)