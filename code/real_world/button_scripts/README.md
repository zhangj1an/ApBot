# steps
firstly download `rls-robot-ws-proj`, `catkin make` it 
then, 
```~/rls-robot-ws-proj$ roslaunch launch_kortex_drivers kortex_driver.launch pc:=true start_rviz:=true```

use `rostopic list` to check for rostopics
the image topic is published to 

```rospy.Subscriber('/kortex/camera/color/image_raw', Image, self.rgb_callback)
rospy.Subscriber('/kortex/camera/depth/image_raw', Image, self.depth_callback)```
