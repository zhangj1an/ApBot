# The given code has accurately modelled the requested feature, as follows:
# Sequence of features needed:
# 1. "time_defrost" to set defrost time and power level.
# 2. "microwave_cook" (if the simulator requires the start logic to explicitly reside here) 
#    OR directly set variable_start_running to "on".

# Relevant user manual text:
# **7. TIME DEFROST FUNCTION**
# 1. Press "TIME DEFROST", screen will display "dEF2".
# 2. Press number pads to input defrosting time. The effective time range is 00:01~99:99.
# 3. The default microwave power is power level 3. If you want to change the power level, press "POWER" once, and the screen will display "PL 3", then press the number pad of the power level you wanted.
# 4. Press "START/+30SEC." to start defrosting. The remaining cooking time will be displayed.

# Relevant feature list names in the given code:
# - "time_defrost"
# - "microwave_cook"

# Goal variable values to achieve the command:
# 1. Set variable_time_defrost to "00:20:00".
# 2. Set variable_power to "PL10" (100% power).
# 3. Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    pass