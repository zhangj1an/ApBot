# The current Simulator correctly models the required appliance features based on the user manual,
# and the sequence of actions needed to complete the command can be executed sequentially.
# Below are the relevant features, their descriptions, and the corresponding step-by-step sequence:

# Sequence of features needed to achieve the command:
# 1. Feature "select_cycle" to set the cycle to "Sweet".
# 2. Feature "select_crust_color" to set the crust color to "Light".
# 3. Feature "select_loaf_size" to set the loaf size to "2-lb".
# 4. Feature "set_delay_timer" to set the delay timer to 2 hours.
# 5. Feature "start_stop_operation" to start the bread maker.

# Raw user manual text relevant to these features:
# - For selecting the cycle: "Press CYCLE button to select your desired cycle."
# - For selecting crust color: "Press CRUST button to move the arrow to desired setting: Light, Medium, or Dark crust."
# - For selecting loaf size: "Press the LOAF SIZE button to move the arrow to 1.5- or 2-lb. loaf size."
# - For delay timer: "Use the Delay Timer feature to start the breadmaker at a later time. Press the + and – buttons to increase the cycle time shown on the display. Add up to 13 hours including the delay time and breadmaking cycle."
# - For starting the operation: "Press START/STOP. The digital display will show the time remaining in the cycle."

# Feature list names in the given code:
# - "select_cycle"
# - "select_crust_color"
# - "select_loaf_size"
# - "set_delay_timer"
# - "start_stop_operation"

# Goal variable values needed to achieve the user command:
# - Set variable_cycle to "Sweet".
# - Set variable_crust_color to "Light".
# - Set variable_loaf_size to "2-lb".
# - Set variable_delay_timer to 120 (minutes).
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator):
    pass