# As per the user manual, the air purifier's features are correctly modeled in the provided feature_list. 
# Here is the sequence of features and their corresponding feature_list names to achieve the user command:

# 1. Turn on the dehumidifier:
# - Feature: power_control
# - User manual: Power Button: Turn air purifier on and off.
# - Feature_list name: "power_control"

# 2. Set the timer to run for 2 hours:
# - Feature: adjust_timer
# - User manual: Timer Button: Time can be selected from 1, 2, 4, and 8 hours.
# - Feature_list name: "adjust_timer"

# Goal Variable Values:
# - Set variable_power_on_off to "on".
# - Set variable_timer to "2H".

class ExtendedSimulator(Simulator): 
    pass