# Python Comments:
# The current implementation models the required features accurately to achieve the user command:
# "Light French Bread. Select the French program. Choose a loaf size of 900g.
# Set the crust color to Light. Set the delay timer to 5 hours. Power on and
# start the bread maker operation."

# Sequence of features needed:
# 1. "set_program_menu" to set the menu to French program.
# 2. "adjust_loaf_size" to set the loaf size to 900g.
# 3. "adjust_crust_color" to set the crust color to Light.
# 4. "adjust_delay_timer" to set the delay timer to 300 minutes (5 hours).
# 5. "start_stop_appliance" ensures the appliance starts operation.

# Relevant user manual instructions:
# 1. "Choose a Programme with the MENU button."
#    - Feature: "set_program_menu"
# 2. "Press LOAF SIZE button to select the Loaf Size (as needed)."
#    - Feature: "adjust_loaf_size"
# 3. "Press COLOR button to select the Crust Colour (as needed)."
#    - Feature: "adjust_crust_color"
# 4. "Use these buttons [TIME +/- buttons] when you would like to delay the completion..."
#    - Feature: "adjust_delay_timer"
# 5. "Press START/STOP button to start the bread maker."
#    - Feature: "start_stop_appliance"

# Goal variable values:
# - Set `variable_menu_index` to "2" (French program).
# - Set `variable_loaf_size` to "900g".
# - Set `variable_crust_color` to "Light".
# - Set `variable_delay_timer` to 300 (in minutes).
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator):
    pass