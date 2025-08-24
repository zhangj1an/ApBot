# The code correctly models the relevant appliance features that can be used to achieve the command:
# "Use time cooking setting to cook at 90% power for 8 minutes. Then start the appliance."
# The sequence of features needed to achieve the user command is as follows:
# 1. "set_microwave_cook_time_power"
# The raw user manual text that describes the relevant features:
# **Microwave Cooking Feature:**
# 1. Press "TIME COOK" once, screen will display "00:00".
# 2. Press number keys to input the cooking time; the maximum cooking time is 99 minutes and 99 seconds.
# 3. Press "POWER" once, screen will display "PL10". The default power is 100% power. Now you can press number keys to adjust the power level.
# 4. Press "START/+30SEC." to start cooking.
#
# The feature_list name in the given code: "set_microwave_cook_time_power"
# Goal variable values to achieve the command:
# 1. Set `variable_time_cook_time` to "00:08:00".
# 2. Set `variable_power` to "PL9".
# 3. Set `variable_start_running` to "on" (automatically set after pressing "START/+30SEC.").

class ExtendedSimulator(Simulator):
    pass