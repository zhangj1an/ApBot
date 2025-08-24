# The requested user command "Quick Bread for Breakfast" is accurately modeled in the given code.

# Sequence of features needed to achieve this command:
# 1. "select_cycle": Set cycle to 'Quick'.
# User manual: Press CYCLE button until desired program number appears on the digital display.
# Feature list: feature_list["select_cycle"]

# 2. "adjust_crust_color": Choose 'Medium' crust color.
# User manual: Press CRUST button to move the arrow to desired setting: Light, Medium, or Dark crust.
# Feature list: feature_list["adjust_crust_color"]

# 3. "adjust_loaf_size": Choose loaf size '1.5-lb'.
# User manual: Press the LOAF SIZE button to move the arrow to 1.5- or 2-lb. loaf size.
# Feature list: feature_list["adjust_loaf_size"]

# 4. "adjust_delay_timer": Set the delay timer to 2 hours (120 minutes).
# User manual: Use the Delay Timer feature to start the breadmaker at a later time.
# Press the + and – buttons to increase or decrease the delay time.
# Feature list: feature_list["adjust_delay_timer"]

# 5. "start_or_stop_operation": Start the breadmaker.
# User manual: Press START/STOP. The digital display will show the time remaining in the cycle.
# Feature list: feature_list["start_or_stop_operation"]

# Goal variable values to achieve this command:
goal_variable_values = {
    "variable_cycle": "Quick",
    "variable_crust_color": "Medium",
    "variable_loaf_size": "1.5lb",
    "variable_delay_timer": 120,
    "variable_start_running": "on"
}

class ExtendedSimulator(Simulator):
    pass