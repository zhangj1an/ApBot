# 4 variables

# Variable for menu selection
variable_menu_selection = DiscreteVariable(
    value_range=["White Rice", "Brown Rice", "Quinoa", "Steel Cut Oats"],
    current_value="White Rice"
)

# Variable for cooking time adjustment
variable_cooking_time = ContinuousVariable(
    value_ranges_steps=[(20, 40, 1)],  # Maximum cooking time is 90 minutes
    current_value=30
)

# Variable for delay timer
variable_delay_timer = ContinuousVariable(
    value_ranges_steps=[(0, 24, 0.5)],  # Delay timer can be set from 0 to 24 hours in 30-minute increments
    current_value=0
)

# Variable for start/stop functionality
variable_start_running = DiscreteVariable(
    value_range=["off", "on"],
    current_value="off"
)

# Note: The "Keep Warm" function is automatically activated after cooking, so no separate variable is needed for it.

feature_list = {}

feature_list["menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_selection", "step_size": 4},
    {"step": 2, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_cooking_time", "step_size": 3},
]

feature_list["delay_timer"] = [
    {"step": 1, "actions": ["press_delay_timer_button"]},
    {"step": 2, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_delay_timer", "step_size": 48},
]

feature_list["start"] = [
    {"step": 1, "actions": ["press_start_button"], "comment": "variable_start_running: set to 'on'", "step_size": 2}
]

feature_list["keep_warm_stop"] = [
    {"step": 1, "actions": ["press_keep_warm_stop_button"], "comment": "variable_start_running: set to 'off'", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_menu_selection = variable_menu_selection
        self.variable_cooking_time = variable_cooking_time
        self.variable_delay_timer = variable_delay_timer
        self.variable_start_running = variable_start_running

    def press_start_button(self):
        # Update feature progress
        self.feature.update_progress("press_start_button")
        self.variable_start_running.set_current_value("on")

    def press_delay_timer_button(self):
        # Update feature progress
        self.feature.update_progress("press_delay_timer_button")

    def press_keep_warm_stop_button(self):
        # Update feature progress
        self.feature.update_progress("press_keep_warm_stop_button")
        current_feature = self.feature.current_value[0]
        # Set variable_start_running to "off" when stop button is pressed
        if current_feature == "keep_warm_stop":
            self.variable_start_running.set_current_value("off")

    def press_minus_button(self):
        # Update feature progress and adjust variable value
        self.feature.update_progress("press_minus_button")
        current_variable = self.get_current_variable("press_minus_button")
        self.assign_variable_to_prev(current_variable)

    def press_plus_button(self):
        # Update feature progress and adjust variable value
        self.feature.update_progress("press_plus_button")
        current_variable = self.get_current_variable("press_plus_button")
        self.assign_variable_to_next(current_variable)

    def press_menu_button(self):
        # Update feature progress and adjust menu selection
        self.feature.update_progress("press_menu_button")
        current_variable = self.get_current_variable("press_menu_button")
        self.assign_variable_to_next(current_variable)