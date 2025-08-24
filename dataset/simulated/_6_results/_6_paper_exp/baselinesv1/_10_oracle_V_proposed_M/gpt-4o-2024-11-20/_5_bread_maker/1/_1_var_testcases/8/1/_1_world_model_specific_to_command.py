# The given code models the appliance features accurately based on the user manual. 
# The sequence of features required to achieve the command is as follows:
# 1. Set the menu to "Sweet" using the "set_menu" feature.
#    User manual text: "The Menu button is used to select a program. ... Select your desired program."
#    Feature: feature_list["set_menu"]
#    Relevant variable: variable_menu_index
# 2. Set the crust color to "Light" using the "set_crust_color" feature.
#    User manual text: "Use the Color button to select a LIGHT, MEDIUM or DARK color for the crust."
#    Feature: feature_list["set_crust_color"]
#    Relevant variable: variable_crust_color
# 3. Set the loaf size to "2.0LB" using the "set_loaf_size" feature.
#    User manual text: "Press this button to select the desired size of the loaf."
#    Feature: feature_list["set_loaf_size"]
#    Relevant variable: variable_loaf_size
# 4. Adjust the delay timer to 3 hours (180 minutes) using the "adjust_delay_time" feature.
#    User manual text: "Use this button to delay the start time for your desired program."
#    Feature: feature_list["adjust_delay_time"]
#    Relevant variable: variable_delay_time
# 5. Start the bread maker using the "start_or_stop_bread_maker" feature.
#    User manual text: "Press the START/STOP button to start working, the working light will illuminate."
#    Feature: feature_list["start_or_stop_bread_maker"]
#    Relevant variable: variable_start_running

# The goal variable values to achieve this command are:
# variable_menu_index = "Sweet"
# variable_crust_color = "Light"
# variable_loaf_size = "2.0LB"
# variable_delay_time = 180 (minutes)
# variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass