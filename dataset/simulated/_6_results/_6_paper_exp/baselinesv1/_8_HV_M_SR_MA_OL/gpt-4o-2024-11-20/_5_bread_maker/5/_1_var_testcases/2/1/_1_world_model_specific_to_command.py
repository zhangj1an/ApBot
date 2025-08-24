# Checking against the user manual:

# The current code correctly captures the relevant features and variables described in the user manual for this appliance.
# Features such as program menu selection, loaf size, crust color, delay timer, and start/stop functionality are well modeled.
# Every feature described in the user manual is accurately implemented in the feature list and matches the required steps for execution.

# Sequence of features to achieve the user command:
# 1. "set_menu" to set the Whole Wheat program ("3").
#    Raw user manual: "Press the MENU button repeatedly to select the program you want (e.g. Whole Wheat for Whole Wheat bread)."
#    Feature list: feature_list["set_menu"].
# 2. "set_loaf_size" to select 900g loaf size.
#    Raw user manual: "Press the LOAF SIZE button to select 700g or 900g."
#    Feature list: feature_list["set_loaf_size"].
# 3. "set_crust_color" to select the Dark crust.
#    Raw user manual: "Press the COLOR button to choose your desired crust color (Light, Medium, or Dark)."
#    Feature list: feature_list["set_crust_color"].
# 4. "set_delay_timer" to set the delay timer to 6 hours.
#    Raw user manual: "Use the TIME + or TIME - buttons to set a delay up to 12 hours. Each button press adjusts time in 10-minute increments."
#    Feature list: feature_list["set_delay_timer"].
# 5. "start_stop_program" to power on and start the bread maker operation.
#    Raw user manual: "Press the START/STOP button to start the bread maker. This button also stops the program when held down."
#    Feature list: feature_list["start_stop_program"].

# Goal variable values to achieve this command:
# - variable_menu_index: "3".
# - variable_loaf_size: "900g".
# - variable_crust_color: "Dark".
# - variable_delay_timer: 360 (6 hours in minutes).
# - variable_start_running: "on".

class ExtendedSimulator(Simulator):
    pass