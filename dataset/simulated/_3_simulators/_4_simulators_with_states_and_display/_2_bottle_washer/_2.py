# 5 variables

# User manual: Press this button to turn on the appliance and the light is on. Press again to turn it off and the light is off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for bottle type selection
variable_bottle_type = DiscreteVariable(value_range=["Milk bag", "Plastic", "Silicone"], current_value="Milk bag")

# Variable for initial temperature selection
variable_initial_temp = DiscreteVariable(value_range=["Room- 25℃ (77℉)", "Refrig- 4℃ (39.2℉)", "Frozen- 0℃ (32℉)"], current_value="Room- 25℃ (77℉)")

# Variable for volume selection
variable_volume = DiscreteVariable(value_range=["1-3 fl-oz", "4-6 fl-oz", "7+ fl-oz"], current_value="1-3 fl-oz")

# Variable for night light
variable_night_light = DiscreteVariable(value_range=["on", "off"], current_value="off")

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["select_bottle_type"] = [
    {"step": 1, "actions": ["press_bottle_button"], "variable": "variable_bottle_type", "step_size": 3}
]

feature_list["select_initial_temp"] = [
    {"step": 1, "actions": ["press_initial_temp_button"], "variable": "variable_initial_temp", "step_size": 3}
]

feature_list["select_volume"] = [
    {"step": 1, "actions": ["press_volume_button"], "variable": "variable_volume", "step_size": 3}
]

feature_list["control_night_light"] = [
    {"step": 1, "actions": ["press_and_hold_power_button"], "variable": "variable_night_light", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_bottle_type = variable_bottle_type
        self.variable_initial_temp = variable_initial_temp
        self.variable_volume = variable_volume
        self.variable_night_light = variable_night_light

    def press_power_button(self):
        # Update feature progress and toggle power on/off
        self.feature.update_progress("press_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "turn_on_off":
            self.execute_action_and_set_next("press_power_button")

    def press_bottle_button(self):
        # Update feature progress and cycle through bottle types
        self.feature.update_progress("press_bottle_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_bottle_type":
            self.execute_action_and_set_next("press_bottle_button")

    def press_initial_temp_button(self):
        # Update feature progress and cycle through initial temperatures
        self.feature.update_progress("press_initial_temp_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_initial_temp":
            self.execute_action_and_set_next("press_initial_temp_button")

    def press_volume_button(self):
        # Update feature progress and cycle through volume options
        self.feature.update_progress("press_volume_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_volume":
            self.execute_action_and_set_next("press_volume_button")

    def press_and_hold_power_button(self, duration=3):
        # Update feature progress and toggle night light if held for 3 seconds
        self.feature.update_progress("press_and_hold_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "control_night_light" and duration >= 3:
            self.execute_action_and_set_next("press_and_hold_power_button")