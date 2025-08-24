# The given code missed some features like "setting the preset timer for delayed cooking" and "adjust the preset timer". Correcting this... 
# User manual mentions: "If you want to enjoy delicious rice after 8 hours, set the preset time to 8 hours." 
# Current code doesn't account for adjusting preset time values explicitly or separate features for this operation.

# Updated feature for the requested user command to set mode to "white rice", adjust preset time, and start the machine.

variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
variable_cooking_mode = DiscreteVariable(
    value_range=["fast cook", "white rice", "congee", "soup", "cake", "keep warm"],
    current_value="fast cook"
)
variable_preset_timer = ContinuousVariable(
    value_ranges_steps=[(0, 1440, 15)],  # 0 to 1440 minutes (24 hours max) in steps of 15 minutes
    current_value=0
)

# Updated feature list
updated_feature_list = {}

# Feature: Start the appliance (ON state)
updated_feature_list["start_running"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", 
    "comment": "value always set to 'on'"},
]

# Feature: Set cooking mode
updated_feature_list["set_cooking_mode"] = [
    {"step": 1, "actions": ["press_menu_cancel_button"], "variable": "variable_cooking_mode"}
]

# Feature: Adjust preset timer
updated_feature_list["set_preset_timer"] = [
    {"step": 1, "actions": ["press_preset_time_time_button"], "variable": "variable_preset_timer"}
]

# Null feature for unused variables and actions
updated_feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

# Class that inherits from Simulator and applies updates
class ExtendedSimulator(Simulator):
    def reset(self):
        super().reset()
        self.feature = Feature(feature_list=updated_feature_list, current_value=("empty", 1))
        self.variable_start_running = variable_start_running
        self.variable_cooking_mode = variable_cooking_mode
        self.variable_preset_timer = variable_preset_timer

    # Update feature and set variable_start_running to "on"
    def press_start_button(self):
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_running":
            self.variable_start_running.set_current_value("on")

    # Update feature and adjust variable_cooking_mode
    def press_menu_cancel_button(self):
        self.feature.update_progress("press_menu_cancel_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_cooking_mode":
            self.execute_action_and_set_next("press_menu_cancel_button")

    # Update feature and adjust variable_preset_timer
    def press_preset_time_time_button(self):
        self.feature.update_progress("press_preset_time_time_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_preset_timer":
            self.execute_action_and_set_next("press_preset_time_time_button")