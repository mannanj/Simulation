            '''#right arm
            if ( actuator.id == 9):
                set_j(right, rj[0], dyn2rad(actuator.current_position));
            if ( actuator.id == 10):
                set_j(right, rj[1], dyn2rad(actuator.current_position)); 
            if ( actuator.id == 11):
                set_j(right, rj[2], dyn2rad(actuator.current_position));  
            if ( actuator.id == 12):
                set_j(right, rj[3], dyn2rad(actuator.current_position));  
            if ( actuator.id == 13):
                set_j(right, rj[4], dyn2rad(actuator.current_position)); 
            if ( actuator.id == 14):
                set_j(right, rj[5], dyn2rad(actuator.current_position));''' 



           #bindings = {
              #  '.': (set_j_keyboard, [left, lj[6], 0.1], "left_w2 increase"),
              #  'n': (set_j_keyboard, [left, lj[6], -0.1], "left_w2 decrease"),
              #  'v': (set_j_keyboard, [right, rj[6], 0.1], "right_w2 increase"),
              #  'z': (set_j_keyboard, [right, rj[6], -0.1], "right_w2 decrease"),
             }    

	    if Flag == 0:
                print("Controlling joints. Press ? for help, Esc to quit.")
            if not done and not rospy.is_shutdown():
                c = baxter_external_devices.getch()
                if c:
                    #catch Esc or ctrl-c
                    if c in ['\x1b', '\x03']:
                        done = True
                        rospy.signal_shutdown("Example finished.")
                        clean_shutdown();
                    elif c in bindings:
                        cmd = bindings[c]
                        #expand binding to something like "set_j(right, 's0', 0.1)"
                        cmd[0](*cmd[1])
                        print("command: %s" % (cmd[2],))
                    else:
                        print("key bindings: ")
                        print("  Esc: Quit")
                        print("  ?: Help")
                        for key, val in sorted(bindings.items(),
                                               key=lambda x: x[1][2]):
                            print("  %s: %s" % (key, val[2]))
	    Flag =1;  


            '''left arm
            if ( actuator.id == 9):
                set_j(left, rj[0], dyn2rad(actuator.current_position));
            if ( actuator.id == 10):
                set_j(left, rj[1], dyn2rad(actuator.current_position)); 
            if ( actuator.id == 11):
                set_j(left, rj[2], dyn2rad(actuator.current_position));  
            if ( actuator.id == 12):
                set_j(left, rj[3], dyn2rad(actuator.current_position));  
            if ( actuator.id == 13):
                set_j(left, rj[4], dyn2rad(actuator.current_position)); 
            if ( actuator.id == 14):
                set_j(left, rj[5], dyn2rad(actuator.current_position));  
            '''
'''            if not done and not rospy.is_shutdown():
                c = baxter_external_devices.getch()
                if c:
                    #catch Esc or ctrl-c
                    if c in ['\x1b', '\x03']:
                        done = True
                        rospy.signal_shutdown("Example finished.")
                    elif c in bindings:
                        cmd = bindings[c]
                        #expand binding to something like "set_j(right, 's0', 0.1)"
                        cmd[0](*cmd[1])
                        print("command: %s" % (cmd[2],))
                    else:
                        print("key bindings: ")
                        print("  Esc: Quit")
                        print("  ?: Help")
                        for key, val in sorted(bindings.items(),
                                               key=lambda x: x[1][2]):
                            print("  %s: %s" % (key, val[2]))
'''















>>> import rospy

# baxter_interface - Baxter Python API
>>> import baxter_interface

# initialize our ROS node, registering it with the Master
>>> rospy.init_node('Hello_Baxter')

# create an instance of baxter_interface's Limb class
>>> limb = baxter_interface.Limb('right')

# get the right limb's current joint angles
>>> angles = limb.joint_angles()

# print the current joint angles
>>> print angles

# reassign new joint angles (all zeros) which we will later command to the limb
>>> angles['right_s0']=0.0
>>> angles['right_s1']=0.0
>>> angles['right_e0']=0.0
>>> angles['right_e1']=0.0
>>> angles['right_w0']=0.0
>>> angles['right_w1']=0.0
>>> angles['right_w2']=0.0

# print the joint angle command
>>> print angles

# move the right arm to those joint angles
>>> limb.move_to_joint_positions(angles)

# Baxter wants to say hello, let's wave the arm

# store the first wave position 
>>> wave_1 = {'right_s0': -0.459, 'right_s1': -0.202, 'right_e0': 1.807, 'right_e1': 1.714, 'right_w0': -0.906, 'right_w1': -1.545, 'right_w2': -0.276}

# store the second wave position
>>> wave_2 = {'right_s0': -0.395, 'right_s1': -0.202, 'right_e0': 1.831, 'right_e1': 1.981, 'right_w0': -1.979, 'right_w1': -1.100, 'right_w2': -0.448}

# wave three times
>>> for _move in range(3):
...     limb.move_to_joint_positions(wave_1)
...     limb.move_to_joint_positions(wave_2)
