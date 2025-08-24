# 10 variables
# User manual: Press POWER, the Dehumidifier Starts Operation.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: MODE: select auto dehumidification, Continuous dehumidification, Drying clothes, purification and ventilation, etc.
variable_mode = DiscreteVariable(value_range=["auto dehumidification", "continuous dehumidification", "drying clothes", "purification", "ventilation"], current_value="auto dehumidification")

# User manual: SLEEP: start ultra silent air speed;
variable_sleep = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: DRYING: press it for more than 2s to start internal drying function;
variable_internal_drying = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: IONIZER: start anion function;
variable_anion = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: SWING: start air swing function to realize wide-angle air sweeping;
variable_swing = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: TIMER: realize start/shutdown of the dehumidifier at fixed time;
variable_timer = ContinuousVariable(value_ranges_steps=[(0, 24, 1)], current_value=0)

# User manual: Humidity can be set in Auto mode, wind speed can be adjusted in air purification mode and wind mode;
variable_humidity = ContinuousVariable(value_ranges_steps=[(0, 40, 40), (40, 70, 5)], current_value=0)

# User manual: press "humidity" button and "Timer" button together to achieve °C and °F conversion.
variable_temperature_unit = DiscreteVariable(value_range=["Celsius", "Fahrenheit"], current_value="Celsius")

# User manual: press MODE for over 2s to start child lock function;
variable_child_lock = DiscreteVariable(value_range=["locked", "unlocked"], current_value="unlocked")

feature_list = {}

feature_list["power"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["mode_selection"] = [
    {"step": 1, "actions": ["press_mode_button"], "variable": "variable_mode", "step_size": 5}
]

feature_list["child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_child_lock_button"], "variable": "variable_child_lock", "step_size": 2}
]

feature_list["sleep_mode"] = [
    {"step": 1, "actions": ["press_sleep_button"], "variable": "variable_sleep", "step_size": 2}
]

feature_list["internal_drying"] = [
    {"step": 1, "actions": ["press_and_hold_drying_button"], "variable": "variable_internal_drying", "step_size": 2}
]

feature_list["anion_function"] = [
    {"step": 1, "actions": ["press_anion_button"], "variable": "variable_anion" , "step_size": 2}
]

feature_list["air_swing"] = [
    {"step": 1, "actions": ["press_swing_button"], "variable": "variable_swing", "step_size": 2}
]

feature_list["timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer" , "step_size": 25}
]

feature_list["humidity_setting"] = [
    {"step": 1, "actions": ["press_humidity_button"], "variable": "variable_humidity", "step_size": 7}
]

feature_list["temperature_unit_conversion"] = [
    {"step": 1, "actions": ["press_and_hold_humidity_button_and_timer_button"], "variable": "variable_temperature_unit", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_mode = variable_mode
        self.variable_sleep = variable_sleep
        self.variable_internal_drying = variable_internal_drying
        self.variable_anion = variable_anion
        self.variable_swing = variable_swing
        self.variable_timer = variable_timer
        self.variable_humidity = variable_humidity
        self.variable_temperature_unit = variable_temperature_unit
        self.variable_child_lock = variable_child_lock

    def press_power_button(self):
        # Update feature and set variable to "on" or "off"
        self.feature.update_progress("press_power_button")
        self.variable_power_on_off.set_current_value("on" if self.variable_power_on_off.get_current_value() == "off" else "off")

    def press_mode_button(self):
        # Update feature and cycle through modes
        self.feature.update_progress("press_mode_button")
        self.execute_action_and_set_next("press_mode_button")

    def press_and_hold_mode_button(self, duration=3):
        # Update feature and enable child lock if duration >= 3 seconds
        self.feature.update_progress("press_and_hold_mode_button")
        if duration >= 3:
            self.variable_child_lock.set_current_value("locked")

    def press_sleep_button(self):
        # Update feature and toggle sleep mode
        self.feature.update_progress("press_sleep_button")
        self.variable_sleep.set_current_value("on" if self.variable_sleep.get_current_value() == "off" else "off")

    def press_and_hold_drying_button(self, duration=2):
        # Update feature and enable internal drying if duration >= 2 seconds
        self.feature.update_progress("press_and_hold_drying_button")
        if duration >= 2:
            self.variable_internal_drying.set_current_value("on" if self.variable_internal_drying.get_current_value() == "off" else "off")

    def press_anion_button(self):
        # Update feature and toggle anion function
        self.feature.update_progress("press_anion_button")
        self.variable_anion.set_current_value("on" if self.variable_anion.get_current_value() == "off" else "off")

    def press_swing_button(self):
        # Update feature and toggle air swing
        self.feature.update_progress("press_swing_button")
        self.variable_swing.set_current_value("on" if self.variable_swing.get_current_value() == "off" else "off")

    def press_timer_button(self):
        # Update feature and adjust timer
        self.feature.update_progress("press_timer_button")
        self.execute_action_and_set_next("press_timer_button")

    def press_humidity_button(self):
        # Update feature and adjust humidity
        self.feature.update_progress("press_humidity_button")
        self.execute_action_and_set_next("press_humidity_button")

    def press_and_hold_humidity_button_and_timer_button(self, duration=3):
        # Update feature and toggle temperature unit if duration >= 3 seconds
        self.feature.update_progress("press_and_hold_humidity_button_and_timer_button")
        if duration >= 3:
            new_unit = "Fahrenheit" if self.variable_temperature_unit.get_current_value() == "Celsius" else "Celsius"
            self.variable_temperature_unit.set_current_value(new_unit)

    def run_action(self, action_name, execution_times=1, **kwargs):
        # Check child lock status
        if self.variable_child_lock.get_current_value() == "locked" and action_name not in ["press_power_button", "press_and_hold_mode_button"]:
            self.display = "child lock: locked"
            return self.display

        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)