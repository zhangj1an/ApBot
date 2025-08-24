# 5 variables

# Variable for cooking program selection
variable_cooking_program = DiscreteVariable(
    value_range=[
        "jasmine_rice", 
        "white_rice", 
        "brown_rice", 
        "glutinous_rice", 
        "clay_pot", 
        "soup_congee", 
        "quick_cooking_steam", 
        "slow_cook_stew", 
        "reheat"
    ], 
    current_value="jasmine_rice"
)

# Variable for start running
variable_start_running = DiscreteVariable(
    value_range=["on", "off"], 
    current_value="off"
)

# Variable for preset time
variable_preset_time = TimeVariable(
    value_ranges_steps=[("00:00:00", "24:00:00", 600)], 
    current_value="00:00:00"
)

# Variable for timer
variable_timer = TimeVariable(
    value_ranges_steps=[("00:00:00", "24:00:00", 600)], 
    current_value="00:00:00"
)

# Variable for keep warm
variable_keep_warm = DiscreteVariable(
    value_range=["on", "off"], 
    current_value="off"
)

feature_list = {}

feature_list["cooking_program_selection"] = [
    {"step": 1, "actions": ["press_jasmine_rice_button", "press_white_rice_button", "press_brown_rice_button", "press_glutinous_rice_button", "press_clay_pot_button", "press_soup_congee_button", "press_quick_cooking_steam_button", "press_slow_cook_stew_button", "press_reheat_button"], "variable": "variable_cooking_program", "step_size": 9}
]

feature_list["start_function"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["preset_time"] = [
    {"step": 1, "actions": ["press_preset_button"], "variable": "variable_preset_time", "step_size": 100},
]

feature_list["timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer", "step_size": 100}
]

feature_list["keep_warm"] = [
    {"step": 1, "actions": ["press_cancel_button"], "variable": "variable_keep_warm", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_cooking_program = variable_cooking_program
        self.variable_start_running = variable_start_running
        self.variable_preset_time = variable_preset_time
        self.variable_timer = variable_timer
        self.variable_keep_warm = variable_keep_warm

    def press_preset_button(self):
        # Update feature progress for preset time setting
        self.feature.update_progress("press_preset_button")
        self.execute_action_and_set_next("press_preset_button")

    def press_start_button(self):
        # Update feature progress and set start running to "on"
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_function":
            self.variable_start_running.set_current_value("on")

    def press_glutinous_rice_button(self):
        # Update feature progress and set cooking program to "glutinous_rice"
        self.feature.update_progress("press_glutinous_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_program_selection":
            self.variable_cooking_program.set_current_value("glutinous_rice")

    def press_white_rice_button(self):
        # Update feature progress and set cooking program to "white_rice"
        self.feature.update_progress("press_white_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_program_selection":
            self.variable_cooking_program.set_current_value("white_rice")

    def press_reheat_button(self):
        # Update feature progress and set cooking program to "reheat"
        self.feature.update_progress("press_reheat_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_program_selection":
            self.variable_cooking_program.set_current_value("reheat")

    def press_cancel_button(self):
        # Update feature progress and toggle keep warm setting
        self.feature.update_progress("press_cancel_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "keep_warm":
            current_value = self.variable_keep_warm.get_current_value()
            new_value = "off" if current_value == "on" else "on"
            self.variable_keep_warm.set_current_value(new_value)

    def press_slow_cook_stew_button(self):
        # Update feature progress and set cooking program to "slow_cook_stew"
        self.feature.update_progress("press_slow_cook_stew_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_program_selection":
            self.variable_cooking_program.set_current_value("slow_cook_stew")

    def press_brown_rice_button(self):
        # Update feature progress and set cooking program to "brown_rice"
        self.feature.update_progress("press_brown_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_program_selection":
            self.variable_cooking_program.set_current_value("brown_rice")

    def press_jasmine_rice_button(self):
        # Update feature progress and set cooking program to "jasmine_rice"
        self.feature.update_progress("press_jasmine_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_program_selection":
            self.variable_cooking_program.set_current_value("jasmine_rice")

    def press_clay_pot_button(self):
        # Update feature progress and set cooking program to "clay_pot"
        self.feature.update_progress("press_clay_pot_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_program_selection":
            self.variable_cooking_program.set_current_value("clay_pot")

    def press_quick_cooking_steam_button(self):
        # Update feature progress and set cooking program to "quick_cooking_steam"
        self.feature.update_progress("press_quick_cooking_steam_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_program_selection":
            self.variable_cooking_program.set_current_value("quick_cooking_steam")

    def press_soup_congee_button(self):
        # Update feature progress and set cooking program to "soup_congee"
        self.feature.update_progress("press_soup_congee_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_program_selection":
            self.variable_cooking_program.set_current_value("soup_congee")

    def press_timer_button(self):
        # Update feature progress and adjust timer or preset time
        self.feature.update_progress("press_timer_button")
        current_feature = self.feature.current_value[0]
        self.execute_action_and_set_next("press_timer_button")
        
