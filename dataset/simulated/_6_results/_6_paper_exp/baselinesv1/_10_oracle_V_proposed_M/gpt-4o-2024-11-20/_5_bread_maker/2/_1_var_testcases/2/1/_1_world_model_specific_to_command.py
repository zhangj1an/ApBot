# Based on the user command and the given code for the Simulator class, we'll evaluate whether the code correctly models all relevant appliance features to achieve the user command.

# User Command Summary: Start a small, dark-crust wholewheat loaf using wholewheat menu, with a 2-hour timer delay, then start the breadmaker.

# Key actions required:
# 1. Set the menu to "3 Wholewheat".
# 2. Adjust the loaf size to "1.5lb".
# 3. Adjust the crust color to "dark".
# 4. Set the timer delay to 2 hours (120 minutes).
# 5. Start the breadmaker.

# Checking against the given feature list and the user manual:
# - The feature "set_menu" correctly models step 1 (setting menu).
# - The feature "adjust_loaf_size" correctly models step 2 (adjusting loaf size).
# - The feature "adjust_crust_color" correctly models step 3 (adjusting crust color).
# - The feature "adjust_timer" correctly models step 4, as it allows modifying the timer delay in 10-minute increments (relevant for 2-hour delay).
# - The feature "start_stop" correctly models step 5 (starting the breadmaker).

# All required features are included in the code; no adjustments are needed.

# Quoting relevant user manual text:
# - To set the menu: "For choosing the bread making program from the list 1 to 12."
# - To select loaf size: "For selecting small (1.5lb) or large (2lb) loaf size."
# - To select crust color: "For selecting crust color from light, medium or dark."
# - To set timer delay: "Use to delay the start of bread making (all programs except Fastbake)."
# - To start the breadmaker: "Press to start for approx 1 second, a beep sounds and the colon (:) flashes and the program starts."

# Quoting feature names corresponding to the user command:
# - Feature for step 1: "set_menu"
# - Feature for step 2: "adjust_loaf_size"
# - Feature for step 3: "adjust_crust_color"
# - Feature for step 4: "adjust_timer"
# - Feature for step 5: "start_stop"

# Goal Variable Values:
variable_menu_index.set_current_value("3 Wholewheat")
variable_loaf_size.set_current_value("1.5lb")
variable_crust_color.set_current_value("dark")
variable_timer_delay.set_current_value(120)  # Timer delay set to 2 hours (120 minutes)
variable_start_running.set_current_value("on")

class ExtendedSimulator(Simulator): 
    pass