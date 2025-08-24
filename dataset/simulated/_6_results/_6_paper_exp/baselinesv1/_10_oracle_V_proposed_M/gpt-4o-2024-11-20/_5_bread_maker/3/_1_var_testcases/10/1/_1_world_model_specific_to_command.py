# User manual explicitly correctly models the functionality needed for the user command.
# Sequence of features needed to achieve this command:
# 1. "select_cycle" - Set the cycle to 'French'.
# 2. "select_crust_color" - Choose 'Medium' crust color.
# 3. "select_loaf_size" - Choose loaf size '2-lb'.
# 4. "set_delay_timer" - Set the delay timer to 6 hours.
# 5. "start_stop_operation" - Start the breadmaker.
#
# User manual text describes the necessary features:
# - "Press CYCLE button until desired program number appears on the digital display." (variable_cycle, feature: "select_cycle")
# - "Press CRUST button to move the arrow to desired setting: Light, Medium, or Dark crust." (variable_crust_color, feature: "select_crust_color")
# - "Press the LOAF SIZE button to move the arrow to 1.5- or 2-lb. loaf size." (variable_loaf_size, feature: "select_loaf_size")
# - "Use the Delay Timer feature to start the breadmaker at a later time. Press the + and – buttons to increase the cycle time shown on the display." (variable_delay_timer, feature: "set_delay_timer")
# - "Press START/STOP. The digital display will show the time remaining in the cycle." (variable_start_running, feature: "start_stop_operation")
#
# Goal variable values to achieve the command:
# - variable_cycle: "French"
# - variable_crust_color: "Medium"
# - variable_loaf_size: "2.0lb"
# - variable_delay_timer: 360 (6 hours in minutes)
# - variable_start_running: "on"

class ExtendedSimulator(Simulator):
    pass