# 5 variables

# User manual: Press the ⏻ button to turn on/off the unit.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for temperature setting in Cool Mode
variable_cool_mode_temperature = ContinuousVariable(value_ranges_steps=[(0, 18, 18), (18, 32, 1)], current_value=0)

# Variable for fan speed setting
variable_fan_speed = DiscreteVariable(value_range=["HIGH", "MED", "LOW", "AUTO"], current_value="HIGH")

# Variable for operating mode
variable_operating_mode = DiscreteVariable(value_range=["COOL", "FAN", "DRY", "SMART"], current_value="COOL")

# Variable for programmable timer
variable_timer = ContinuousVariable(value_ranges_steps=[(0, 1, 1), (1, 24, 1)], current_value=0)

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["adjust_cool_mode_temperature"] = [
    {"step": 1, "actions": ["press_mode_button"], "variable": "variable_operating_mode", "step_size": 4},  # Ensure the mode is set to COOL
    {"step": 2, "actions": ["press_increase_temp_setting_button", "press_decrease_temp_setting_button"], "variable": "variable_cool_mode_temperature", "step_size": 15}
]

feature_list["adjust_fan_speed"] = [
    {"step": 1, "actions": ["press_speed_uv_button"], "variable": "variable_fan_speed", "step_size": 4}
]

feature_list["adjust_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer", "step_size": 25}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_cool_mode_temperature = variable_cool_mode_temperature
        self.variable_fan_speed = variable_fan_speed
        self.variable_operating_mode = variable_operating_mode
        self.variable_timer = variable_timer

    def press_on_off_button(self):
        # This action toggles the power state of the appliance.
        self.feature.update_progress("press_on_off_button")
        self.variable_power_on_off.set_current_value("on" if self.variable_power_on_off.get_current_value() == "off" else "off")

    def press_increase_temp_setting_button(self):
        # This action increases the temperature setting in Cool Mode.
        self.feature.update_progress("press_increase_temp_setting_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_cool_mode_temperature":
            self.execute_action_and_set_next("press_increase_temp_setting_button")

    def press_decrease_temp_setting_button(self):
        # This action decreases the temperature setting in Cool Mode.
        self.feature.update_progress("press_decrease_temp_setting_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_cool_mode_temperature":
            self.execute_action_and_set_prev("press_decrease_temp_setting_button")

    def press_speed_uv_button(self):
        # This action adjusts the fan speed.
        self.feature.update_progress("press_speed_uv_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_fan_speed":
            self.execute_action_and_set_next("press_speed_uv_button")

    def press_mode_button(self):
        # This action changes the operating mode.
        self.feature.update_progress("press_mode_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_cool_mode_temperature":
            self.execute_action_and_set_next("press_mode_button")

    def press_timer_button(self):
        # This action adjusts the programmable timer.
        self.feature.update_progress("press_timer_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer":
            self.execute_action_and_set_next("press_timer_button")