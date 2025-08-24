# The current code sufficiently models the relevant appliance features described in the user manual for the user command:
# "Defrost using time defrost for 20 minutes with 20% power, then start the appliance."
# Here's the sequence of features and required states to achieve this command:

# Sequence of features:
# 1. Feature "time_defrost" (feature_list["time_defrost"]): 
#    - Actions in sequence: ["press_time_defrost_button", meta_actions_on_number, "press_power_button", meta_actions_on_number, "press_start_plus_30sec_button"]
#    - Goal variables: Set variable_time_defrost to "00:20:00", set variable_power to "PL2".
#
# 2. Feature "speedy_cooking" (feature_list["speedy_cooking"]): 
#    - Action: ["press_start_plus_30sec_button"]
#    - Goal variable: Set variable_start_running to "on".

# Relevant user manual text:
# - Time Defrost Function: 
#   1. Press "TIME DEFROST", screen will display "dEF2".
#   2. Press number pads to input defrosting time. The effective time range is 00:01~99:99.
#   3. The default microwave power is power level 3. If you want to change the power level, press "POWER" once, and the screen will display "PL 3", then press the number pad of the power level you wanted.
#   4. Press "START/+30SEC." to start defrosting. The remaining cooking time will be displayed.

# Goal variable values to achieve the command:
# - variable_time_defrost: "00:20:00"
# - variable_power: "PL2"
# - variable_start_running: "on"

class ExtendedSimulator(Simulator):
    pass