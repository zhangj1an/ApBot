class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                'start_appliance': [{'step': 1, 'actions': ['press_start_button'], 'variable': 'variable_start_running', 'comment': 'value always set to on'}],
                'cancel_operation': [{'step': 1, 'actions': ['press_cancel_button'], 'variable': 'variable_start_running', 'comment': 'value always set to off'}],
                'select_cooking_program': [{'step': 1, 'actions': ['press_jasmine_rice_button', 'press_white_rice_button', 'press_brown_rice_button', 'press_glutinous_rice_button', 'press_clay_pot_button', 'press_quick_cooking_steam_button', 'press_soup_congee_button', 'press_slow_cook_stew_button', 'press_reheat_button'], 'variable': 'variable_cooking_program'}],
                'adjust_timer': [{'step': 1, 'actions': ['press_timer_button'], 'variable': 'variable_timer'}],
                'adjust_preset_time': [{'step': 1, 'actions': ['press_preset_button'], 'variable': 'variable_preset_time'}],
                'toggle_keep_warm': [{'step': 1, 'actions': ['press_and_hold_start_button', 'press_and_hold_start_button_and_cancel_button'], 'variable': 'variable_keep_warm'}],
                'null': [{'step': 1, 'actions': ['press_and_hold_cancel_button'], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_cooking_program = DiscreteVariable(
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
        self.variable_timer = ContinuousVariable(value_ranges_steps=[(0, 1440, 1)], current_value=0)  # Timer in minutes, max 24 hours
        self.variable_preset_time = ContinuousVariable(value_ranges_steps=[(0, 1440, 1)], current_value=0)  # Preset time in minutes, max 24 hours
        self.variable_keep_warm = DiscreteVariable(value_range=["on", "off"], current_value="off")

    def press_start_button(self):
        # Start the appliance by setting variable_start_running to "on"
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_appliance":
            self.variable_start_running.set_current_value("on")

    def press_cancel_button(self):
        # Cancel operation by setting variable_start_running to "off"
        self.feature.update_progress("press_cancel_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cancel_operation":
            self.variable_start_running.set_current_value("off")

    def press_jasmine_rice_button(self):
        # Select jasmine rice cooking program
        self.feature.update_progress("press_jasmine_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_cooking_program":
            self.variable_cooking_program.set_current_value("jasmine_rice")

    def press_white_rice_button(self):
        # Select white rice cooking program
        self.feature.update_progress("press_white_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_cooking_program":
            self.variable_cooking_program.set_current_value("white_rice")

    def press_brown_rice_button(self):
        # Select brown rice cooking program
        self.feature.update_progress("press_brown_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_cooking_program":
            self.variable_cooking_program.set_current_value("brown_rice")

    def press_glutinous_rice_button(self):
        # Select glutinous rice cooking program
        self.feature.update_progress("press_glutinous_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_cooking_program":
            self.variable_cooking_program.set_current_value("glutinous_rice")

    def press_clay_pot_button(self):
        # Select clay pot cooking program
        self.feature.update_progress("press_clay_pot_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_cooking_program":
            self.variable_cooking_program.set_current_value("clay_pot")

    def press_quick_cooking_steam_button(self):
        # Select quick cooking/steam program
        self.feature.update_progress("press_quick_cooking_steam_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_cooking_program":
            self.variable_cooking_program.set_current_value("quick_cooking_steam")

    def press_soup_congee_button(self):
        # Select soup/congee cooking program
        self.feature.update_progress("press_soup_congee_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_cooking_program":
            self.variable_cooking_program.set_current_value("soup_congee")

    def press_slow_cook_stew_button(self):
        # Select slow cook/stew program
        self.feature.update_progress("press_slow_cook_stew_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_cooking_program":
            self.variable_cooking_program.set_current_value("slow_cook_stew")

    def press_reheat_button(self):
        # Select reheat program
        self.feature.update_progress("press_reheat_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_cooking_program":
            self.variable_cooking_program.set_current_value("reheat")

    def press_timer_button(self):
        # Adjust the timer
        self.feature.update_progress("press_timer_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer":
            self.execute_action_and_set_next("press_timer_button")

    def press_preset_button(self):
        # Adjust the preset time
        self.feature.update_progress("press_preset_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_preset_time":
            self.execute_action_and_set_next("press_preset_button")

    def press_and_hold_start_button(self, duration=3):
        # Toggle keep warm functionality
        self.feature.update_progress("press_and_hold_start_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "toggle_keep_warm" and duration >= 3:
            self.variable_keep_warm.set_current_value("on")

    def press_and_hold_start_button_and_cancel_button(self, duration=3):
        # Toggle keep warm functionality
        self.feature.update_progress("press_and_hold_start_button_and_cancel_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "toggle_keep_warm" and duration >= 3:
            self.variable_keep_warm.set_current_value("off")

    def press_and_hold_cancel_button(self, duration=3):
        # Null action
        self.feature.update_progress("press_and_hold_cancel_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "null" and duration >= 3:
            pass

    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)