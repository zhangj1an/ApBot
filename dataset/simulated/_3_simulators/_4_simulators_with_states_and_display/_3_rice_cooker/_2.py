# 3 variables

# Variable for start running
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for cooking mode selection
variable_cooking_mode = DiscreteVariable(
    value_range=["Fast cook", "White rice", "Congee", "Soup", "Cake", "Keep warm"],
    current_value="Fast cook"
)

# Variable for preset timer
variable_preset_timer = ContinuousVariable(
    value_ranges_steps=[(0, 24, 0.25)],  # 15 minutes step, total 24 hours
    current_value=0
)

feature_list = {}

feature_list["cooking_mode_selection"] = [
    {"step": 1, "actions": ["press_menu_cancel_button"], "variable": "variable_cooking_mode", "step_size": 6}
]

feature_list["preset_timer"] = [
    {"step": 1, "actions": ["press_preset_time_time_button"], "variable": "variable_preset_timer", "step_size": 48},
]

feature_list["start_cooking"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_start_running = variable_start_running
        self.variable_cooking_mode = variable_cooking_mode
        self.variable_preset_timer = variable_preset_timer

    def press_start_button(self):
        # Update feature progress
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]

        # If in start_cooking feature, set start_running to "on"
        if current_feature == "start_cooking":
            self.variable_start_running.set_current_value("on")

        # If in preset_timer feature, set the preset timer
        elif current_feature == "preset_timer":
            self.execute_action_and_set_next("press_start_button")

    def press_menu_cancel_button(self):
        # Update feature progress
        self.feature.update_progress("press_menu_cancel_button")
        current_feature = self.feature.current_value[0]

        # If in cooking_mode_selection feature, cycle through cooking modes
        if current_feature == "cooking_mode_selection":
            self.execute_action_and_set_next("press_menu_cancel_button")

    def press_preset_time_time_button(self):
        # Update feature progress
        self.feature.update_progress("press_preset_time_time_button")
        current_feature = self.feature.current_value[0]

        # If in preset_timer feature, adjust the preset timer
        if current_feature == "preset_timer":
            self.execute_action_and_set_next("press_preset_time_time_button")