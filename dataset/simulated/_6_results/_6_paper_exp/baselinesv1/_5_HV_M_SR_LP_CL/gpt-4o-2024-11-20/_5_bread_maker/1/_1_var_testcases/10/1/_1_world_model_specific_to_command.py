# The given code correctly models the relevant appliance features based on the user command:
# - Selecting "French" menu corresponds to feature_list["adjust_menu"].
# - Setting crust to "Light" corresponds to feature_list["adjust_crust_color"].
# - Setting the loaf size to "1.5LB" corresponds to feature_list["adjust_loaf_size"].
# - Setting a timer of 11 hours corresponds to feature_list["adjust_delay_time"].
# - Starting the bread maker corresponds to feature_list["start_stop_bread_maker"].

# The user manual text that describes these features matches the implemented features:
# 1. **MENU**: "The Menu button is used to select a program."
# 2. **COLOR**: "Use the Color button to select a LIGHT, MEDIUM or DARK color for the crust."
# 3. **LOAF SIZE**: "Press this button to select the desired size of the loaf."
# 4. **DELAY FUNCTION**: "Use this button to delay the start time for your desired program... press the '+' and '-' buttons to set the required time."
# 5. **START/STOP**: "To start a program, press the START/STOP button once."
#
# Relevant features from the feature_list are:
# - "adjust_menu"
# - "adjust_crust_color"
# - "adjust_loaf_size"
# - "adjust_delay_time"
# - "start_stop_bread_maker"

# Goal Variable Values:
# - variable_menu_index: "French"
# - variable_crust_color: "Light"
# - variable_loaf_size: "1.5LB"
# - variable_delay_time: 660 (11 hours in minutes)
# - variable_start_running: "on"

class ExtendedSimulator(Simulator):
    pass