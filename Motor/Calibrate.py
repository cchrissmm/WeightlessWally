#open the tool
odrivetool

#Hoverboard Motor Parameters
odrv0.axis1.motor.config.pole_pairs = 15
odrv0.axis1.motor.config.resistance_calib_max_voltage = 4
odrv0.axis1.motor.config.requested_current_range = 25 
odrv0.axis1.motor.config.current_control_bandwidth = 100
odrv0.axis1.motor.config.torque_constant = 8.27 / 16
odrv0.axis1.encoder.config.bandwidth = 100
odrv0.axis1.encoder.config.cpr = 90
odrv0.axis1.encoder.config.calib_scan_distance = 150
odrv0.axis1.encoder.config.mode = ENCODER_MODE_HALL
odrv0.axis1.controller.config.pos_gain = 1
odrv0.axis1.controller.config.vel_gain = 0.02 * odrv0.axis1.motor.config.torque_constant * odrv0.axis1.encoder.config.cpr
odrv0.axis1.controller.config.vel_integrator_gain = 0.1 * odrv0.axis1.motor.config.torque_constant * odrv0.axis1.encoder.config.cpr
odrv0.axis1.controller.config.vel_limit = 10
odrv0.axis1.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
odrv0.save_configuration()
odrv0.reboot()

#Motor Calibration
odrv0.axis1.requested_state = AXIS_STATE_MOTOR_CALIBRATION
odrv0.axis1.motor
odrv0.axis1.motor.config.pre_calibrated = True 

#Encoder Indexing
odrv0.axis1.requested_state = AXIS_STATE_ENCODER_INDEX_SEARCH
odrv0.save_configuration() 
odrv0.reboot()

#Encoder Offset
odrv0.axis1.requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION
odrv0.axis1.encoder.config.pre_calibrated = True 
odrv0.save_configuration() 
odrv0.reboot()

#to check for errors
dump_errors(odrv0)

#to check for calibration
odrv0.axis1.motor
odrv0.axis1.encoder

#to test run the motor
odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
odrv0.axis1.controller.input_vel = 1
odrv0.axis1.controller.input_vel = 0
odrv0.axis1.requested_state = AXIS_STATE_IDLE

#to see the position of the encoder
odrv0.axis1.encoder.shadow_count