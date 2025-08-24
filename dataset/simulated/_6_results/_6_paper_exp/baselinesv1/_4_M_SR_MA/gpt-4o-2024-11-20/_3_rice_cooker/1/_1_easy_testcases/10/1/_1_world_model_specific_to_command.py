# Python comments listing the sequence of features needed to achieve this command:
# 1. Use "set_cooking_mode" to select "Glutinous rice".
#    - User manual: "6. Select the Glutinous Rice function by pressing the menu button (fig. 7)."
#    - Feature: set_cooking_mode
# 2. Use "adjust_cooking_time" to set the cooking time to 1 hour and 10 minutes.
#    - User manual: "6. Press the 'Cooking time' button." and "7. Adjust time values with 'Hr.' or 'Min.' buttons."
#    - Feature: adjust_cooking_time
# 3. Use "start_appliance" to start cooking.
#    - User manual: "8. Press the 'Start' button to start cooking (fig. 8)."
#    - Feature: start_appliance

# Goal variable values:
# variable_cooking_mode: "Glutinous rice"
# variable_cooking_time_hr: 1
# variable_cooking_time_min: 10
# variable_start_running: "on"

class ExtendedSimulator(Simulator):
    pass