# 4 variables

# User manual: Press the On/Off (power symbol) button once and the function icons will light up.
variable_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for the drying time in the Automatic Sterilize/Dry Function
variable_drying_time = DiscreteVariable(value_range=["0", "30", "45", "60"], current_value="0")

# Variable for the sterilization cycle in the Automatic Sterilize/Dry Function and Sterilize Only Function
variable_sterilization_cycle = DiscreteVariable(value_range=["0", "running"], current_value="0")

# Variable for the drying cycle in the Dryer Only Function
variable_drying_cycle = DiscreteVariable(value_range=["0", "30", "45", "60"], current_value="0")

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_on_off", "step_size": 2}
]

feature_list["automatic_sterilize_dry"] = [
    {"step": 1, "actions": ["press_automatic_sterilize_dry_button"], "variable": "variable_drying_time", "comment": "variable_sterilization_cycle: set to running", "step_size": 4}
]

feature_list["sterilize_only"] = [
    {"step": 1, "actions": ["press_sterilize_only_button"], "comment": "variable_sterilization_cycle: set to running", , "step_size": 2}
]

feature_list["dry_only"] = [
    {"step": 1, "actions": ["press_dry_only_button"], "variable": "variable_drying_cycle", "step_size": 4}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_on_off = variable_on_off
        self.variable_drying_time = variable_drying_time
        self.variable_sterilization_cycle = variable_sterilization_cycle
        self.variable_drying_cycle = variable_drying_cycle

    def press_on_off_button(self):
        # This action toggles the on/off state of the appliance.
        self.feature.update_progress("press_on_off_button")
        self.execute_action_and_set_next("press_on_off_button")

    def press_automatic_sterilize_dry_button(self):
        # This action sets the drying time and starts the sterilization cycle.
        self.feature.update_progress("press_automatic_sterilize_dry_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "automatic_sterilize_dry":
            self.variable_sterilization_cycle.set_current_value("running")
            self.execute_action_and_set_next("press_automatic_sterilize_dry_button")

    def press_sterilize_only_button(self):
        # This action starts the sterilization cycle.
        self.feature.update_progress("press_sterilize_only_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "sterilize_only":
            self.variable_sterilization_cycle.set_current_value("running")

    def press_dry_only_button(self):
        # This action sets the drying cycle time.
        self.feature.update_progress("press_dry_only_button")
        self.execute_action_and_set_next("press_dry_only_button")