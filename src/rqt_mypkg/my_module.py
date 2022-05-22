import os
import rospy
import rospkg

from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget, QLabel, QDockWidget 
import time
#from posEncoder import PositionEncoder  
#rom datetime import datetime
from python_qt_binding.QtCore import QTimer,QDateTime

class MyPlugin(Plugin):

    def __init__(self, context):
        super(MyPlugin, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('MyPlugin')

          # Process standalone plugin command-line arguments
        from argparse import ArgumentParser
        parser = ArgumentParser()
        # Add argument(s) to the parser.
        parser.add_argument("-q", "--quiet", action="store_true",
                      dest="quiet",
                      help="Put plugin in silent mode")
        args, unknowns = parser.parse_known_args(context.argv())
        if not args.quiet:
            print 'arguments: ', args
            print 'unknowns: ', unknowns

        # Create QWidget
        self._widget = QWidget()
        # Get path to UI file which should be in the "resource" folder of this package
        ui_file = os.path.join(rospkg.RosPack().get_path('rqt_mypkg'), 'resource', 'Start_Stop_Cameras.ui')

        # Extend the widget with all attributes and children from UI file
        loadUi(ui_file, self._widget)
        # Give QObjects reasonable names
        self._widget.setObjectName('MyPluginUi')
        # Show _widget.windowTitle on left-top of each plugin (when 
        # it's set in _widget). This is useful when you open multiple 
        # plugins at once. Also if you open multiple instances of your 
        # plugin at once, these lines add number to make it easy to 
        # tell from pane to pane.
        if context.serial_number() > 1:
            self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        # Add widget to the user interface
        context.add_widget(self._widget)
     
        #link buttons to functions. 
        self._widget.pushButton_StartFrontCamera.clicked.connect(self.startFrontCamera)
        self._widget.pushButton_StopFrontCamera.clicked.connect(self.stopFrontCamera)
        self._widget.pushButton_StartBackCamera.clicked.connect(self.startBackCamra)
        self._widget.pushButton_StopBackCamera.clicked.connect(self.stopBackCamera)

    
    #functions to control the robot. 
    def manualControl(self):
        print("Manual control initiated!")
        #keyboard input, make it open in a new terminal?
        os.system("rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/new_robot_urdf_diff_drive_controller/cmd_vel")
        #add button/interface for the controller 
    
    def startFrontCamera(self):
        print("The front camera is being launched...")
        #os.system("bash runJoy.sh") #needed to be in dir to run

        #runs file from root dir
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        DATA_PATH = os.path.join(BASE_DIR, "usb_cam0.launch")
        os.system("roslaunch usb_cam usb_cam0.launch")

        rospy.loginfo("Front Camera STARTED!")
        #print("Front Camera STARTED!")
    def stopFrontCamera(self):
        print("The front camera is being stopped...")
        #os.system("bash runJoy.sh") #needed to be in dir to run

        #runs file from root dir
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        DATA_PATH = os.path.join(BASE_DIR, "kill_usb_cam0.sh")
        #print(str(BASE_DIR))
        #print(str(DATA_PATH))
        #os.system("bash /home/nayal/nasa_ws/src/rqt_mypkg/src/rqt_mypkg/kill_usb_cam0.sh")
        #print("bash " + str(DATA_PATH))
        os.system("bash " + str(DATA_PATH))
        
        #os.system()
        rospy.loginfo("Front Camera STOPPED!")
        #print("Front Camera STOPPED!")
    def startBackCamra(self):
        print("The back camera is being launched...")
        #os.system("bash runJoy.sh") #needed to be in dir to run

        #runs file from root dir
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        DATA_PATH = os.path.join(BASE_DIR, "usb_cam1.launch")
        os.system("roslaunch usb_cam usb_cam1.launch")

        rospy.loginfo("Back camera STARTED!")
        #print("Back camera STARTED!")
    def stopBackCamera(self):
        print("The stop camera is being launched...")
        #os.system("bash runJoy.sh") #needed to be in dir to run

        #runs file from root dir
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        DATA_PATH = os.path.join(BASE_DIR, "kill_usb_cam1.sh")
        #os.system("bash /home/nayal/nasa_ws/src/rqt_mypkg/src/rqt_mypkg/kill_usb_cam1.sh")
        os.system("bash " + str(DATA_PATH))
        
        rospy.loginfo("Back camera STOPPED!") 
        #print("Back camera STOPPED!")            
   
    def shutdown_plugin(self):
        # TODO unregister all publishers here
        pass

    def save_settings(self, plugin_settings, instance_settings):
        # TODO save intrinsic configuration, usually using:
        # instance_settings.set_value(k, v)
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        # TODO restore intrinsic configuration, usually using:
        # v = instance_settings.value(k)
        pass

    #def trigger_configuration(self):
        # Comment in to signal that the plugin has a way to configure
        # This will enable a setting button (gear icon) in each dock widget title bar
        # Usually used to open a modal configuration dialog