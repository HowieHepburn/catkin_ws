#!/usr/bin/env python3
# coding=utf-8

import rospy
import tf2_ros
from tf.transformations import quaternion_from_euler 
from geometry_msgs.msg import TransformStamped


if __name__ == "__main__":
    rospy.init_node("tf_broad_node")

    broad = tf2_ros.StaticTransformBroadcaster()   #坐标变换专用数据发送函数
    
    broad_msg = TransformStamped()

    broad_msg.header.frame_id = "world"  #坐标系id
    broad_msg.header.stamp = rospy.Time.now()  #时间戳
    broad_msg.header.seq = 101  #序列号

    broad_msg.child_frame_id = "laser" #子坐标系
   
    # 子坐标系相对于父坐标系的偏移量
    broad_msg.transform.translation.x = 0.2 
    broad_msg.transform.translation.y = 0.0
    broad_msg.transform.translation.z = 0.5 

    # 四元数 从欧拉角转换，然后设置四元数
    qtn = quaternion_from_euler(0,0,0)
    broad_msg.transform.rotation.x = qtn[0]
    broad_msg.transform.rotation.y = qtn[1]
    broad_msg.transform.rotation.z = qtn[2]
    broad_msg.transform.rotation.w = qtn[3]

    # rate=rospy.Rate(1)
    
    # while not rospy.is_shutdown():
    broad.sendTransform(broad_msg)
    rospy.spin()
    # rate.sleep()