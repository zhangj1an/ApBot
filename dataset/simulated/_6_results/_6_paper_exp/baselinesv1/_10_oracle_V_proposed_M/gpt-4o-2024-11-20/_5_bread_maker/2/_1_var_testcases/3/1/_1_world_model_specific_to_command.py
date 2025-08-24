# The provided code accurately models the relevant appliance features for the given user command. 
# Below is the step-by-step sequence of features to achieve the command, 
# along with the goal variable values for each step and the relevant user manual text:

# 1. **Set menu to sweet**
# - Feature: "set_menu"
# - Goal: Set `variable_menu_index` to "5 Sweet"
# Raw User Manual Text:
#  "For choosing the bread making program from the list 1 to 12."

# 2. **Adjust loaf size to small (1.5lb)**
# - Feature: "adjust_loaf_size"
# - Goal: Set `variable_loaf_size` to "1.5lb"
# Raw User Manual Text:
#  "For selecting small (1.5lb) or large (2lb) loaf size (certain programs only)."

# 3. **Adjust crust color to light**
# - Feature: "adjust_crust_color"
# - Goal: Set `variable_crust_color` to "light"
# Raw User Manual Text:
#  "For selecting crust colour from light, medium or dark (certain programs only)."

# 4. **Set time delay to 4 hours**
# - Feature: "adjust_timer"
# - Goal: Set `variable_timer_delay` to 240 (in minutes) 
# Raw User Manual Text:
#  "Use the timer when you want the bread ready later, or in the morning. A maximum of 13 hours can be set."

# 5. **Start the breadmaker**
# - Feature: "start_stop"
# - Goal: Set `variable_start_running` to "on"
# Raw User Manual Text:
#  "Press to start for approx 1 second, a beep sounds and the colon (:) flashes and the program starts."
#
# The goal variable values to achieve the user command are:
# variable_menu_index = "5 Sweet"
# variable_loaf_size = "1.5lb"
# variable_crust_color = "light"
# variable_timer_delay = 240
# variable_start_running = "on"

class ExtendedSimulator(Simulator):
    pass