import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

class ImageSaver(Node):
    def __init__(self):
        super().__init__('image_saver')
        self.subscription = self.create_subscription(
            Image,
            '/zed/zed_node/rgb_raw/image_raw_color',
            self.listener_callback,
            10)
        self.bridge = CvBridge()
        self.frame_count = 0
        self.save_path = '/home/edward/Documents/Code/BUR/BagToFrames/frames'
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def listener_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        filename = os.path.join(self.save_path, f'image_{self.frame_count:04d}.png')
        cv2.imwrite(filename, cv_image)
        self.frame_count += 1
        self.get_logger().info(f'Saved frame {self.frame_count}')

def main(args=None):
    rclpy.init(args=args)
    image_saver = ImageSaver()
    rclpy.spin(image_saver)
    image_saver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
