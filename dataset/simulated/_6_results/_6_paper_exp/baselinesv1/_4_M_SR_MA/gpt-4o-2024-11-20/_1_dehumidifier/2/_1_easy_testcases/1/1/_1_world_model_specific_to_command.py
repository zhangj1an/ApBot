# The relevant user manual text and features:
# 1. Power On/Off:
# **User manual reads:** "Press the ⏻ button to turn on/off the unit."
# Feature: "power_on_off"
#
# 2. Adjust Fan Speed:
# **User manual reads:** "Press the 🔄 button to select the desired fan speed (High, Medium, Low, or Auto)."
# Feature: "set_fan_speed"
#
# Given the code already models the appliance such that:
# - "power_on_off" toggles variable_power_on_off to "on" or "off".
# - "set_fan_speed" adjusts fan speed using variable_fan_speed.
# The required sequence matches exactly the steps and variables encoded in the given Simulator.

# Sequence of features to achieve the command:
# - Feature: "power_on_off" to turn the appliance on.
# - Feature: "set_fan_speed" to set fan speed to HIGH.

# Goal variable values to achieve this command:
# - Set `variable_power_on_off` to "on".
# - Set `variable_fan_speed` to "HIGH".

class ExtendedSimulator(Simulator): 
    pass