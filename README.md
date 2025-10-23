# system identification data
Data repo for sharing raw system ident data for Liam Nolans master's thesis

roll_step_response_roll_0_pitch_0.csv  This is the roll dof data using open loop control


prbs_roll_0_pitch_0.csv  This is the pitch dof identifcation data using a light closed loop controller and prbs  


This is the raw system identification data for the roll and pitch at the 0,0 position. In the csv files 'position' header is the actual angular position of each joint in degrees and the 'velocity' header is the control input for each DOF as the raw PWM signal sent from the teensy. Those are just the ROS2 naming conventions and are a bit confusing
