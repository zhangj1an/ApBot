# The description of the user manual for "time defrost" and "start appliance" is correctly modelled in the provided code. 
# Here's the sequence of features and the corresponding user manual text:
#
# 1. **Feature: "time_defrost"**
# - This feature allows the user to defrost food using a specific time and power level.
# - User manual text: **7. TIME DEFROST FUNCTION**
#   1. Press "TIME DEFROST," screen will display "dEF2."
#   2. Press number pads to input defrosting time. The effective time range is 00:01~99:99.
#   3. The default microwave power is power level 3. If you want to change the power level, press "POWER" once, and the screen will display "PL3," then press the number pad of the power level you wanted.
#   4. Press "START/+30SEC." to start defrosting. The remaining cooking time will be displayed.
# - This corresponds perfectly with the feature `"time_defrost"` in the code.
#
# 2. **Feature: "microwave_cook"** (for the adjustment of power level during time defrost)
# - Adjust the power using the power button and number pads.
# - User manual text: **4. MICROWAVE COOK**
#   3. Press "POWER" once, screen will display "PL10". The default power is 100% power. Now you can press number keys to adjust the power level.
#   This is valid here because the manual specifies that power can be adjusted during defrosting as well.
# - This corresponds perfectly with step 3 and 4 in `"time_defrost"`.
#
# The simulator also correctly models the action to start the appliance: pressing the "START/+30SEC." button sets `variable_start_running` to "on."
#
# Sequence of features needed to achieve this command:
# - "time_defrost": Set the time to 20 minutes and adjust the power to 20% (PL2).
# - The final step of "time_defrost" automatically starts the appliance.

# Goal variable values to achieve the user command:
# - `variable_time_defrost`: "00:20:00"
# - `variable_power`: "PL2"
# - `variable_start_running`: "on"

class ExtendedSimulator(Simulator): 
    pass