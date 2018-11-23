# ROS + ROS2 setup

1. Install ROS1 from binaries (assuming it's in `/opt/ros/kinetic`). Before proceeding with the next step, make sure you don't source ROS kinetic environment in you `~/bash.rc`, i.e. you should remove there the following line:
```
source /opt/ros/kinetic/setup.bash
```

2. Compile ROS2 `bouncy` from source without `ros1_bridge` following the instructions [here](https://index.ros.org/doc/ros2/Linux-Development-Setup/). 
As the last step instead of
```
colcon build --symlink-install
```
you should skip building the `ros1_brdige` by using 
```
colcon build --symlink-install --packages-skip ros1_bridge
```
From now on we will assume your ROS2 installation workspace is in `~/ros2_install`

3. Compile `roboy_communication` for ROS2
```
# in a new terminal
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/Roboy/roboy_communication.git
cd roboy_communication
git checkout bouncy
cd ~/ros2_ws
source ~/ros2_install/install/setup.bash
colcon build --symlink-install
```

4. Build refactored CARDSflow (with ROS1)
```
# in a new terminal
cd <path_to_CARDSflow>
git checkout ros2-refactor
git submodule init
git submodule update
source /opt/ros/kinetic/setup.bash
cd <catkin_ws_with_CARDSflow>
catkin_make
```

5. Build `ros1_bridge` (you can find more instruction [here](https://github.com/ros2/ros1_bridge))
```
# in a new terminal
# source both ROS distros
source /opt/ros/kinetic/setup.bash
source ~/ros2_install/install/setup.bash

# source both workspaces with roboy_communication
source <catkin_ws_with_CARDSflow>/devel/setup.bash
source ~/ros2_ws/install/setup.bash

# build ros_1 bridge
cd ~/ros2_install
colcon build --symlink-install --packages-select ros1_bridge --cmake-force-configure
```

6. Test the bridge using CARDSflow and `simple_robot_state_subscriber`
```
# in a new terminal
source ~/ros2_install/install/setup.bash
cd ~/ros2_ws/src
git clone https://github.com/Roboy/deep_roboy_contol.git
cd deep_roboy_control/simple_robot_state_subscriber
python3 subscriber.py
```

```
# in a new terminal
source <catkin_ws_with_CARDSflow>/devel/setup.bash
roslaunch kindyn robot.launch robot_name:=msj_platform start_controllers:='sphere_axis0 sphere_axis1 sphere_axis2
```

```
# in a new terminal

# source both ROS distros
source /opt/ros/kinetic/setup.bash
source ~/ros2_install/install/setup.bash

# source both workspaces with roboy_communication
source <catkin_ws_with_CARDSflow>/devel/setup.bash
source ~/ros2_ws/install/setup.bash

ros2 run ros1_bridge dynamic_bridge
```

You should now see the `subscriber.py` script printing messages published by CARDSflow.

