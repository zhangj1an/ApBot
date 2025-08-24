# The given code correctly models the required appliance features and variables based on the user command.
# The features to achieve the command "Warm, Whole Wheat Bread. Select the Whole Wheat program. Choose a loaf size of 900g. Set the crust color to Dark. Set the delay timer to 6 hours. Power on and start the bread maker operation." are:
# 1. "set_program_menu" (to select Whole Wheat program - Menu 3),
# 2. "adjust_loaf_size" (to set loaf size to 900g),
# 3. "adjust_crust_color" (to set crust color as Dark),
# 4. "adjust_delay_timer" (to set delay timer to 6 hours),
# 5. "start_stop_appliance" (to power on and start the operation).

# Relevant user manual texts:
# • Setting Program Menu: **Menu Selector** lets the user select one of the 12 program menus (1 to 12).
# • Choosing Loaf Size: **Loaf Size Selector** for selecting bread size (700g or 900g).
# • Choosing Crust Color: **COLOR button** allows selecting desired crust color (Light, Medium, Dark).
# • Setting Delay Timer: **Delay Timer Buttons** allow delaying start time. Timer can be set in 10-min steps up to 12 hours (720 mins).
# • Starting/Stopping the operation: **START/STOP button** toggles the operation between running and stopping.

# Goal Variable Values to Achieve the Command:
# - variable_menu_index = "3" (Whole Wheat program)
# - variable_loaf_size = "900g"
# - variable_crust_color = "Dark"
# - variable_delay_timer = 360 (6 hours)
# - variable_start_running = "on"

class ExtendedSimulator(Simulator):
    pass