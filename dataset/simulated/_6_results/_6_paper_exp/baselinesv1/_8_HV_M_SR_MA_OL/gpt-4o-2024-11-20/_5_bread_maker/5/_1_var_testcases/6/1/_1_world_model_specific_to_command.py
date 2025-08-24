# The code accurately models the features required to fulfill the user command. Below is the sequence of actions needed to execute the command along with related justifications from the user manual.

# **Sequence of Features:**
# 1. Select the program by setting variable_menu_index to "1" (Basic Program).
# - Feature from code: feature_list["set_menu"]
# - Relevant user manual text: "Choose a Programme with the MENU button."
#
# 2. Set the loaf size to 900g by modifying variable_loaf_size.
# - Feature from code: feature_list["set_loaf_size"]
# - Relevant user manual text: "Press LOAF SIZE button to select the Loaf Size (as needed)."
#
# 3. Set the crust color to Medium by modifying variable_crust_color.
# - Feature from code: feature_list["set_crust_color"]
# - Relevant user manual text: "Press COLOR button to select the Crust Colour (as needed)."
#
# 4. Configure the delay timer to 5 hours by setting variable_delay_timer.
# - Feature from code: feature_list["set_delay_timer"]
# - Relevant user manual text: "To set the Timer, determine when you would like your bread to be ready, then set the Timer."
#
# 5. Start the bread maker operation by toggling variable_start_running to "on".
# - Feature from code: feature_list["start_stop_program"]
# - Relevant user manual text: "Press START/STOP button to start the breadmaker."

# **Goal Variable Values for the Command:**
# - variable_menu_index: "1" (Basic Program)
# - variable_loaf_size: "900g"
# - variable_crust_color: "Medium"
# - variable_delay_timer: 300 (5 hours in minutes)
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass