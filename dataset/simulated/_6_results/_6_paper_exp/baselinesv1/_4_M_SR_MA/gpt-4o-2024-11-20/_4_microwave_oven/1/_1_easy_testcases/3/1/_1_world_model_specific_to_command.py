# Python comments:
# The current code accurately models the steps required to achieve the user command.

# Sequence of features needed to achieve this command:
# 1. "microwave_cook"
# 2. "add_30_seconds" (implicitly implemented as start button doubles as adding 30 seconds in execution)

# Raw user manual text:
# **4. MICROWAVE COOK**
# 1. Press "TIME COOK" once, screen will display "00:00".
# 2. Press number keys to input the cooking time; the maximum cooking time is 99 minutes and 99 seconds.
# 3. Press "POWER" once, screen will display "PL10". The default power is 100% power. Now you can press number keys to adjust the power level.
# 4. Press "START/+30SEC." to start cooking.
#
# The feature "microwave_cook" from the given `feature_list` matches the user manual description.

# Goal variable values:
# - Set "variable_time_cook_time" to "00:05:00".
# - Set "variable_power" to "PL7".
# - Set "variable_start_running" to "on".

class ExtendedSimulator(Simulator): 
    pass