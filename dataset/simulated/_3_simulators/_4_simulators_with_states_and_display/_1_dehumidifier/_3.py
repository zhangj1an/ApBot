# 5 variables

# User manual: Power Button: Turn air purifier on and off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Timer Button: Time can be selected from 1, 2, 4, and 8 hours.
variable_timer = DiscreteVariable(value_range=["0", "1", "2", "4", "8"], current_value="0")

# UV/UV Reset Button: Press UV button once to turn on the UV light; Press UV button again, the UV light will turn off.
variable_uv_light = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Ionizer/Filter Reset: Press Ionizer button once to turn the ionizer on; Press Ionizer button again, the ionizer will turn off.
variable_ionizer = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Fan Speed/Mode: Press the Speed/Mode button to cycle between fan speeds 1, 2, 3, & Turbo and Auto mode and Sleep mode.
variable_fan_speed_mode = DiscreteVariable(value_range=["1", "2", "3", "Turbo", "Auto", "Sleep"], current_value="1")

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["set_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer", "step_size": 5}
]

feature_list["uv_light_control"] = [
    {"step": 1, "actions": ["press_uv_button"], "variable": "variable_uv_light", "step_size": 2}
]

feature_list["ionizer_control"] = [
    {"step": 1, "actions": ["press_ionizer_button"], "variable": "variable_ionizer", "step_size": 2}
]

feature_list["fan_speed_mode"] = [
    {"step": 1, "actions": ["press_speed_mode_button"], "variable": "variable_fan_speed_mode", "step_size": 6}
]

feature_list["uv_reset"] = [
    {"step": 1, "actions": ["press_and_hold_uv_button"]}
]

feature_list["filter_reset"] = [
    {"step": 1, "actions": ["press_and_hold_ionizer_button"]}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_timer = variable_timer
        self.variable_uv_light = variable_uv_light
        self.variable_ionizer = variable_ionizer
        self.variable_fan_speed_mode = variable_fan_speed_mode

    # Power button: Toggles the power state between "on" and "off"
    def press_power_button(self):
        self.feature.update_progress("press_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "turn_on_off":
            self.execute_action_and_set_next("press_power_button")

    # Timer button: Cycles through timer options 1, 2, 4, and 8 hours
    def press_timer_button(self):
        self.feature.update_progress("press_timer_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_timer":
            self.execute_action_and_set_next("press_timer_button")

    # UV button: Toggles the UV light state between "on" and "off"
    def press_uv_button(self):
        self.feature.update_progress("press_uv_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "uv_light_control":
            self.execute_action_and_set_next("press_uv_button")

    # Ionizer button: Toggles the ionizer state between "on" and "off"
    def press_ionizer_button(self):
        self.feature.update_progress("press_ionizer_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "ionizer_control":
            self.execute_action_and_set_next("press_ionizer_button")

    # Speed/Mode button: Cycles through fan speeds and modes
    def press_speed_mode_button(self):
        self.feature.update_progress("press_speed_mode_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "fan_speed_mode":
            self.execute_action_and_set_next("press_speed_mode_button")

    # UV reset: Resets the UV indicator
    def press_and_hold_uv_button(self, duration=3):
        self.feature.update_progress("press_and_hold_uv_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "uv_reset" and duration >= 3:
            self.execute_action_and_set_next("press_and_hold_uv_button")

    # Filter reset: Resets the filter indicator
    def press_and_hold_ionizer_button(self, duration=3):
        self.feature.update_progress("press_and_hold_ionizer_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "filter_reset" and duration >= 3:
            self.execute_action_and_set_next("press_and_hold_ionizer_button")