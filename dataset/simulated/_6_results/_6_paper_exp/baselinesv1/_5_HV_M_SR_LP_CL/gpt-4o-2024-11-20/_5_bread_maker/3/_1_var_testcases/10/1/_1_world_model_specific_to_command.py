# The following command requires:
# - Selecting the "French" cycle
# - Choosing "Medium" crust color
# - Choosing loaf size "2-lb"
# - Setting a delay timer to 6 hours
# - Starting the breadmaker

# Sequence of features needed to achieve this command based on the provided user manual and features:
# 1. Feature: "select_cycle" -> Action: "press_cycle_button" -> Variable: "variable_cycle"
# 2. Feature: "adjust_crust_color" -> Action: "press_crust_button" -> Variable: "variable_crust_color"
# 3. Feature: "adjust_loaf_size" -> Action: "press_loaf_size_button" -> Variable: "variable_loaf_size"
# 4. Feature: "adjust_delay_timer" -> Actions: "press_delay_timer_plus_button", "press_delay_timer_minus_button" -> Variable: "variable_delay_timer"
# 5. Feature: "start_or_stop_operation" -> Action: "press_start_stop_button" -> Variable: "variable_start_running"

# Relevant user manual text:
# - "Press CYCLE button to select your desired cycle. The corresponding cycle number is shown on the display." [Used in feature "select_cycle"]
# - "Press CRUST button to move the arrow to desired setting: Light, Medium, or Dark crust." [Used in feature "adjust_crust_color"]
# - "Press the LOAF SIZE button to move the arrow to 1.5- or 2-lb. loaf size." [Used in feature "adjust_loaf_size"]
# - "Use the Delay Timer feature to start the breadmaker at a later time. Press the + and – buttons to increase the cycle time shown on the display." [Used in feature "adjust_delay_timer"]
# - "Press START/STOP. The digital display will show the time remaining in the cycle." [Used in feature "start_or_stop_operation"]

# Given feature names in code: 
# `select_cycle`, `adjust_crust_color`, `adjust_loaf_size`, `adjust_delay_timer`, `start_or_stop_operation`

# Goal variable values:
# variable_cycle = "French"
# variable_crust_color = "Medium"
# variable_loaf_size = "2.0lb"
# variable_delay_timer = 360 (6 hours in minutes)
# variable_start_running = "on"

class ExtendedSimulator(Simulator):
    pass