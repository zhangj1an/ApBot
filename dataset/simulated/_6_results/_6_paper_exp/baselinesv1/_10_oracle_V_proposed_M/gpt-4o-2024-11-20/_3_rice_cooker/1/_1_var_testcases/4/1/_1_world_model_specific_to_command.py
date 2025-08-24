# The given code already accurately models the requested user command based on the user manual. 
# The sequence of features needed is:
# 1. "select_menu_option": To set the menu option to "Glutinous rice".
# 2. "set_preset_timer": To set the timer (hours to 3 and minutes to 0).
# 3. "start_cooking": To start the cooking process.

# User manual excerpts corresponding to the user command:
# - "Select menu options: Glutinous rice, Porridge, Bean, Soup, Steam, Reheat."
# - "You can preset the delayed cooking time for some menus. The preset timer is available from 1 hour up to 24 hours."
# - "Press the start button to begin cooking."

# The relevant feature list in the given code includes:
# - "select_menu_option" for setting the `variable_menu_index` to "Glutinous rice".
# - "set_preset_timer" for adjusting `variable_preset_timer_hours` and `variable_preset_timer_minutes`.
# - "start_cooking" for starting cooking by setting `variable_start_cooking` to "on".

# The goal variable values to achieve the user command are:
# - `variable_menu_index` = "Glutinous rice".
# - `variable_preset_timer_hours` = 3.
# - `variable_preset_timer_minutes` = 0.
# - `variable_start_cooking` = "on".

class ExtendedSimulator(Simulator): 
    pass