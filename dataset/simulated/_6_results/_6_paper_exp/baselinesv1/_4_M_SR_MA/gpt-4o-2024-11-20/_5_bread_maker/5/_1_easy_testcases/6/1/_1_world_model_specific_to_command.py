# User command: Basic White Bread. Select the Basic program. Choose a loaf size of 900g. Set the crust color to Medium.
# Set the delay timer to 5 hours. Power on and start the bread maker operation.

# The currently provided code has modeled all relevant features and appliance variables:
# 1. "set_menu" feature and variable_menu_index are correctly modeled for selecting the Basic program.
# 2. "set_loaf_size" feature and variable_loaf_size are correctly modeled for choosing the loaf size.
# 3. "set_crust_color" feature and variable_crust_color are correctly modeled for setting the crust color.
# 4. "set_delay_timer" feature and variable_delay_timer are correctly modeled for setting the delay timer.
# 5. "start_stop_program" feature and variable_start_running are correctly modeled for toggling between on and off.

# Sequence of features needed to achieve this command:
# 1. Select the Basic program using the "set_menu" feature: Set variable_menu_index to "1".
#    Raw user manual text: "Choose a Programme with the MENU button."
#    Feature: feature_list["set_menu"]
# 
# 2. Choose a loaf size of 900g using the "set_loaf_size" feature: Set variable_loaf_size to "900g".
#    Raw user manual text: "Press LOAF SIZE button to select the Loaf Size (as needed)."
#    Feature: feature_list["set_loaf_size"]
#
# 3. Set the crust color to Medium using the "set_crust_color" feature: Set variable_crust_color to "Medium".
#    Raw user manual text: "Press COLOR button to select the Crust Colour (as needed)."
#    Feature: feature_list["set_crust_color"]
#
# 4. Set the delay timer to 5 hours using the "set_delay_timer" feature: Set variable_delay_timer to "300" (5 hours in minutes).
#    Raw user manual text: "The time delay function allows you to delay the start time of baking by up to 12 hours."
#    Feature: feature_list["set_delay_timer"]
#
# 5. Start the bread maker operation using the "start_stop_program" feature: Set variable_start_running to "on".
#    Raw user manual text: "Press START/STOP button to start or stop the Programmes."
#    Feature: feature_list["start_stop_program"]

# Goal variable values:
# 1. Set variable_menu_index to "1".
# 2. Set variable_loaf_size to "900g".
# 3. Set variable_crust_color to "Medium".
# 4. Set variable_delay_timer to 300 (5 hours in minutes).
# 5. Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    pass