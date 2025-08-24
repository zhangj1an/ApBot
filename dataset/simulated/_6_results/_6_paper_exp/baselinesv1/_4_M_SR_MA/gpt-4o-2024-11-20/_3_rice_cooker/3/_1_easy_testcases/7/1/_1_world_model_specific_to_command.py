# The current given code correctly implements the features to achieve the user command:
# "Set the rice cooker to Quinoa, and reduce the cooking time to 20 minutes, and start running."
# Below is the sequence of features and user actions needed to achieve the command:
# 
# 1. Use feature "set_menu" to set `variable_menu_index` to "Quinoa".
#    User Manual Quote: "Press menu button to scroll through preset functions, White Rice, Brown Rice, Quinoa, Steel Cut Oats. Indicator light shows which function is selected."
#    Feature: feature_list["set_menu"]
#
# 2. Use the same feature "set_menu" to adjust `variable_menu_setting_Quinoa` (Reduce cooking time to 20 minutes).
#    User Manual Quote: "Press start if cooking time is okay. Use + and - if you want to adjust time."
#    Feature: feature_list["set_menu"]
#
# 3. Use feature "start_cooking" to start the cooking process by setting `variable_start_running` to "on".
#    User Manual Quote: "Press to start cooking."
#    Feature: feature_list["start_cooking"]
#
# Goal Variable Values:
# - variable_menu_index: "Quinoa"
# - variable_menu_setting_quinoa: 20
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass