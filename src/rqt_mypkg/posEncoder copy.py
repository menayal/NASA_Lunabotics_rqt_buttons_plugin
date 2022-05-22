#!/usr/bin/env python

import rospy
from std_msgs.msg import String


class PositionEncoder:
    def __init__(self):
        #instance variables here
        self.isRunning = False
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('chatter', String, self.callback)

        self.theData = "empty"


    def listener(self):
        rospy.Subscriber('chatter', String, self.callback)
        rospy.spin()




    def callback(self, data):
        #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
        print(data.data)
        self.theData = str(data.data)
        #return data.data

if __name__ == '__main__':
    pos = PositionEncoder()
    pos.listener()
