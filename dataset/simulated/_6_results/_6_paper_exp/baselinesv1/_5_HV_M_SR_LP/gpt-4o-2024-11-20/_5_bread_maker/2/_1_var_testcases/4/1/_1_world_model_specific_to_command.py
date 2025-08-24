# The sequence of features needed to achieve the command is as follows:
# 1. Set the menu to "Basic White" using the feature "set_menu_and_setting".
# 2. Adjust the crust color to "medium" using the feature "adjust_crust_color".
# 3. Adjust the loaf size to "2LB" using the feature "adjust_loaf_size".
# 4. Set the timer delay to 5 hours (05:00:00) using the feature "adjust_timer_delay".
# 5. Start the bread maker using the feature "start_stop_operation".

# Relevant user manual text:
# - “For choosing the bread making program from the list 1 to 12” (set menu).
# - “For selecting crust colour from light, medium or dark (certain programs only)” (crust color).
# - "For selecting small (1.5lb) or large (2lb) loaf size (certain programs only)” (loaf size).
# - "Use the timer when you want the bread ready later, or in the morning. A maximum of 13 hours can be set." (timer delay).
# - "Press to start for approx 1 second, a beep sounds and the colon (:) flashes and the program starts" (start operation).

# Feature list names:
# - feature_list["set_menu_and_setting"]
# - feature_list["adjust_crust_color"]
# - feature_list["adjust_loaf_size"]
# - feature_list["adjust_timer_delay"]
# - feature_list["start_stop_operation"]

# Goal variable values:
# - variable_menu_index: "1" (Basic White)
# - variable_crust_color: "medium"
# - variable_loaf_size: "2LB"
# - variable_timer_delay: "05:00:00"
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass