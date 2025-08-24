#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from PIL import Image as PILImage
import numpy as np

class ImageSaver:
    def __init__(self):
        rospy.init_node('image_saver', anonymous=True)
        self.bridge = CvBridge()

        # Subscribing to the RGB and depth image topics
        rospy.Subscriber('/kortex/camera/color/image_raw', Image, self.rgb_callback)
        rospy.Subscriber('/kortex/camera/depth/image_raw', Image, self.depth_callback)

        self.rgb_image = None
        self.depth_image = None

    def rgb_callback(self, msg):
        try:
            rospy.loginfo("RGB callback triggered.")
            self.rgb_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            rospy.loginfo("RGB image converted successfully.")
        except Exception as e:
            rospy.logerr(f"Failed to convert RGB image: {e}")

    def depth_callback(self, msg):
        try:
            rospy.loginfo("Depth callback triggered.")
            self.depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
            rospy.loginfo("Depth image converted successfully.")
        except Exception as e:
            rospy.logerr(f"Failed to convert Depth image: {e}")
    
    def save_images(self):
        """Save RGB and Depth images to files."""
        if self.rgb_image is not None:
            rospy.loginfo(f"RGB Image shape: {self.rgb_image.shape}")
            rgb = cv2.cvtColor(self.rgb_image, cv2.COLOR_BGR2RGB)
            rgb_pil = PILImage.fromarray(rgb)
            rgb_pil.save("test_rgb.png")
            rospy.loginfo("Saved RGB image as test_rgb.png")


        if self.depth_image is not None:
            rospy.loginfo(f"Depth Image shape: {self.depth_image.shape}")
            depth = self.depth_image * 1000
            depth = np.nan_to_num(depth)
            depth = depth.astype(np.uint32)
            depth_pil = PILImage.fromarray(depth)
            depth_pil.save("test_depth.png")
            rospy.loginfo("Saved Depth image as test_depth.png")

    def run(self):
        rospy.loginfo("Waiting for images...")
        rospy.sleep(10)  # Allow more time to receive images
        self.save_images()


if __name__ == "__main__":
    try:
        saver = ImageSaver()
        saver.run()
    except rospy.ROSInterruptException:
        pass
