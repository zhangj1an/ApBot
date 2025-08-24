# The given code already models the power on/off functionality and also includes the fan speed adjustment functionality.
# The user manual states:
# - "Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate."
# - "Press the (fan speed) FAN SPEED button repeatedly until the desired speed is illuminated on the control panel. There are 4 fan speeds: Low, Medium, High and Turbo."

# The sequence of features to achieve the user command "Start the dehumidifier and switch to 'high' fan speed":
# 1. Use the "power_on_off" feature and set `variable_power_on_off` to "on".
# 2. Use the "adjust_fan_speed" feature and set `variable_fan_speed` to "high".

# Goal variable values:
# - `variable_power_on_off` to "on".
# - `variable_fan_speed` to "high".

class ExtendedSimulator(Simulator): 
    pass