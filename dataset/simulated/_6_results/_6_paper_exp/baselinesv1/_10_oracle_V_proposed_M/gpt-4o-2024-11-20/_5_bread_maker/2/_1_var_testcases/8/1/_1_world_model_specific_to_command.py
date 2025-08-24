# Python comment listing steps and verification:

# Sequence of features needed to achieve the command:
# 1. "set_menu" - Set the breadmaker menu to "11 Sandwich".
# 2. "adjust_loaf_size" - Set the loaf size to "1.5lb" (small).
# 3. "adjust_crust_color" - Set the crust color to "dark".
# 4. "adjust_timer" - Set the timer delay to 120 minutes (2 hours delay).
# 5. "start_stop" - Start the breadmaker.

# Relevant user manual text:
# - To select a menu, the user manual mentions: 
#   **Menu button:** For choosing the bread making program from the list 1 to 12.
# - To select loaf size, the manual states:
#   **Loaf size button:** For selecting small (1.5lb) or large (2lb) loaf size (certain programs only).
# - To select crust color, the manual specifies:
#   **Color button:** For selecting crust color from light, medium, or dark.
# - To set a timer delay, the manual describes:
#   **Timer delay buttons:** Use to delay the start of bread making (all programs except Fastbake).
# - To start the machine, the manual states:
#   **Start:** Press to start for approx 1 second, a beep sounds, and the colon (:) flashes and the program starts.

# Feature list verified against the user manual:
# Feature names in the given code: 
# 1. "set_menu" - Matches menu selection requirements.
# 2. "adjust_loaf_size" - Matches loaf size adjustment requirements.
# 3. "adjust_crust_color" - Matches crust color adjustment requirements.
# 4. "adjust_timer" - Matches timer delay adjustment requirements.
# 5. "start_stop" - Matches starting/stopping operation requirements.

# Since the given code correctly models the relevant appliance variables and features as described in the user manual, 
# we can directly achieve the user command by adjusting the variables.

# Goal variable values to achieve the command:
# 1. Set `variable_menu_index` to "11 Sandwich".
# 2. Set `variable_loaf_size` to "1.5lb".
# 3. Set `variable_crust_color` to "dark".
# 4. Set `variable_timer_delay` to 120 minutes.
# 5. Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
    pass