# 5 variables

# Variable for menu selection
variable_menu_index = DiscreteVariable(
    value_range=[
        "BASIC", "FRENCH", "WHOLE WHEAT", "QUICK", "SWEET", 
        "GLUTEN FREE", "RAPID BAKE", "DOUGH", "JAM", 
        "CAKE", "SANDWICH", "BAKE"
    ], 
    current_value="BASIC"
)

# Variable for crust color selection
variable_crust_color = DiscreteVariable(
    value_range=["LIGHT", "MEDIUM", "DARK"], 
    current_value="MEDIUM"
)

# Variable for loaf size selection
variable_loaf_size = DiscreteVariable(
    value_range=["1.5LB", "2.0LB"], 
    current_value="1.5LB"
)

# Variable for delay time setting
variable_delay_time = ContinuousVariable(
    value_ranges_steps=[(0, 13, 1)],  # 1 hour increments, total 13 hours
    current_value=0
)

# Variable for start/stop operation
variable_start_running = DiscreteVariable(
    value_range=["on", "off"], 
    current_value="off"
)

feature_list = {}

feature_list["menu_selection"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index", "step_size": 12}
]

feature_list["crust_color_selection"] = [
    {"step": 1, "actions": ["press_color_button"], "variable": "variable_crust_color", "step_size": 3}
]

feature_list["loaf_size_selection"] = [
    {"step": 1, "actions": ["press_loaf_button"], "variable": "variable_loaf_size", "step_size": 2}
]

feature_list["delay_time_setting"] = [
    {"step": 1, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_delay_time", "step_size": 14}
]

feature_list["start_stop_operation"] = [
    {"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["stop_operation"] = [
    {"step": 1, "actions": ["press_and_hold_start_stop_button"], "variable": "variable_start_running", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_menu_index = variable_menu_index
        self.variable_crust_color = variable_crust_color
        self.variable_loaf_size = variable_loaf_size
        self.variable_delay_time = variable_delay_time
        self.variable_start_running = variable_start_running

    def press_menu_button(self):
        # Update feature progress and adjust the menu index variable
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "menu_selection":
            self.execute_action_and_set_next("press_menu_button")

    def press_color_button(self):
        # Update feature progress and adjust the crust color variable
        self.feature.update_progress("press_color_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "crust_color_selection":
            self.execute_action_and_set_next("press_color_button")

    def press_loaf_button(self):
        # Update feature progress and adjust the loaf size variable
        self.feature.update_progress("press_loaf_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "loaf_size_selection":
            self.execute_action_and_set_next("press_loaf_button")

    def press_plus_button(self):
        # Update feature progress and increase the delay time variable
        self.feature.update_progress("press_plus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "delay_time_setting":
            self.execute_action_and_set_next("press_plus_button")

    def press_minus_button(self):
        # Update feature progress and decrease the delay time variable
        self.feature.update_progress("press_minus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "delay_time_setting":
            self.execute_action_and_set_prev("press_minus_button")

    def press_start_stop_button(self):
        # Update feature progress and toggle the start/stop operation
        self.feature.update_progress("press_start_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_stop_operation":
            self.variable_start_running.set_current_value("on" if self.variable_start_running.get_current_value() == "off" else "off")

    def press_and_hold_start_stop_button(self, duration=2):
        # Update feature progress and stop the operation if held for 2 seconds
        self.feature.update_progress("press_and_hold_start_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "stop_operation" and duration >= 2:
            self.variable_start_running.set_current_value("off")