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
        ui_file = os.path.join(rospkg.RosPack().get_path('rqt_mypkg'), 'resource', 'ThreeButtonsWithLabels.ui')

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
        self._widget.pushButton_Manual.clicked.connect(self.manualControl)
        self._widget.pushButton_Autonomy.clicked.connect(self.autonomy)
        self._widget.pushButton_STOP.clicked.connect(self.stop)

        #create obj for subscriber
        # sampleSub = PositionEncoder()
        #now = datetime.now()
        #current_time = now.strftime("%H:%M:%S")

        #get the position encoder values
        #self._widget.QLabel_positionEncoder1.setText(self.getPositionEncoder1())
        #self.getPositionEncoder1()
        #while True:
            # self._widget.QLabel_positionEncoder1.setText(str(sampleSub.listener()))
            #self._widget.QLabel_positionEncoder1.setText("1")
        
        #testing out qTimer
        self.timer=QTimer()
        #starts show time function
        self.timer.timeout.connect(self.showTime)

        #refreshes every millisecond
        self.timer.start(1000)

        self._widget.QLabel_positionEncoder2.setText(self.getPositionEncoder2())
        self._widget.QLabel_tempAugerMotor.setText(self.getTempAugerMotor())
        self._widget.QLabel_currentAugerMotor.setText(self.getCurrentAugerMotor())
        self._widget.QLabel_batteryVoltage.setText(self.getBatteryVoltage())
        self._widget.QLabel_velocityAugerMotor.setText(self.getVelocityAugerMotor())
        #self.textEdit.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")

    #updatin the time here
    def showTime(self):
        time=QDateTime.currentDateTime()
        timeDisplay=time.toString('mm:ss dddd')
        self._widget.QLabel_positionEncoder1.setText(timeDisplay)
    
    #functions to get the encoder values
   #def getPositionEncoder1(self):
    #    self._widget.QLabel_positionEncoder1.setText("from funct")
    def getPositionEncoder2(self):
        return "pos enc 2.."
    def getTempAugerMotor(self):
        return "temp.."
    def getCurrentAugerMotor(self):
        return "current.."
    def getBatteryVoltage(self):
        return "voltage.."
    def getVelocityAugerMotor(self):
        return "velo.."
    #functions to control the robot. 
    def manualControl(self):
        print("Manual control initiated!")
        #keyboard input, make it open in a new terminal?
        os.system("rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/new_robot_urdf_diff_drive_controller/cmd_vel")
        #add button/interface for the controller 
    
    def autonomy(self):
        print("autonomous control initiated!")
   
    def stop(self):
        print("STOP process initiated!")
        self.timer.stop()
        self._widget.QLabel_positionEncoder1.setText("STOPPPED")

        #will need to publish some geo twist messages here to stop from driving

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