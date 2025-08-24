# The current code already models the appliance features relevant for the user command correctly.
# User command: "Set the rice cooker to prepare beans in the rice cooker to be cooked for 1 hour and 10 minutes, then start."

# Sequence of features needed to achieve this command:
# 1. Select the cooking mode "Bean" using the "set_cooking_mode" feature.
#    - User manual: "Press the 'Menu' button to select the desired function."
#    - Feature: feature_list["set_cooking_mode"]
# 2. Set the cooking time to 1 hour and 10 minutes using the "adjust_cooking_time" feature.
#    - User manual: "Select the cooking time by pressing the Hour ('Hr.') and Minute ('Min.') buttons."
#    - Feature: feature_list["adjust_cooking_time"]
# 3. Start cooking using the "start_appliance" feature.
#    - User manual: "Press the 'Start' button."
#    - Feature: feature_list["start_appliance"]

# Goal variable values to achieve this command:
# - variable_cooking_mode = "Bean"
# - variable_cooking_time_hr = 1
# - variable_cooking_time_min = 10
# - variable_start_running = "on"

class ExtendedSimulator(Simulator):
    pass