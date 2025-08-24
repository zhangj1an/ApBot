# Analyze the user command against the given code and the user manual.

# The provided code models all the necessary variables and features required to achieve the user command. 
# The following sequence of features needs to be executed:
# 1. "set_menu": Select the Quick program.
# 2. "set_loaf_size": Choose a loaf size of 900g.
# 3. "set_crust_color": Set the crust color to Medium.
# 4. "set_delay_timer": Set the delay timer to 2 hours.
# 5. "start_stop_program": Power on and start operation.

# Relevant sections from the user manual:
# - **Menu Selector**: Select one of the 12 program menus (e.g., 1 for BASIC, 2 for FRENCH, 4 for QUICK, etc.).
# - **Loaf Size Selector**: Select different sizes of bread (700g or 900g).
# - **Colour Button**: Choose the desired crust color: Light, Medium, or Dark.
# - **Delay Timer Buttons**: Use these buttons to delay the completion of your bread by up to 12 hours (720 minutes).
# - **Start/Stop Button**: Press this button to start or stop the baking program.

# Feature and variable names in the given code:
# 1. Feature "set_menu" adjusts `variable_menu_index` to "4" for the quick program.
# 2. Feature "set_loaf_size" adjusts `variable_loaf_size` to "900g".
# 3. Feature "set_crust_color" adjusts `variable_crust_color` to "Medium".
# 4. Feature "set_delay_timer" adjusts `variable_delay_timer` to 120 (2 hours in minutes).
# 5. Feature "start_stop_program" toggles `variable_start_running` to "on".

# Goal variable values for the command:
# - `variable_menu_index = "4"`  (Quick program)
# - `variable_loaf_size = "900g"`
# - `variable_crust_color = "Medium"`
# - `variable_delay_timer = 120`
# - `variable_start_running = "on"`

class ExtendedSimulator(Simulator):
    pass