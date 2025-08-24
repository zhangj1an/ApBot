# 5 variables

# Variable for menu selection
variable_menu_index = DiscreteVariable(
    value_range=["1 Basic", "2 French", "3 Whole Wheat", "4 Quick", "5 Sweet", "6 Ultra Fast-I", "7 Ultra Fast - II", "8 Dough", "9 Jam", "10 Cake", "11 Sandwich", "12 Bake"],
    current_value="1 Basic"
)

# Variable for loaf size selection
variable_loaf_size = DiscreteVariable(
    value_range=["700g", "900g"],
    current_value="700g"
)

# Variable for crust color selection
variable_crust_color = DiscreteVariable(
    value_range=["Light", "Medium", "Dark"],
    current_value="Medium"
)

# Variable for start/stop operation
variable_start_running = DiscreteVariable(
    value_range=["on", "off"],
    current_value="off"
)

# Variable for delay timer
variable_delay_timer = ContinuousVariable(  
    value_ranges_steps=[(0, 13, 1)],  # Delay timer can be set from 0 to 13 hours in 1-hour increments
    current_value=0
)

feature_list = {}

feature_list["menu_selection"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index", "step_size": 12}
]

feature_list["loaf_size_selection"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size", "step_size": 2}
]

feature_list["crust_color_selection"] = [
    {"step": 1, "actions": ["press_color_button"], "variable": "variable_crust_color", "step_size": 3}
]

feature_list["delay_timer_setting"] = [
    {"step": 1, "actions": ["press_time_plus_button", "press_time_minus_button"], "variable": "variable_delay_timer", "step_size": 14}
]

feature_list["start_stop_operation"] = [
    {"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_menu_index = variable_menu_index
        self.variable_loaf_size = variable_loaf_size
        self.variable_crust_color = variable_crust_color
        self.variable_start_running = variable_start_running
        self.variable_delay_timer = variable_delay_timer

    def press_menu_button(self):
        # Update feature progress and adjust the menu index variable
        self.feature.update_progress("press_menu_button")
        self.execute_action_and_set_next("press_menu_button")

    def press_loaf_size_button(self):
        # Update feature progress and adjust the loaf size variable
        self.feature.update_progress("press_loaf_size_button")
        self.execute_action_and_set_next("press_loaf_size_button")

    def press_color_button(self):
        # Update feature progress and adjust the crust color variable
        self.feature.update_progress("press_color_button")
        self.execute_action_and_set_next("press_color_button")

    def press_time_plus_button(self):
        # Update feature progress and increase the delay timer
        self.feature.update_progress("press_time_plus_button")
        self.execute_action_and_set_next("press_time_plus_button")

    def press_time_minus_button(self):
        # Update feature progress and decrease the delay timer
        self.feature.update_progress("press_time_minus_button")
        self.execute_action_and_set_prev("press_time_minus_button")

    def press_start_stop_button(self):
        # Update feature progress and toggle the start/stop operation
        self.feature.update_progress("press_start_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_stop_operation":
            if self.variable_start_running.get_current_value() == "off":
                self.variable_start_running.set_current_value("on")
            else:
                self.variable_start_running.set_current_value("off")