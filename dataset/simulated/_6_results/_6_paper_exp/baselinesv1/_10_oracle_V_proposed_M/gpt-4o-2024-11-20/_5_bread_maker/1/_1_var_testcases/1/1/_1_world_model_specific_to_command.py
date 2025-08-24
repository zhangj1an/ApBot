# The current code's feature_list adequately models all necessary steps for the user command:
# - To make a basic loaf, select the "Basic" menu using the "set_menu" feature.
# - For a medium crust, adjust the crust color to "Medium" using the "set_crust_color" feature.
# - For a loaf size of 1.5LB, adjust the loaf size using the "set_loaf_size" feature.
# - Set the delay timer to 10 hours using the "adjust_delay_time" feature.
# - Finally, start the bread maker using the "start_or_stop_bread_maker" feature.

# Quote from raw user manual:
# - "The Menu button is used to select a program. Each time it is pressed, the program will vary." (modelled by feature_list["set_menu"])
# - "Use the Color button to select a LIGHT, MEDIUM or DARK color for the crust." (modelled by feature_list["set_crust_color"])
# - "Press this button to select the desired size of the loaf." (modelled by feature_list["set_loaf_size"])
# - "Use this button to delay the start time for your desired program." (modelled by feature_list["adjust_delay_time"])
# - "This button is used for starting and stopping the selected baking program." (modelled by feature_list["start_or_stop_bread_maker"])

# The relevant feature_list names in the code are:
# - set_menu
# - set_crust_color
# - set_loaf_size
# - adjust_delay_time
# - start_or_stop_bread_maker

# Sequence of feature steps to implement the command:
# 1. Use "press_menu_button" to select "Basic" in the "set_menu" feature.
# 2. Use "press_color_button" to set the crust color to "Medium" in the "set_crust_color" feature.
# 3. Use "press_loaf_button" to set the loaf size to "1.5LB" in the "set_loaf_size" feature.
# 4. Use "press_plus_button" or "press_minus_button" to set the delay timer to 10 hours in the "adjust_delay_time" feature.
# 5. Use "press_start_stop_button" to start the bread maker in the "start_or_stop_bread_maker" feature.

# Goal variable values to achieve this command:
# - variable_menu_index = "Basic"
# - variable_crust_color = "Medium"
# - variable_loaf_size = "1.5LB"
# - variable_delay_time = 600 (10 hours in minutes)
# - variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass