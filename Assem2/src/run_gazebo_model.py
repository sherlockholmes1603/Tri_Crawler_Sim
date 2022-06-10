#!/usr/bin/env python3
import rospy
from actuatorcontroller_ros.msg import ActuatorCommand
from std_msgs.msg import Float64

class CrawlerNode:
    def __init__(self, front_steer_id, front_motor_id, left_motor_id, right_motor_id):
        rospy.init_node("Crawler_Gazebo_node")
        rospy.loginfo("Starting CrawlerNode as crawler.")
        self.steer_id = front_steer_id
        self.front_id = front_motor_id
        self.left_id  = left_motor_id
        self.right_id = right_motor_id
        rospy.Subscriber("/INNFOS/setTargetVelocity", ActuatorCommand, self.vel_callback, queue_size=10)
        self.front_steer = rospy.Publisher("/simple_model/joint_1_position_controller/command", Float64, queue_size=10)
        self.front_motor = rospy.Publisher("/simple_model/joint_2_velocity_controller/command", Float64, queue_size=10)
        self.right_motor = rospy.Publisher("/simple_model/joint_3_velocity_controller/command", Float64, queue_size=10)
        self.left_motor = rospy.Publisher("/simple_model/joint_4_velocity_controller/command", Float64, queue_size=10)
        

        

    def vel_callback(self, data):
        # print(data)
        if data.JointID == self.steer_id:
            self.front_steer.publish(data.TargetValue/100)
            print("steer", data.TargetValue/100)
        if data.JointID == self.front_id:
            self.front_motor.publish(data.TargetValue/100)
            print("front", data.TargetValue/100)
        if data.JointID == self.left_id:
            self.right_motor.publish(data.TargetValue/100)
            self.front_motor.publish(data.TargetValue/100)
            self.left_motor.publish(data.TargetValue/100)
            print("right", data.TargetValue/100)
        if data.JointID == self.right_id:
            self.left_motor.publish(data.TargetValue/100)
            print("left",data.TargetValue/100)

    def update(self):
        pass

front_steer = 32
front_motor= 1
right_motor = 14
left_motor = 34

if __name__ == "__main__":
    
    front_steer =  rospy.get_param("/steeringid", 24)
    front_motor = rospy.get_param("/front_motorid", 74)
    left_motor = rospy.get_param("/left_motorid", 34)
    right_motor = rospy.get_param("/right_motorid", 14)
    crawler = CrawlerNode(front_steer, front_motor, left_motor, right_motor)
    while not rospy.is_shutdown():
        crawler.update()
    rospy.spin()