# The sequence of features needed to achieve the command:
# 1. "set_menu": Select the French program.
# 2. "set_loaf_size": Choose a loaf size of 900g.
# 3. "set_crust_color": Set the crust color to Light.
# 4. "set_delay_timer": Set the delay timer to 5 hours.
# 5. "start_stop_program": Power on and start the bread maker operation (toggle to "on").

# Relevant raw user manual text:
# - "Menu Selector: Select one of the 12 programme menus."
# - "Loaf Size Selector: Select different sizes of bread (700g or 900g)."
# - "Colour Button: For choosing the desired crust colour: Light, Medium or Dark."
# - "Delay Timer Buttons: Use these buttons when you would like to delay the completion of your bread. To set the Timer, determine when you would like your bread to be ready, then set the Timer."
# - "Start/Stop Button: To start or stop the Programmes."

# Relevant feature_list names in the given code:
# - "set_menu"
# - "set_loaf_size"
# - "set_crust_color"
# - "set_delay_timer"
# - "start_stop_program"

# Goal variable values to achieve the command:
# - variable_menu_index = "2" (French bread program)
# - variable_loaf_size = "900g"
# - variable_crust_color = "Light"
# - variable_delay_timer = 300 (5 hours in minutes)
# - variable_start_running = "on" (start bread maker)

class ExtendedSimulator(Simulator): 
	pass