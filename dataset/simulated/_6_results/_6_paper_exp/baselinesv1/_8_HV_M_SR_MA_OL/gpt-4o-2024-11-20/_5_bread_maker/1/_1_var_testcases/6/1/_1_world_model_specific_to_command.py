# The user manual clearly outlines the necessary features and steps to achieve the given user command.
# The current code accurately models the relevant appliance features, variables, and actions.

# Sequence of features needed to achieve the command:
# 1. Adjust the menu to select "Sandwich".
#    User manual text: 
#    "- Use the Menu button to select a program. Each press cycles the LCD display through the 12 programs."
#    Feature list: feature_list["adjust_menu"]
#    Variable: variable_menu_index set to "Sandwich".
#
# 2. Set the loaf size to "1.5LB".
#    User manual text:
#    "- Press LOAF to select the desired loaf size: 1.5LB or 2.0LB."
#    Feature list: feature_list["adjust_loaf_size"]
#    Variable: variable_loaf_size set to "1.5LB".
#
# 3. Set the delay time to 6 hours (360 minutes).
#    User manual text:
#    "- Use the Delay function button to set the required time in 10-minute increments, to a maximum of 13 hours (780 minutes)."
#    Feature list: feature_list["adjust_delay_time"]
#    Variable: variable_delay_time set to 360.
#
# 4. Start the bread maker.
#    User manual text:
#    "- The START/STOP button is used to start or stop the selected baking program."
#    Feature list: feature_list["start_stop_bread_maker"]
#    Variable: variable_start_running set to "on".

# The goal variable values to achieve this user command:
# - variable_menu_index: "Sandwich"
# - variable_loaf_size: "1.5LB"
# - variable_delay_time: 360
# - variable_start_running: "on"

class ExtendedSimulator(Simulator):
    pass