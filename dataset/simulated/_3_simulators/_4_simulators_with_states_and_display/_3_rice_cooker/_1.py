# 7 variables

# Variable for starting the cooking process
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for menu selection
variable_menu_index = DiscreteVariable(
    value_range=["Glutinous rice", "Porridge", "Bean", "Soup", "Steam", "Reheat"],
    current_value="Glutinous rice"
)

# Variable for cooking time adjustment
variable_cooking_time_hour = ContinuousVariable(
    value_ranges_steps=[(0, 4, 1)],  # 0 to 240 minutes
    current_value=0
)

variable_cooking_time_minute = ContinuousVariable(
    value_ranges_steps=[(0, 50, 10)],  # 0 to 240 minutes
    current_value=0
)

# Variable for preset timer
variable_preset_timer_hour = ContinuousVariable(
    value_ranges_steps=[(0, 24, 1)],  # 0 to 1440 minutes (24 hours)
    current_value=0
)

variable_preset_timer_minute = ContinuousVariable(
    value_ranges_steps=[(0, 60, 30)],  # 0 to 1440 minutes (24 hours)
    current_value=0
)

# Variable for keep warm/cancel
variable_keep_warm_cancel = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Note: The current value of variable_menu_index will determine the initiation of other variables.
# For example, if "Porridge" is selected, the cooking time can be adjusted between 1-4 hours.
# This will be implemented in the appliance's actions.

feature_list = {}

feature_list["cooking"] = [
    {"step": 1, "actions": ["press_white_button", "press_brown_rice_button", "press_menu_button"], "variable": "variable_menu_index", "step_size": 1},
]

feature_list["start"] = [
    {"step": 1, "actions": ["press_start_button"], "comment": "variable_start_running: set to on", "step_size": 2}
]

feature_list["adjust_cooking_time"] = [
    {"step": 1, "actions": ["press_cooking_time_button"]},
    {"step": 2, "actions": ["press_hr_button"], "variable": "variable_cooking_time_hour", "skip_to": 3, "step_size": 4},
    {"step": 3, "actions": ["press_min_button"], "variable": "variable_cooking_time_minute", "step_size": 6}
]

feature_list["preset_timer"] = [
    {"step": 1, "actions": ["press_preset_timer_button"]},
    {"step": 2, "actions": ["press_hr_button"], "variable": "variable_preset_timer_hour", "skip_to": 3, "step_size": 24},
    {"step": 3, "actions": ["press_min_button"], "variable": "variable_preset_timer_minute", "step_size": 3}
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
        self.variable_cooking_time_hour = variable_cooking_time_hour
        self.variable_cooking_time_minute = variable_cooking_time_minute
        self.variable_preset_timer_hour = variable_preset_timer_hour 
        self.variable_preset_timer_minute = variable_preset_timer_minute
        self.variable_keep_warm_cancel = variable_keep_warm_cancel

    def press_start_button(self):
        # Update feature progress and set variable_start_running to "on"
        self.feature.update_progress("press_start_button")
        self.variable_start_running.set_current_value("on")

    def press_preset_timer_button(self):
        # Update feature progress for preset timer
        self.feature.update_progress("press_preset_timer_button")

    def press_hr_button(self):
        # Update feature progress and adjust the current variable's hour value
        self.feature.update_progress("press_hr_button")
        current_variable = self.get_current_variable("press_hr_button")
        self.assign_variable_to_next(current_variable)

    def press_cooking_time_button(self):
        # Update feature progress for cooking time adjustment
        self.feature.update_progress("press_cooking_time_button")

    def press_menu_button(self):
        # Update feature progress and adjust the menu index
        self.feature.update_progress("press_menu_button")
        current_variable = self.get_current_variable("press_menu_button")
        self.assign_variable_to_next(current_variable)

    def press_brown_rice_button(self):
        # Update feature progress and set menu index to "Brown rice"
        self.feature.update_progress("press_brown_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking":
            self.variable_menu_index.set_current_value("Brown rice")

    def press_min_button(self):
        # Update feature progress and adjust the current variable's minute value
        self.feature.update_progress("press_min_button")
        current_variable = self.get_current_variable("press_min_button")
        self.assign_variable_to_next(current_variable)

    def press_keep_warm_cancel_button(self):
        # Update feature progress and toggle keep warm/cancel state
        self.feature.update_progress("press_keep_warm_cancel_button")
        current_variable = self.get_current_variable("press_keep_warm_cancel_button")
        self.assign_variable_to_next(current_variable)

    def press_white_button(self):
        # Update feature progress and set menu index to "White rice"
        self.feature.update_progress("press_white_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking":
            self.variable_menu_index.set_current_value("White rice")