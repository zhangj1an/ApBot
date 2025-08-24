# Based on the given user command, here is the rationale:

# The user command is "Switch on the dehumidifier and configure the timer to shut down after 3 hours."
# 1. To "Switch on the dehumidifier," we use the feature "power_on_off," where the variable variable_power_on_off will be set to "on."
# 2. To "configure the timer to shut down after 3 hours," we use the feature "adjust_timer," where the variable variable_timer will be set to 3.

# The existing code accurately models both features as described in the user manual.
# - "power_on_off" feature correctly models turning the dehumidifier on via "press_power_button."
# - "adjust_timer" feature allows configuring the timer in adjustable hour increments (0–24), as described in the user manual: "slightly touch TIMER to adjust time, every one touch increases one hour."

# Sequence of features to achieve the command:
# - First, execute the "power_on_off" feature by pressing the "press_power_button" action to turn the dehumidifier on.
# - Next, execute the "adjust_timer" feature by incrementing the timer value using the "press_timer_button" action, setting it to 3 hours.

# Relevant manual excerpts:
# - "Press POWER, the Dehumidifier Starts Operation."
# - "Slightly touch TIMER to adjust time, every one touch increases one hour."

# Features from the given code:
# - feature_list["power_on_off"]
# - feature_list["adjust_timer"]

# Goal variable values to achieve this command:
# - variable_power_on_off: "on"
# - variable_timer: 3

class ExtendedSimulator(Simulator):
    pass