# Python comments addressing the user command and required checks 

# The current command is to select the Basic program (Program 1), choose a loaf size of 700g, set the crust 
# color to Light, delay the timer for 3 hours, and finally power on the appliance to start baking. 
# We need to cross-check the user manual and the provided code to verify if the functionalities for the
# required steps are accurately modeled. Below are the checks for each step in the user command:
#
# 1. **Select Basic Program (Program 1):**
# - User manual reference: "Press MENU button repeatedly to cycle through the 12 Programmes."
# - The provided feature `feature_list["set_menu"]` models this accurately.
#
# 2. **Choose Loaf Size of 700g:**
# - User manual reference: "Press LOAF SIZE button to select the Loaf Size (700g or 900g)."
# - The provided feature `feature_list["set_loaf_size"]` models this step accurately.
#
# 3. **Set the Crust Color to Light:**
# - User manual reference: "Press COLOR button to select the Crust Colour (Light, Medium, or Dark). This function is only available for Programme Menu 1-7."
# - The provided feature `feature_list["set_crust_color"]` models this step accurately.
#
# 4. **Set the Delay Timer to 3 hours:**
# - User manual reference: "Press the TIME+ or TIME- buttons to adjust the delay timer in 10-minute increments up to a maximum of 12 hours (720 minutes)."
# - The provided feature `feature_list["set_delay_timer"]` models this functionality accurately.
#
# 5. **Power on and Start the Operation:**
# - User manual reference: "Press START/STOP button to start or stop the Programmes."
# - The provided feature `feature_list["start_stop_program"]` models this functionality accurately.
#
# Therefore, the provided code already models the relevant appliance features and their functionalities correctly.

# Sequence of Features for this Command:
# 1. Use the "set_menu" feature to select "Basic" (Program 1).
# 2. Use the "set_loaf_size" feature to choose "700g".
# 3. Use the "set_crust_color" feature to set the crust color to "Light".
# 4. Use the "set_delay_timer" feature to set a delay timer for 3 hours (180 minutes).
# 5. Use the "start_stop_program" feature to start the bread maker.

# Relevant user manual text:
# - For menu selection: "The appliance will automatically be set to the BASIC programme with the crust setting at MEDIUM. The display will show 3:00. Choose a Programme with the MENU button."
# - For loaf size: "Press LOAF SIZE button to select the Loaf Size (as needed)."
# - For crust color: "Press COLOR button to select the Crust Colour (as needed)."
# - For delay timer: "Use the TIME+ or TIME- buttons to adjust the delay timer."
# - For start/stop: "Press START/STOP button to start or stop the Programmes."

# Feature List Names in Provided Code:
# - `feature_list["set_menu"]` for menu selection.
# - `feature_list["set_loaf_size"]` for loaf size selection.
# - `feature_list["set_crust_color"]` for crust color selection.
# - `feature_list["set_delay_timer"]` for delay timer adjustment.
# - `feature_list["start_stop_program"]` for starting the program.

# Goal Variable Values for this Command:
# - `variable_menu_index` = "1" (Basic Program)
# - `variable_loaf_size` = "700g"
# - `variable_crust_color` = "Light"
# - `variable_delay_timer` = 180 (3 hours in minutes)
# - `variable_start_running` = "on"

class ExtendedSimulator(Simulator):
    pass