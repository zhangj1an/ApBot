# The current code has correctly modeled the features required to achieve the user command. Below is the sequence of features used and the corresponding raw user manual text:

# Sequence of Features:
# 1. Use the "select_cycle" feature to set the cycle to "Whole Grain".
#    - User Manual Text: "Press CYCLE button to select your desired cycle. The corresponding cycle number is shown on the display."
#    - Feature list: "select_cycle"

# 2. Use the "adjust_crust_color" feature to choose "Dark" crust color.
#    - User Manual Text: "Press CRUST button to move the arrow to desired setting: Light, Medium, or Dark crust."
#    - Feature list: "adjust_crust_color"

# 3. Use the "adjust_loaf_size" feature to choose loaf size "2-lb".
#    - User Manual Text: "Press the LOAF SIZE button to move the arrow to 1.5- or 2-lb. loaf size."
#    - Feature list: "adjust_loaf_size"

# 4. Use the "adjust_delay_timer" feature to set the delay timer to 4 hours (240 minutes).
#    - User Manual Text: "Use the Delay Timer feature to start the breadmaker at a later time. Press the + and – buttons to increase the cycle time shown on the display. Add up to 13 hours including the delay time and breadmaking cycle."
#    - Feature list: "adjust_delay_timer"

# 5. Use the "start_or_stop_operation" feature to start the bread maker.
#    - User Manual Text: "Press START/STOP. The digital display will show the time remaining in the cycle."
#    - Feature list: "start_or_stop_operation"

# Goal Variable Values to Achieve the Command:
# - Set variable_cycle to "Whole Grain".
# - Set variable_crust_color to "Dark".
# - Set variable_loaf_size to "2.0lb".
# - Set variable_delay_timer to 240 (4 hours in minutes).
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    pass