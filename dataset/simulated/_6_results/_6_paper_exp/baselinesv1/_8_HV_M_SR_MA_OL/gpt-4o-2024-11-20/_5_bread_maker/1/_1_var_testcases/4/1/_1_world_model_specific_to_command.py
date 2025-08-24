# No new variables or features need to be added. The current implementation accurately models the features necessary
# to achieve the requested user command.

# Relevant user manual feature descriptions:
# 1. "Press the Menu button until your desired program is selected." (adjust_menu feature)
# 2. "Press the COLOR button to select the desired crust color." (adjust_crust_color feature)
# 3. "Press the LOAF button to select the desired size—1.5LB or 2.0LB." (adjust_loaf_size feature)
# 4. "Set the delay time by pressing the + or – buttons." (adjust_delay_time feature)
# 5. "Press the START/STOP button to start working, the working light will illuminate." (start_stop_bread_maker feature)

# Code features that align:
# - feature_list["adjust_menu"]: Adjusts the bread program (e.g., sets to "Sweet" for sweet bread).
# - feature_list["adjust_crust_color"]: Adjusts the crust color to "Medium."
# - feature_list["adjust_loaf_size"]: Sets the loaf size to "1.5LB."
# - feature_list["adjust_delay_time"]: Sets the delay timer to 6 hours.
# - feature_list["start_stop_bread_maker"]: Starts the bread maker.

# Sequence of features to achieve the command:
# 1. Use "adjust_menu" to set variable_menu_index to "Sweet."
# 2. Use "adjust_crust_color" to set variable_crust_color to "Medium."
# 3. Use "adjust_loaf_size" to set variable_loaf_size to "1.5LB."
# 4. Use "adjust_delay_time" to set variable_delay_time to 360 (6 hours in minutes).
# 5. Use "start_stop_bread_maker" to set variable_start_running to "on."

# Expected goal variable values:
# - variable_menu_index = "Sweet"
# - variable_crust_color = "Medium"
# - variable_loaf_size = "1.5LB"
# - variable_delay_time = 360 (6 hours)
# - variable_start_running = "on"

class ExtendedSimulator(Simulator):
    pass