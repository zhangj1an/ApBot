# 6 variables
# Variable for menu selection
variable_menu_index = DiscreteVariable(
    value_range=["1 Basic", "2 French", "3 Whole Wheat", "4 Sweet", "5 Express 680g", "6 Express 900g", "7 Yeast Free", "8 Continental", "9 Dough", "10 Gluten Free", "11 Jam", "12 Bake"],
    current_value="1 Basic"
)

# Variable for crust color
variable_crust_colour = DiscreteVariable(
    value_range=["Light", "Medium", "Dark", "Rapid"],
    current_value="Light"
)

# Variable for loaf size
variable_loaf_size = DiscreteVariable(
    value_range=["450g", "680g", "900g"],
    current_value="450g"
)

# Variable for gluten free setting
variable_gluten_free = DiscreteVariable(
    value_range=["off", "on"],
    current_value="off"
)

# Variable for timer
variable_timer = ContinuousVariable(value_ranges_steps=[(0, 15, 1)], current_value=0)

# Variable for start/cancel
variable_start_running = DiscreteVariable(
    value_range=["off", "on"],
    current_value="off"
)

feature_list = {}

feature_list["menu_selection"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index", "step_size": 12}
]

feature_list["crust_colour_selection"] = [
    {"step": 1, "actions": ["press_crust_colour_button"], "variable": "variable_crust_colour", "step_size": 4}
]

feature_list["loaf_size_selection"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size", "step_size": 3}
]

feature_list["gluten_free_selection"] = [
    {"step": 1, "actions": ["press_gluten_free_button"], "variable": "variable_gluten_free", "step_size": 2}
]

feature_list["timer_adjustment"] = [
    {"step": 1, "actions": ["press_timer_up_button", "press_timer_down_button"], "variable": "variable_timer", "step_size": 16}
]

feature_list["start_cancel_function"] = [
    {"step": 1, "actions": ["press_start_cancel_button"], "variable": "variable_start_running", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_menu_index = variable_menu_index
        self.variable_crust_colour = variable_crust_colour
        self.variable_loaf_size = variable_loaf_size
        self.variable_gluten_free = variable_gluten_free
        self.variable_timer = variable_timer
        self.variable_start_running = variable_start_running

    def press_menu_button(self):
        # Update feature progress and set the menu index to the next value
        self.feature.update_progress("press_menu_button")
        self.execute_action_and_set_next("press_menu_button")

    def press_crust_colour_button(self):
        # Update feature progress and set the crust color to the next value
        self.feature.update_progress("press_crust_colour_button")
        self.execute_action_and_set_next("press_crust_colour_button")

    def press_loaf_size_button(self):
        # Update feature progress and set the loaf size to the next value
        self.feature.update_progress("press_loaf_size_button")
        self.execute_action_and_set_next("press_loaf_size_button")

    def press_gluten_free_button(self):
        # Update feature progress and toggle the gluten free setting
        self.feature.update_progress("press_gluten_free_button")
        self.variable_gluten_free.set_current_value("on")

    def press_timer_up_button(self):
        # Update feature progress and increase the timer value
        self.feature.update_progress("press_timer_up_button")
        self.execute_action_and_set_next("press_timer_up_button")

    def press_timer_down_button(self):
        # Update feature progress and decrease the timer value
        self.feature.update_progress("press_timer_down_button")
        self.execute_action_and_set_prev("press_timer_down_button")

    def press_start_cancel_button(self):
        # Update feature progress and toggle the start/cancel setting
        self.feature.update_progress("press_start_cancel_button")
        self.variable_start_running.set_current_value("on")
