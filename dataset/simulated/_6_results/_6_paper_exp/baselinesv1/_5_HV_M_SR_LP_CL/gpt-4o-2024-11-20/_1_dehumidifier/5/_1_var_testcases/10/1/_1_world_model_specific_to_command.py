# Power on the dehumidifier and set the timer for 1 hour.

# Raw user manual text:
# - User manual: Turns the unit on and off.
# - User manual: Sets an Auto-On or Shut-Off timer, 1H, 2H or 4H.

# Features needed:
# 1. Power Control: Turn the unit on or off.
#    - Feature Name: "power_control"
# 2. Adjust Timer: Set the timer to the desired duration (1 hour in this case).
#    - Feature Name: "adjust_timer"

# Step-by-step actions:
# - Step 1: Use "power_control" to turn the dehumidifier on by pressing the power button.
# - Step 2: Use "adjust_timer" to set the timer to 1 hour by pressing the timer button.

# Goal variable values to achieve the command:
# - Set `variable_power_on_off` to "on".
# - Set `variable_timer` to "1".

class ExtendedSimulator(Simulator): 
    pass