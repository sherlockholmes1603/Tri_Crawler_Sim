# Tri_Crawler_Sim

To start 

```bash
roslaunch Assem2 gazebo.launch
```

Publish position for Steer

```bash
/simple_model/joint_1_position_controller/command
```

Publish Velocity for front motor

```bash
/simple_model/joint_2_velocity_controller/command
```

Publish Velocity for rear left motor

```bash
/simple_model/joint_3_velocity_controller/command
```

Publish Velocity for rear right motor

```bash
/simple_model/joint_4_velocity_controller/command
```



