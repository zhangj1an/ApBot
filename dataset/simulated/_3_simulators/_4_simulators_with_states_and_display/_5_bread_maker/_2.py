# 5 variables

# Variable for menu selection
variable_menu_index = DiscreteVariable(
    value_range=["1 Basic White", "2 French", "3 Wholewheat", "4 Quick", "5 Sweet", "6 Fastbake I", "7 Fastbake II", "8 Dough", "9 Jam", "10 Cake", "11 Sandwich", "12 Extrabake"],
    current_value="1 Basic White"
)

# Variable for loaf size selection
variable_loaf_size = DiscreteVariable(
    value_range=["small", "large"],
    current_value="small"
)

# Variable for crust color selection
variable_crust_color = DiscreteVariable(
    value_range=["light", "medium", "dark"],
    current_value="light"
)

# Variable for timer delay
variable_timer_delay = ContinuousVariable(
    value_ranges_steps=[(0, 13, 1)],  # 1 hour step, total 13 hours
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

feature_list["loaf_size_selection"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size", "step_size": 2}
]

feature_list["crust_color_selection"] = [
    {"step": 1, "actions": ["press_crust_button"], "variable": "variable_crust_color", "step_size": 3}
]

feature_list["timer_delay"] = [
    {"step": 1, "actions": ["press_time_down_button", "press_time_up_button"], "variable": "variable_timer_delay", "step_size": 14}
]

feature_list["start_stop"] = [
    {"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_menu_index = variable_menu_index
        self.variable_loaf_size = variable_loaf_size
        self.variable_crust_color = variable_crust_color
        self.variable_timer_delay = variable_timer_delay
        self.variable_start_running = variable_start_running

    def press_menu_button(self):
        # Update feature progress and set the next menu index
        self.feature.update_progress("press_menu_button")
        self.execute_action_and_set_next("press_menu_button")

    def press_loaf_size_button(self):
        # Update feature progress and set the next loaf size
        self.feature.update_progress("press_loaf_size_button")
        self.execute_action_and_set_next("press_loaf_size_button")

    def press_crust_button(self):
        # Update feature progress and set the next crust color
        self.feature.update_progress("press_crust_button")
        self.execute_action_and_set_next("press_crust_button")

    def press_time_down_button(self):
        # Update feature progress and decrease the timer delay
        self.feature.update_progress("press_time_down_button")
        self.execute_action_and_set_prev("press_time_down_button")

    def press_time_up_button(self):
        # Update feature progress and increase the timer delay
        self.feature.update_progress("press_time_up_button")
        self.execute_action_and_set_next("press_time_up_button")

    def press_start_stop_button(self):
        # Update feature progress and toggle the start/stop state
        self.feature.update_progress("press_start_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_stop":
            if self.variable_start_running.get_current_value() == "off":
                self.variable_start_running.set_current_value("on")
            else:
                self.variable_start_running.set_current_value("off")