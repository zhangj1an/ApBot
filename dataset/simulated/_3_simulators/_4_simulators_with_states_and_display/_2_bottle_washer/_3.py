# 4 variables

# User manual: Press and hold the "Power" button for 3 seconds to turn on the Bottle Washer Pro®.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Wash mode selection
variable_wash_mode = DiscreteVariable(
    value_range=["Wash & Dry", "Wash, Sterilize, Dry", "Wash Only"],
    current_value="Wash & Dry"
)

# Sterilize-Dry mode selection
variable_sterilize_dry_mode = DiscreteVariable(
    value_range=["Sterilize & Dry", "Dry Only", "Sterilize Only"],
    current_value="Sterilize & Dry"
)

# Start/Pause functionality
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_and_hold_power_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["select_wash_mode"] = [
    {"step": 1, "actions": ["press_wash_mode_button"], "variable": "variable_wash_mode", "step_size": 3}
]

feature_list["select_sterilize_dry_mode"] = [
    {"step": 1, "actions": ["press_sterilize_dry_button"], "variable": "variable_sterilize_dry_mode", "step_size": 3}
]

feature_list["start_pause"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_wash_mode = variable_wash_mode
        self.variable_sterilize_dry_mode = variable_sterilize_dry_mode
        self.variable_start_running = variable_start_running

    def press_wash_mode_button(self):
        # Update feature progress and adjust wash mode variable
        self.feature.update_progress("press_wash_mode_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_wash_mode":
            self.execute_action_and_set_next("press_wash_mode_button")

    def press_sterilize_dry_button(self):
        # Update feature progress and adjust sterilize-dry mode variable
        self.feature.update_progress("press_sterilize_dry_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_sterilize_dry_mode":
            self.execute_action_and_set_next("press_sterilize_dry_button")

    def press_and_hold_power_button(self, duration=3):
        # Update feature progress and set power on/off based on duration
        self.feature.update_progress("press_and_hold_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "turn_on_off":
            if duration >= 3:
                self.execute_action_and_set_next("press_and_hold_power_button")

    def press_start_pause_button(self):
        # Update feature progress and set start/pause variable
        self.feature.update_progress("press_start_pause_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_pause":
            self.execute_action_and_set_next("press_start_pause_button")