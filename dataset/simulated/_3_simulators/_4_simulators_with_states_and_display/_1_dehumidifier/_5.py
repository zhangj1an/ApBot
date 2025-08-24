# 5 variables

# User manual: Turns the unit on and off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: Fan/Air Speed (SPEED) | 1. Low 2. Mid 3. High
variable_fan_speed = DiscreteVariable(value_range=["low", "mid", "high"], current_value="low")

# User manual: Turns the negative Ion generator on and off
variable_ion_generator = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: Sets an Auto-On or Shut-Off timer, 1H, 2H or 4H.
variable_timer = DiscreteVariable(value_range=["0", "1H", "2H", "4H"], current_value="0")

# User manual: Press to send the display to sleep. The unit will continue working on the low fan mode but the lights will turn off.
variable_sleep_mode = DiscreteVariable(value_range=["on", "off"], current_value="off")

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["adjust_fan_speed"] = [
    {"step": 1, "actions": ["press_speed_button"], "variable": "variable_fan_speed", "step_size": 3}
]

feature_list["toggle_ion_generator"] = [
    {"step": 1, "actions": ["press_ion_button"], "variable": "variable_ion_generator", "step_size": 2}
]

feature_list["set_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer", "step_size": 4}
]

feature_list["activate_sleep_mode"] = [
    {"step": 1, "actions": ["press_sleep_button"], "variable": "variable_sleep_mode", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_fan_speed = variable_fan_speed
        self.variable_ion_generator = variable_ion_generator
        self.variable_timer = variable_timer
        self.variable_sleep_mode = variable_sleep_mode

    def press_power_button(self):
        # Update feature and set variable based on input string
        self.feature.update_progress("press_power_button")
        # Set the power variable to the next value in its range
        self.execute_action_and_set_next("press_power_button")

    def press_speed_button(self):
        # Update feature and set variable based on input string
        self.feature.update_progress("press_speed_button")
        # Set the fan speed variable to the next value in its range
        self.execute_action_and_set_next("press_speed_button")

    def press_ion_button(self):
        # Update feature and set variable based on input string
        self.feature.update_progress("press_ion_button")
        # Set the ion generator variable to the next value in its range
        self.execute_action_and_set_next("press_ion_button")

    def press_timer_button(self):
        # Update feature and set variable based on input string
        self.feature.update_progress("press_timer_button")
        # Set the timer variable to the next value in its range
        self.execute_action_and_set_next("press_timer_button")

    def press_sleep_button(self):
        # Update feature and set variable based on input string
        self.feature.update_progress("press_sleep_button")
        # Set the sleep mode variable to the next value in its range
        self.execute_action_and_set_next("press_sleep_button")