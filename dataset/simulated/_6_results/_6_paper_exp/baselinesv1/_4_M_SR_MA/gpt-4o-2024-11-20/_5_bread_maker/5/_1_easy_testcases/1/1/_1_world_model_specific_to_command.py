# User manual check against the given code
# 1. The given code models all the variables described in the user manual: menu selection, loaf size, crust color, delay timer, and start/stop functionality.
# 2. The given code models features for each task in the appliance: set_menu, set_loaf_size, set_crust_color, set_delay_timer, and start_stop_program.
# 3. The given code has sufficient actions (`press_menu_button`, `press_loaf_size_button`, `press_color_button`, `press_time_plus_button`, `press_time_minus_button`, `press_start_stop_button`).
# 4. The features align well with the user manual steps, enabling the command to be executed.

# Command breakdown:
# - Select the Quick program (menu 4).
# - Choose a loaf size of 700g.
# - Set the crust color to Light.
# - Set the delay timer for 11 hours (660 minutes).
# - Start the bread maker operation.

# Corresponding feature sequence:
# 1. Start with "set_menu" — select program 4 (Quick).
# 2. Move to "set_loaf_size" — select 700g.
# 3. Proceed to "set_crust_color" — select Light.
# 4. Use "set_delay_timer" to set 11 hours (660 minutes).
# 5. Finalize with "start_stop_program" — set start_running to on.

class ExtendedSimulator(Simulator): 
    pass