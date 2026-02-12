# WK3 Day12 Topic communication (ROS2)

## Goal
To understand the flow fo Publisher -> Topic -> Subscriber

## Command
-the list of topic: :'ros2 topic list'
-type/connections: 'ros2 topic info /chatter'

-tranciver: 'ros2 topic pub /chatter std_msg/String "{data: 'hello'}" -r 2'
-receiver: 'ros2 topic echo /chatter'
-Herz: 'ros2 topic hz /chatter'
-Band: 'ros2 topic bw /chatter'

## Learned
-Can connect if the name of topic and type is as same.
-Enable to send whether Subscriber is or not.
-can connect many to may.

