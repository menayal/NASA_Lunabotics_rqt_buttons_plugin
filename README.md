
# NASA_Lunabotics_rqt_buttons_plugin

This is all the files related to the custom plugin being developed for a user interface. This plugin has multiple buttons that control various functions of the robot. 


## Steps to get it running

 - Git clone my other [repo](https://github.com/menayal/NASA_Lunabotics_Robot_Files/tree/updatingPackagePython2)
    -  Use the updatingPackagePython2 branch if using Python 2
 - Run this command in your catkin workspace:
    
    ```bash
    roslaunch new_robot_urdf nasa_bot.launch
    ```
 - This command launches the robot in gazebo and starts up the GUI with the created plugin.
 ### Note

   - Currently, the manual button function, launches the keyboard control in the terminal where the robot is running. To exit the keyboard input, you will need to press Control C. However, this also quits running the robot. This will be fixed in the future. 
   - The autonomous movement and stop button have not been developed yet. 




