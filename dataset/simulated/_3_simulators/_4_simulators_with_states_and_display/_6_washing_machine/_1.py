# 8 variables

# Variable for power on/off
# User manual: Press this button once to turn the washing machine on. Then press this button again to turn it off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for start/pause
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for cycle selection
variable_cycle_selector = DiscreteVariable(
    value_range=[
        "Super Eco Wash", "Outdoor Care", "Wool", "Hand Wash", "Spin", 
        "Rinse+Spin", "Cotton", "Synthetics", "15' Quick Wash", 
        "Baby Care", "Daily Wash", "Stain Away"
    ], 
    current_value="Cotton"
)

# Variable for temperature setting
variable_temperature = DiscreteVariable(
    value_range=["0", "Cold water 🌡️", "20 °C", "30 °C", "40 °C", "60 °C", "95 °C"], 
    current_value="0"
)

# Variable for spin speed
variable_spin_speed = DiscreteVariable(
    value_range=["0", "Rinse Hold", "🚫", "400", "800", "1200", "1400"], 
    current_value="0"
)

# Variable for option setting
variable_option = DiscreteVariable(
    value_range=[
        "off", "Soak", "Intensive", "Prewash", "Rinse+", 
        "Soak + Rinse+", "Intensive + Rinse+", "Prewash + Rinse+"
    ], 
    current_value="off"
)

# Variable for delay end
variable_delay_end = ContinuousVariable(
    value_ranges_steps=[(0, 3, 3), (3, 19, 1)], 
    current_value=0
)

# Variable for child lock
variable_child_lock = DiscreteVariable(value_range=["on", "off"], current_value="off")

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["start_pause"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["set_cycle"] = [
    {"step": 1, "actions": ["turn_cycle_selector_dial_clockwise", "turn_cycle_selector_dial_anticlockwise"], "variable": "variable_cycle_selector", "step_size": 12}
]

feature_list["set_temperature"] = [
    {"step": 1, "actions": ["press_temp_button"], "variable": "variable_temperature", "step_size": 7}
]

feature_list["set_spin_speed"] = [
    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin_speed", "step_size": 7}
]

feature_list["set_option"] = [
    {"step": 1, "actions": ["press_option_button"], "variable": "variable_option", "step_size": 8}
]

feature_list["set_delay_end"] = [
    {"step": 1, "actions": ["press_delay_end_button"], "variable": "variable_delay_end", "step_size": 17}
]

feature_list["child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_temp_button_and_spin_button"], "variable": "variable_child_lock", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_start_running = variable_start_running
        self.variable_cycle_selector = variable_cycle_selector
        self.variable_temperature = variable_temperature
        self.variable_spin_speed = variable_spin_speed
        self.variable_option = variable_option
        self.variable_delay_end = variable_delay_end
        self.variable_child_lock = variable_child_lock

    def press_power_button(self):
        # Update feature progress and set power to "on" or "off"
        self.feature.update_progress("press_power_button")
        self.variable_power_on_off.set_current_value("on" if self.variable_power_on_off.get_current_value() == "off" else "off")

    def press_start_pause_button(self):
        # Update feature progress and set start to "on" or "off"
        self.feature.update_progress("press_start_pause_button")
        self.variable_start_running.set_current_value("on" if self.variable_start_running.get_current_value() == "off" else "off")

    def turn_cycle_selector_dial_clockwise(self):
        # Update feature progress and set cycle to the next value
        self.feature.update_progress("turn_cycle_selector_dial_clockwise")
        self.execute_action_and_set_next("turn_cycle_selector_dial_clockwise")

    def turn_cycle_selector_dial_anticlockwise(self):
        # Update feature progress and set cycle to the previous value
        self.feature.update_progress("turn_cycle_selector_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_cycle_selector_dial_anticlockwise")

    def press_temp_button(self):
        # Update feature progress and set temperature to the next value
        self.feature.update_progress("press_temp_button")
        self.execute_action_and_set_next("press_temp_button")

    def press_spin_button(self):
        # Update feature progress and set spin speed to the next value
        self.feature.update_progress("press_spin_button")
        self.execute_action_and_set_next("press_spin_button")

    def press_option_button(self):
        # Update feature progress and set option to the next value
        self.feature.update_progress("press_option_button")
        self.execute_action_and_set_next("press_option_button")

    def press_delay_end_button(self):
        # Update feature progress and set delay end to the next value
        self.feature.update_progress("press_delay_end_button")
        self.execute_action_and_set_next("press_delay_end_button")

    def press_and_hold_temp_button_and_spin_button(self, duration=3):
        # Update feature progress and toggle child lock if held for 3 seconds
        self.feature.update_progress("press_and_hold_temp_button_and_spin_button")
        if duration >= 3:
            self.variable_child_lock.set_current_value("on" if self.variable_child_lock.get_current_value() == "off" else "off")