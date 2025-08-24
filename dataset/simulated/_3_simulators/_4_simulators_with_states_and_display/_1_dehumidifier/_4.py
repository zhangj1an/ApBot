# 4 variables

# User manual: Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Microbe Shield™/Night Mode feature
variable_microbe_shield_night_mode = DiscreteVariable(value_range=["off", "microbe_shield", "night_mode"], current_value="off")

# Fan Speed feature
variable_fan_speed = DiscreteVariable(value_range=["low", "medium", "high", "turbo"], current_value="low")

# Timer feature
variable_timer = DiscreteVariable(value_range=["0", "2H", "4H", "8H"], current_value="0")

feature_list = {}

feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["microbe_shield_night_mode"] = [
    {"step": 1, "actions": ["press_microbe_shield_night_mode_button"], "variable": "variable_microbe_shield_night_mode", "step_size": 3}
]

feature_list["fan_speed"] = [
    {"step": 1, "actions": ["press_fan_speed_button"], "variable": "variable_fan_speed", "step_size": 4}
]

feature_list["timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer", "step_size": 4}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_microbe_shield_night_mode = variable_microbe_shield_night_mode
        self.variable_fan_speed = variable_fan_speed
        self.variable_timer = variable_timer

    def press_power_button(self):
        # Update feature progress and set power variable to next value
        self.feature.update_progress("press_power_button")
        self.execute_action_and_set_next("press_power_button")

    def press_microbe_shield_night_mode_button(self):
        # Update feature progress and set microbe shield/night mode variable to next value
        self.feature.update_progress("press_microbe_shield_night_mode_button")
        self.execute_action_and_set_next("press_microbe_shield_night_mode_button")

    def press_fan_speed_button(self):
        # Update feature progress and set fan speed variable to next value
        self.feature.update_progress("press_fan_speed_button")
        self.execute_action_and_set_next("press_fan_speed_button")

    def press_timer_button(self):
        # Update feature progress and set timer variable to next value
        self.feature.update_progress("press_timer_button")
        self.execute_action_and_set_next("press_timer_button")