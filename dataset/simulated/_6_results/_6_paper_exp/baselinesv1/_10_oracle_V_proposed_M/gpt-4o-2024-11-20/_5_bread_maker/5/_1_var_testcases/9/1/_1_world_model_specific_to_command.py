# The given code correctly models the features and variables needed to achieve the user command: 
# Basic Bread with Light Crust. Select the Basic program. Choose a loaf size of 700g. Set the crust color to Light. 
# Set the delay timer to 9 hours. Power on and start the bread maker operation.

# Sequence of required features:
# 1. "set_program_menu" to select the Basic program (menu "1").
# 2. "adjust_loaf_size" to choose loaf size of 700g.
# 3. "adjust_crust_color" to set the crust color to Light.
# 4. "adjust_delay_timer" to set the delay timer to 9 hours (540 minutes).
# 5. "start_stop_appliance" to turn the start running to "on".

# Raw user manual text references:
# 1. For selecting the program: "Choose a Programme with the MENU button."
# 2. For selecting loaf size: "Press LOAF SIZE button to select the Loaf Size (as needed)."
# 3. For crust color: "Press COLOR button to select the Crust Colour (as needed)."
# 4. For delay timer: "Use these buttons when you would like to delay the completion of your bread."
# 5. For starting/stopping the appliance: "Press START/STOP button to start or stop the Programmes."

# Features in the given code:
# - "set_program_menu"
# - "adjust_loaf_size"
# - "adjust_crust_color"
# - "adjust_delay_timer"
# - "start_stop_appliance"

# Goal variable values:
# - Set variable_menu_index to "1".
# - Set variable_loaf_size to "700g".
# - Set variable_crust_color to "Light".
# - Set variable_delay_timer to 540.
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
	pass