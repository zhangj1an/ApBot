# User command: Make soup with the rice cooker. Set the preset timer to 4 hours, then start.

# Verifying the existing code:
# Sequence of features needed to achieve the command:
# 1. Select the cooking mode to "Soup" using the "set_cooking_mode" feature.
# 2. Adjust the preset timer using the "set_preset_time" feature.
# 3. Finally, start the appliance using the "start_appliance" feature.

# Relevant user manual quotes:
# - "Select the Bean or Soup function by pressing the Menu button (fig. 10)." (Relevant to 'set_cooking_mode')
# - "To preset time for delayed cooking, press the Preset timer button, and the default preset time starts flashing on the display..." (Relevant to 'set_preset_time')
# - "Press the Start button to start cooking (fig. 8)." (Relevant to 'start_appliance')

# The existing code correctly models these features:
# Feature: "set_cooking_mode" -> Models the ability to select the cooking mode (Soup).
# Feature: "set_preset_time" -> Allows adjusting the preset timer to desired hours and minutes.
# Feature: "start_appliance" -> Starts the operation after configurations.

# Sequence of actions (as per existing feature_list):
# - Use "press_menu_button" to select "Soup" in the cooking mode.
# - Use "press_preset_timer_button", then "press_hr_button" to set the timer to 4 hours.
# - Use "press_start_button" to begin.

# Variables requiring changes:
# - `variable_cooking_mode`: Set to "Soup".
# - `variable_preset_time_hr`: Set to 4.
# - `variable_start_running`: Set to "on".

# Since the code already includes the necessary features and actions, no modifications are needed.

class ExtendedSimulator(Simulator):
    pass