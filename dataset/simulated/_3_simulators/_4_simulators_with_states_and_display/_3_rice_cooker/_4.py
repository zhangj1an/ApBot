# 5 variables

# Variable for start running
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for menu selection
variable_menu_index = DiscreteVariable(
    value_range=["WHITE RICE", "BROWN", "PORRIDGE", "GRAINS", "MIXED", "STEAM", "SOUP", "STEW"],
    current_value="WHITE RICE"
)

# Variable for delay timer
variable_delay_timer = ContinuousVariable(
    value_ranges_steps=[(0, 12, 1)],
    current_value=0
)

# Variable for quick rice function
variable_quick_rice = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for keep warm/cancel function
variable_keep_warm_cancel = DiscreteVariable(value_range=["on", "off"], current_value="off")

feature_list = {}

feature_list["quick_rice"] = [
    {"step": 1, "actions": ["press_quick_rice_button"], "variable": "variable_quick_rice", "step_size": 2}
]

feature_list["start_running"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "step_size": 2},
]

feature_list["menu_selection"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index", "step_size": 8}
]

feature_list["delay_timer"] = [
    {"step": 1, "actions": ["press_delay_button"], "variable": "variable_delay_timer", "step_size": 13}
]

feature_list["keep_warm_cancel"] = [
    {"step": 1, "actions": ["press_keep_warm_cancel_button"], "variable": "variable_keep_warm_cancel", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_start_running = variable_start_running
        self.variable_menu_index = variable_menu_index
        self.variable_delay_timer = variable_delay_timer
        self.variable_quick_rice = variable_quick_rice
        self.variable_keep_warm_cancel = variable_keep_warm_cancel

    def press_start_button(self):
        # Update feature progress
        self.feature.update_progress("press_start_button")
        self.variable_start_running.set_current_value("on")

    def press_delay_button(self):
        # Update feature progress and adjust delay timer
        self.feature.update_progress("press_delay_button")
        current_variable = self.get_current_variable("press_delay_button")
        self.assign_variable_to_next(current_variable)

    def press_quick_rice_button(self):
        # Update feature progress and toggle quick rice function
        self.feature.update_progress("press_quick_rice_button")
        current_variable = self.get_current_variable("press_quick_rice_button")
        self.assign_variable_to_next(current_variable)

    def press_keep_warm_cancel_button(self):
        # Update feature progress and toggle keep warm/cancel function
        self.feature.update_progress("press_keep_warm_cancel_button")
        current_variable = self.get_current_variable("press_keep_warm_cancel_button")
        self.assign_variable_to_next(current_variable)

    def press_menu_button(self):
        # Update feature progress and change menu selection
        self.feature.update_progress("press_menu_button")
        current_variable = self.get_current_variable("press_menu_button")
        self.assign_variable_to_next(current_variable)
