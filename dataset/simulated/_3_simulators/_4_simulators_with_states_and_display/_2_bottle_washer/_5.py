# 5 variables

# User manual: Press this button to switch the steriliser on and off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Sterilise only function
variable_sterilise_only_time = DiscreteVariable(value_range=["0", "10", "35"], current_value="0")

# Drying only function
variable_drying_only_time = DiscreteVariable(value_range=["0", "30", "40", "50"], current_value="0")

# Auto mode
variable_auto_mode_time = DiscreteVariable(value_range=["0", "35", "60"], current_value="0")

# Storage function
variable_storage_mode = DiscreteVariable(value_range=["off", "on"], current_value="off")

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_power_on_off_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["sterilise_only"] = [
    {"step": 1, "actions": ["press_sterilise_only_button"], "variable": "variable_sterilise_only_time", "step_size": 3}
]

feature_list["drying_only"] = [
    {"step": 1, "actions": ["press_drying_only_button"], "variable": "variable_drying_only_time", "step_size": 4}
]

feature_list["auto_mode"] = [
    {"step": 1, "actions": ["press_auto_mode_button"], "variable": "variable_auto_mode_time", "step_size": 3}
]

feature_list["storage_mode"] = [
    {"step": 1, "actions": ["press_storage_button"], "variable": "variable_storage_mode", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_sterilise_only_time = variable_sterilise_only_time
        self.variable_drying_only_time = variable_drying_only_time
        self.variable_auto_mode_time = variable_auto_mode_time
        self.variable_storage_mode = variable_storage_mode

    def press_power_on_off_button(self):
        # This action toggles the power state between "on" and "off".
        self.feature.update_progress("press_power_on_off_button")
        self.execute_action_and_set_next("press_power_on_off_button")

    def press_sterilise_only_button(self):
        # This action sets the sterilise only time to either 10 or 35 minutes.
        self.feature.update_progress("press_sterilise_only_button")
        self.execute_action_and_set_next("press_sterilise_only_button")

    def press_drying_only_button(self):
        # This action sets the drying only time to 30, 40, or 50 minutes.
        self.feature.update_progress("press_drying_only_button")
        self.execute_action_and_set_next("press_drying_only_button")

    def press_auto_mode_button(self):
        # This action sets the auto mode time to either 35 or 60 minutes.
        self.feature.update_progress("press_auto_mode_button")
        self.execute_action_and_set_next("press_auto_mode_button")

    def press_storage_button(self):
        # This action toggles the storage mode between "on" and "off".
        self.feature.update_progress("press_storage_button")
        self.execute_action_and_set_next("press_storage_button")