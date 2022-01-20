#!/usr/bin/env python
# Note you can implement this code in your project , but if you wanna impplement or make changes to the code kindly make sure you add the link  to where the code was initially gotten from 
import rospy 
from geometry_msgs.msg import Twist


# code to make a vehicle to move in rotation motion 

# setting the initial velocity of the linear parameters
x = 0
y = 0 
z = 0
command_velocity = '/cmd_vel'




rospy.init_node ('rotate_of_robot',anonymous=True) 
velocity = Twist()
linear_values= [2,4,5]
velocity.linear.x = linear_values[0]
velocity.angular.z = 2
loop = rospy.Rate(10)
pub = rospy.Publisher(command_velocity,Twist,queue_size=1)
speed = 2
time = 4
distance = speed * time

if distance == 8:
    velocity.linear.x = 5
    rospy.Duration(2)
    velocity.angular.z = 2


while not rospy.is_shutdown():
    rospy.loginfo("Now the code of the robot can be executed,The robot rotates")
    pub.publish(velocity)
