# User manual text confirms the procedure: 
# Time Defrost Function:
# 1. Press "TIME DEFROST", screen will display "dEF2".
# 2. Press number pads to input defrosting time. The effective time range is 00:01~99:99.
# 3. The default microwave power is power level 3. If you want to change the power level, press "POWER" once, and the screen will display "PL 3", then press the number pad of the power level you wanted.
# 4. Press "START/+30SEC." to start defrosting. The remained cooking time will be displayed.
# 
# Feature in existing code: "time_defrost"
# The sequence of features needed are:
# - "time_defrost" to input defrost time and change power level as required
# - Start the microwave using "microwave_cook" feature for cooking.

# Goal Values for the User Command:
# - Set `variable_time_defrost` to "00:10:00" (10 minutes).
# - Set `variable_power` to "PL6" (60% power).
# - Set `variable_start_running` to "on" (start the microwave).

class ExtendedSimulator(Simulator): 
    pass