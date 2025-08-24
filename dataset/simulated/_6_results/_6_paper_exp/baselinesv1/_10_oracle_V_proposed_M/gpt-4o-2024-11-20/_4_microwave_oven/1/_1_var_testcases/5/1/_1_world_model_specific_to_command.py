# Python comments indicate the sequence of features, quoting user manual text and feature names
# 1. The sequence of features needed to execute this user command is:
#    - "set_time_defrost" (set defrost time and power as described in user manual)
#    - "set_microwave_cook_time_power" (adjust microwave power to PL10, i.e., 100%)
#    - "set_microwave_cook_time_power" step automatically handles starting the appliance
#
# 2. Relevant user manual quotes:
#    **Time Defrost**:
#    1. Press "TIME DEFROST", screen will display "dEF2".
#    2. Press number pads to input defrosting time. The effective time range is 00:01~99:99
#    3. The default microwave power is power level 3. If you want to change the power level, press "POWER" once,
#       and the screen will display "PL 3", then press the number pad of the power level you wanted.
#    4. Press "START/+30SEC." to start defrosting. The remained cooking time will be displayed.
#
# 3. Relevant feature list names:
#    - "set_time_defrost"

class ExtendedSimulator(Simulator): 
    pass