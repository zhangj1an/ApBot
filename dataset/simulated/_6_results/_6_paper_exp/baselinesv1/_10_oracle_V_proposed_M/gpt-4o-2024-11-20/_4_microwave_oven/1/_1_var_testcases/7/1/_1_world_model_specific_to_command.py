# According to the user manual, the current code already accurately models the relevant features needed to achieve this task of defrosting using time defrost for 20 minutes with 20% power and then starting the appliance.

# Sequence of features needed to achieve this command:
# 1. Use the "set_time_defrost" feature to set the time defrost duration to 20 minutes and the power level to 20%.
#    - From user manual: **7. TIME DEFROST FUNCTION**
#      - "Press `TIME DEFROST`"
#      - "Press number pads to input defrosting time. The effective time range is 00:01 ~ 99:99."
#      - "The default microwave power is power level 3. If you want to change the power level, press `POWER` once, and the screen will display `PL 3`, then press the number pad of the power level you wanted."
#      - "Press `START/+30SEC.` to start defrosting. The remained cooking time will be displayed."
#    - Corresponding feature_list in the given code: `"set_time_defrost"`

# 2. Use the `set_time_defrost` feature to start the appliance by pressing the "start/+30sec button".

# Goal variable values to achieve this command:
# - `variable_time_defrost`: "00:20:00" (defrost time of 20 minutes)
# - `variable_power`: "PL2" (power set to 20%)
# - `variable_start_running`: "on" (appliance starts running)

class ExtendedSimulator(Simulator):
    pass