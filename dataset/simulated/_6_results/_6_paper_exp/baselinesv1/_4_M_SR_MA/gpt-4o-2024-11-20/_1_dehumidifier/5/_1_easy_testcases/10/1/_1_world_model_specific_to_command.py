# User manual reference:
# Relevant text for turning the unit on/off: "Turns the unit on and off."
# Relevant text for setting the timer: "Sets an Auto-On or Shut-Off timer, 1H, 2H or 4H."

# The provided code already accurately models the features required to achieve the user command:
# 1. "power_control" feature from the feature_list is correctly designed to turn the unit on/off. The step in the feature_list defines the action "press_power_button" to toggle the variable "variable_power_on_off".
# 2. "adjust_timer" feature from the feature_list is correctly designed to set the timer (auto-on or auto-off) to the desired values of "1H", "2H", or "4H". The step allows "press_timer_button" to update the variable "variable_timer" to the appropriate value.

# Sequence of features needed to achieve this user command:
# - Feature: "power_control" -> Action: press_power_button -> Toggle power to "on".
# - Feature: "adjust_timer" -> Action: press_timer_button -> Set the timer to "1" (1H).

# Final goal variable values:
# - variable_power_on_off = "on".
# - variable_timer = "1".

class ExtendedSimulator(Simulator):
    pass