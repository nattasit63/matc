#!/usr/bin/env python3
import time
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import os
from std_srvs.srv import Empty
import sys, errno  
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlee_interfaces.srv import Setgoal

class Controller(Node):
    def __init__(self,name,start_position):
        super().__init__(str(name)+'_controller')
        self.agent_name = name
        self.publisher = self.create_publisher(Twist,str(name)+'/cmd_vel',10)
        # self.command_publisher = self.create_publisher(Twist,str(name)+'/cmd_vel',10)
        self.pose_subscription = self.create_subscription(Pose,'/'+str(name)+'/pose',self.pose_callback,10)
        self.set_goal_service = self.create_service(Setgoal,'/'+str(name)+'_set_goal',self.set_goal_callback)
        self.goal = start_position
        self.start_point = start_position
        self.first = True
        self.is_arrive = 0
        self.pose = Pose()
        timer_period = 0.1
        self.timer = self.create_timer(timer_period,self.timer_callback)
    def timer_callback(self):
        msg = self.control()     
        self.publisher.publish(msg)
        if self.check_reach_goal() and self.is_arrive==0:
            self.is_arrive =1
            print(str(self.agent_name),' Arrive')
            return True

    def check_reach_goal(self):
        current_position = np.array([self.pose.x,self.pose.y])
        if not self.first:
            dp = self.goal-current_position
            if np.linalg.norm(dp)<0.2:
                return True

    def pose_callback(self,msg):
        self.pose = msg
    def set_goal_callback(self,request,response):
        self.first=False
        self.is_arrive=0
        self.goal = np.array([request.x,request.y])
        return response
    
    def control(self):
        global current_pose
        msg = Twist()
        current_position = np.array([self.pose.x,self.pose.y])
        current_pose = current_position
        dp = self.goal-current_position
        e = np.arctan2(dp[1],dp[0])-self.pose.theta
        K = 1.0
        w = K*np.arctan2(np.sin(e),np.cos(e))
        if np.linalg.norm(dp)>0.2:
            v = 0.5
        else:
            v = 0.0
            w = 0.0
        msg.linear.x = v
        msg.angular.z = w
        return msg


    

# def main(args=None):
#     rclpy.init(args=args)
#     turtlesimController = Controller()
#     rclpy.spin(turtlesimController)
#     turtlesimController.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()