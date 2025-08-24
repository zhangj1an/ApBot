# The given code correctly models the relevant appliance features to achieve the command. 
# Features needed to achieve the command are: 
# 1. "select_cycle": to set the cycle to "Quick".
# User manual: "Press CYCLE button to select your desired cycle. The corresponding cycle number is shown on the display."
# Feature in code: feature_list["select_cycle"]
#
# 2. "adjust_crust_color": to select the crust color to "Medium".
# User manual: "Press CRUST button to move the arrow to desired setting: Light, Medium, or Dark crust."
# Feature in code: feature_list["adjust_crust_color"]
#
# 3. "adjust_loaf_size": to set the loaf size to "1.5-lb".
# User manual: "Press the LOAF SIZE button to move the arrow to 1.5- or 2-lb. loaf size."
# Feature in code: feature_list["adjust_loaf_size"]
#
# 4. "adjust_delay_timer": to set the delay timer to 2 hours (120 minutes).
# User manual: "Use the Delay Timer feature to start the breadmaker at a later time. Press the + and – buttons to increase the cycle time shown on the display."
# Feature in code: feature_list["adjust_delay_timer"]
#
# 5. "start_or_stop_operation": to start the bread maker.
# User manual: "Press START/STOP. The digital display will show the time remaining in the cycle."
# Feature in code: feature_list["start_or_stop_operation"]

# Goal variable values to achieve the requested user command:
# - Set variable_cycle to "Quick"
# - Set variable_crust_color to "Medium"
# - Set variable_loaf_size to "1.5lb"
# - Set variable_delay_timer to 120
# - Set variable_start_running to "on"

class ExtendedSimulator(Simulator): 
    pass